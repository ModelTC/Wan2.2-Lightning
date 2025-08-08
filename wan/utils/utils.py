# Copyright 2024-2025 The Alibaba Wan Team Authors. All rights reserved.
import argparse
import binascii
import logging
import os
import os.path as osp
import torch.nn as nn
import imageio
import torch
import torchvision
from safetensors import safe_open

__all__ = ['save_video', 'save_image', 'str2bool', "use_cfg", "model_safe_downcast", "load_and_merge_lora_weight_from_safetensors"]

def use_cfg(cfg_scale:float=1.0, eps:float=1e-6):
    return abs(cfg_scale - 1.0) > eps


def model_safe_downcast(
    model: nn.Module, 
    dtype: torch.dtype = torch.bfloat16, 
    keep_in_fp32_modules: list[str]|tuple[str,...]|None = None, 
    keep_in_fp32_parameters: list[str]|tuple[str,...]|None = None,
    verbose: bool = False,
) -> nn.Module:
    """
    Downcast model parameters and buffers to a specified dtype, while keeping certain modules/parameters in fp32.

    Args:
        model: The PyTorch model to downcast
        dtype: The target dtype to downcast to (default: torch.bfloat16)
        keep_in_fp32_modules: List of module names to keep in fp32, fuzzy matching is supported
        keep_in_fp32_parameters: List of parameter names to keep in fp32, exact matching is required
        verbose: Whether to print information.

    Returns:
        The downcast model (modified in-place)
    """
    keep_in_fp32_modules = list(keep_in_fp32_modules or [])
    keep_in_fp32_modules.extend(getattr(model, "_keep_in_fp32_modules", []))
    keep_in_fp32_parameters = keep_in_fp32_parameters or []

    for name, module in model.named_modules():
        # Skip if module is in keep_in_fp32_modules list
        if any(keep_name in name for keep_name in keep_in_fp32_modules):
            if verbose:
                print(f"Skipping {name} because it is in keep_in_fp32_modules")
            continue

        # Downcast parameters
        for param_name, param in module.named_parameters(recurse=False):
            full_param_name = f"{name}.{param_name}" if name else param_name
            if param is not None:
                if full_param_name in keep_in_fp32_parameters and verbose:
                    print(f"Skipping {full_param_name} because it is in keep_in_fp32_parameters")
                # if not any(keep_name in full_param_name for keep_name in keep_in_fp32_parameters):
                else:
                    param.data = param.data.to(dtype)

        # Downcast buffers
        for buffer_name, buffer in module.named_buffers(recurse=False):
            if buffer is not None:
                buffer.data = buffer.data.to(dtype)
    return model

def build_lora_names(key, lora_down_key, lora_up_key, is_native_weight):
    base = "diffusion_model." if is_native_weight else ""
    lora_down = base + key.replace(".weight", lora_down_key)
    lora_up = base + key.replace(".weight", lora_up_key)
    lora_alpha = base + key.replace(".weight", ".alpha")
    return lora_down, lora_up, lora_alpha

def load_and_merge_lora_weight(
    model: nn.Module,
    lora_state_dict: dict,
    lora_down_key: str=".lora_down.weight",
    lora_up_key: str=".lora_up.weight"):
    is_native_weight = any("diffusion_model." in key for key in lora_state_dict)
    for key, value in model.named_parameters():
        lora_down_name, lora_up_name, lora_alpha_name = build_lora_names(
            key, lora_down_key, lora_up_key, is_native_weight
        )
        if lora_down_name in lora_state_dict:
            lora_down = lora_state_dict[lora_down_name]
            lora_up = lora_state_dict[lora_up_name]
            lora_alpha = float(lora_state_dict[lora_alpha_name])
            rank = lora_down.shape[0]
            scaling_factor = lora_alpha / rank
            assert lora_up.dtype == torch.float32
            assert lora_down.dtype == torch.float32
            delta_W = scaling_factor * torch.matmul(lora_up, lora_down)
            value.data = value.data + delta_W
    return model


def load_and_merge_lora_weight_from_safetensors(
    model: nn.Module,
    lora_weight_path:str,
    lora_down_key:str=".lora_down.weight",
    lora_up_key:str=".lora_up.weight"):
    lora_state_dict = {}
    with safe_open(lora_weight_path, framework="pt", device="cpu") as f:
        for key in f.keys():
            lora_state_dict[key] = f.get_tensor(key)
    model = load_and_merge_lora_weight(model, lora_state_dict, lora_down_key, lora_up_key)
    return model

def rand_name(length=8, suffix=''):
    name = binascii.b2a_hex(os.urandom(length)).decode('utf-8')
    if suffix:
        if not suffix.startswith('.'):
            suffix = '.' + suffix
        name += suffix
    return name


def save_video(tensor,
               save_file=None,
               fps=30,
               suffix='.mp4',
               nrow=8,
               normalize=True,
               value_range=(-1, 1)):
    # cache file
    cache_file = osp.join('/tmp', rand_name(
        suffix=suffix)) if save_file is None else save_file

    # save to cache
    try:
        # preprocess
        tensor = tensor.clamp(min(value_range), max(value_range))
        tensor = torch.stack([
            torchvision.utils.make_grid(
                u, nrow=nrow, normalize=normalize, value_range=value_range)
            for u in tensor.unbind(2)
        ],
                             dim=1).permute(1, 2, 3, 0)
        tensor = (tensor * 255).type(torch.uint8).cpu()

        # write video
        writer = imageio.get_writer(
            cache_file, fps=fps, codec='libx264', quality=8)
        for frame in tensor.numpy():
            writer.append_data(frame)
        writer.close()
    except Exception as e:
        logging.info(f'save_video failed, error: {e}')


def save_image(tensor, save_file, nrow=8, normalize=True, value_range=(-1, 1)):
    # cache file
    suffix = osp.splitext(save_file)[1]
    if suffix.lower() not in [
            '.jpg', '.jpeg', '.png', '.tiff', '.gif', '.webp'
    ]:
        suffix = '.png'

    # save to cache
    try:
        tensor = tensor.clamp(min(value_range), max(value_range))
        torchvision.utils.save_image(
            tensor,
            save_file,
            nrow=nrow,
            normalize=normalize,
            value_range=value_range)
        return save_file
    except Exception as e:
        logging.info(f'save_image failed, error: {e}')


def str2bool(v):
    """
    Convert a string to a boolean.

    Supported true values: 'yes', 'true', 't', 'y', '1'
    Supported false values: 'no', 'false', 'f', 'n', '0'

    Args:
        v (str): String to convert.

    Returns:
        bool: Converted boolean value.

    Raises:
        argparse.ArgumentTypeError: If the value cannot be converted to boolean.
    """
    if isinstance(v, bool):
        return v
    v_lower = v.lower()
    if v_lower in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v_lower in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected (True/False)')


def masks_like(tensor, zero=False, generator=None, p=0.2):
    assert isinstance(tensor, list)
    out1 = [torch.ones(u.shape, dtype=u.dtype, device=u.device) for u in tensor]

    out2 = [torch.ones(u.shape, dtype=u.dtype, device=u.device) for u in tensor]

    if zero:
        if generator is not None:
            for u, v in zip(out1, out2):
                random_num = torch.rand(
                    1, generator=generator, device=generator.device).item()
                if random_num < p:
                    u[:, 0] = torch.normal(
                        mean=-3.5,
                        std=0.5,
                        size=(1,),
                        device=u.device,
                        generator=generator).expand_as(u[:, 0]).exp()
                    v[:, 0] = torch.zeros_like(v[:, 0])
                else:
                    u[:, 0] = u[:, 0]
                    v[:, 0] = v[:, 0]
        else:
            for u, v in zip(out1, out2):
                u[:, 0] = torch.zeros_like(u[:, 0])
                v[:, 0] = torch.zeros_like(v[:, 0])

    return out1, out2


def best_output_size(w, h, dw, dh, expected_area):
    # float output size
    ratio = w / h
    ow = (expected_area * ratio)**0.5
    oh = expected_area / ow

    # process width first
    ow1 = int(ow // dw * dw)
    oh1 = int(expected_area / ow1 // dh * dh)
    assert ow1 % dw == 0 and oh1 % dh == 0 and ow1 * oh1 <= expected_area
    ratio1 = ow1 / oh1

    # process height first
    oh2 = int(oh // dh * dh)
    ow2 = int(expected_area / oh2 // dw * dw)
    assert oh2 % dh == 0 and ow2 % dw == 0 and ow2 * oh2 <= expected_area
    ratio2 = ow2 / oh2

    # compare ratios
    if max(ratio / ratio1, ratio1 / ratio) < max(ratio / ratio2,
                                                 ratio2 / ratio):
        return ow1, oh1
    else:
        return ow2, oh2
