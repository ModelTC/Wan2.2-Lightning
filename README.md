# Wan2.2-Lightning


-----

<!-- [**Wan2.2-Lightning: Distill Wan2.2 Family into 4 Steps**] <be> -->


We are excited to release the distilled version of <a href="https://wan.video"><b>Wan2.2</b></a> video generation model family, which offers the following advantages:
- **Fast**: Video generation now requires only 4 steps without the need of CFG trick, leading to x20 speed-up
- **High-quality**: The distilled model delivers visuals on par with the base model in most scenarios, sometimes even better.
- **Complex Motion Generation**: Despite the reduction to just 4 steps, the model retains excellent motion dynamics in the generated scenes.

## 🔥 Latest News!!
* Aug 07, 2025: 👋 We have open the  [Wan2.2-I2V-A14B-NFE4-V1](https://hf-mirror.com/lightx2v/Wan2.2-Lightning/tree/main/Wan2.2-I2V-A14B-4steps-lora-rank64-Seko-V1). A [workflow](https://hf-mirror.com/lightx2v/Wan2.2-Lightning/blob/main/Wan2.2-I2V-A14B-4steps-lora-rank64-Seko-V1/Wan2.2-I2V-A14B-4steps-lora-rank64-Seko-V1-forKJ.json) compatible with [Kijai's ComfyUI WanVideoWrapper](https://github.com/kijai/ComfyUI-WanVideoWrapper) is inside this link. Enjoy!
* Aug 07, 2025: 👋 We have open the  [Wan2.2-T2V-A14B-NFE4-V1.1](https://hf-mirror.com/lightx2v/Wan2.2-Lightning/tree/main/Wan2.2-T2V-A14B-4steps-lora-rank64-Seko-V1.1). A [workflow](https://hf-mirror.com/lightx2v/Wan2.2-Lightning/blob/main/Wan2.2-T2V-A14B-4steps-lora-rank64-Seko-V1.1/Wan2.2-T2V-A14B-4steps-lora-rank64-Seko-V1.1-forKJ.json) compatible with [Kijai's ComfyUI WanVideoWrapper](https://github.com/kijai/ComfyUI-WanVideoWrapper) is inside this link. The generation quality of V1.1 is slightly better than V1. Enjoy!
* Aug 04, 2025: 👋 We have open the  [Wan2.2-T2V-A14B-NFE4-V1](https://hf-mirror.com/lightx2v/Wan2.2-Lightning/tree/main/Wan2.2-T2V-A14B-4steps-lora-rank64-Seko-V1). Enjoy!
- [Kijai's ComfyUI WanVideoWrapper](https://github.com/kijai/ComfyUI-WanVideoWrapper) is an implementation of Wan models for ComfyUI. Thanks to its Wan-only focus, it's on the frontline of getting cutting edge optimizations and hot research features.

## Video Demos
### Wan2.2-I2V-A14B-NFE4-V1 Demo

The videos below can be reproduced using [examples/i2v_prompt_list.txt](examples/i2v_prompt_list.txt) and [examples/i2v_image_path_list.txt](examples/i2v_image_path_list.txt).

<table border="0" style="width: 100%; text-align: left; margin-top: 20px;">
  <tr>
      <td>
          <video src="https://github.com/user-attachments/assets/4f6bb1e0-9e2b-4eb2-8b9f-0678ccd5b4ec" width="100%" controls loop></video>
      </td>
      <td>
          <video src="https://github.com/user-attachments/assets/bb249553-3f52-40b3-88f9-6e3bca1a8358" width="100%" controls loop></video>
      </td>
       <td>
          <video src="https://github.com/user-attachments/assets/17a6d26a-dd63-47ef-9a98-1502f503dfba" width="100%" controls loop></video>
     </td>
  </tr>
  <tr>
      <td>
          <video src="https://github.com/user-attachments/assets/6ccc69cf-e129-456f-8b93-6dc709cb0ede" width="100%" controls loop></video>
      </td>
      <td>
          <video src="https://github.com/user-attachments/assets/6cf9c586-f37a-47ed-ab5b-e106c3877fa8" width="100%" controls loop></video>
      </td>
       <td>
          <video src="https://github.com/user-attachments/assets/27e82fdf-88af-44ac-b987-b48aa3f9f793" width="100%" controls loop></video>
     </td>
  </tr>
  <tr>
      <td>
          <video src="https://github.com/user-attachments/assets/36a76f1d-2b64-4b16-a862-210d0ffd6d55" width="100%" controls loop></video>
      </td>
      <td>
          <video src="https://github.com/user-attachments/assets/4bc36c70-931e-4539-be8c-432d832819d3" width="100%" controls loop></video>
      </td>
       <td>
          <video src="https://github.com/user-attachments/assets/488b9179-741b-4b9d-8f23-895981f054cb" width="100%" controls loop></video>
     </td>
  </tr>
</table>

### Wan2.2-T2V-A14B-NFE4-V1 Demo

The videos below can be reproduced using [examples/prompt_list.txt](examples/prompt_list.txt).

<table border="0" style="width: 100%; text-align: left; margin-top: 20px;">
  <tr>
      <td>
          <video src="https://github.com/user-attachments/assets/ae791fbb-ef4a-4f72-989a-2ac862883201" width="100%" controls loop></video>
      </td>
      <td>
          <video src="https://github.com/user-attachments/assets/f8083a50-25a0-42a8-9cd1-635f99588b19" width="100%" controls loop></video>
      </td>
       <td>
          <video src="https://github.com/user-attachments/assets/5f15826b-b07b-49a2-a522-f2caea0adc60" width="100%" controls loop></video>
     </td>
  </tr>
  <tr>
      <td>
          <video src="https://github.com/user-attachments/assets/9e48c7c2-f1a1-4d94-ade0-11e1aa913cb7" width="100%" controls loop></video>
      </td>
      <td>
          <video src="https://github.com/user-attachments/assets/45ae83df-af1e-4506-b00e-7d413a0dfa51" width="100%" controls loop></video>
      </td>
       <td>
          <video src="https://github.com/user-attachments/assets/554dd476-d9c1-49df-b6e1-d129113cb2be" width="100%" controls loop></video>
     </td>
  </tr>
  <tr>
      <td>
          <video src="https://github.com/user-attachments/assets/f22b8c0f-9e40-418d-8cd5-153da3678093" width="100%" controls loop></video>
      </td>
      <td>
          <video src="https://github.com/user-attachments/assets/2fc03af0-7c76-48e5-ab12-fc222164ec64" width="100%" controls loop></video>
      </td>
       <td>
          <video src="https://github.com/user-attachments/assets/a8d07ae6-f037-4518-9b13-4a6702a3e0ae" width="100%" controls loop></video>
     </td>
  </tr>
</table>

### Wan2.2-T2V-A14B-NFE4 Limitation

When the video contains elements with extremely large motion, the generated results may include artifacts.
In some results, the direction of the vehicles may be reversed.

<table border="0" style="width: 100%; text-align: left; margin-top: 20px;">
  <tr>
      <td>
          <video src="https://github.com/user-attachments/assets/db8f4240-7feb-4b95-8851-c52220ece9dc" width="100%" controls loop></video>
      </td>
      <td>
          <video src="https://github.com/user-attachments/assets/43820463-22e0-41aa-a446-e0f130ef80d0" width="100%" controls loop></video>
      </td>
       <td>
          <video src="https://github.com/user-attachments/assets/8a0580eb-2b35-4548-abcb-45fc0df12ff0" width="100%" controls loop></video>
     </td>
  </tr>
</table>



## 📑 Todo List
- [x] Wan2.2-T2V-A14B-4steps
- [x] Wan2.2-I2V-A14B-4steps
- [ ] Wan2.2-TI2V-5B-4steps

## 🚀 Run Wan2.2-Lightning

#### Installation

Please follow [Wan2.2 Official Github](https://github.com/Wan-Video/Wan2.2/) to install the **Python Environment** and download the **Base Model**.

#### Model Download

Download models using huggingface-cli:
``` sh
pip install "huggingface_hub[cli]"
huggingface-cli download Wan-AI/Wan2.2-T2V-A14B --local-dir ./Wan2.2-T2V-A14B
huggingface-cli download lightx2v/Wan2.2-Lightning --local-dir ./Wan2.2-Lightning
```

#### Run Text-to-Video Generation

This repository supports the `Wan2.2-T2V-A14B` Text-to-Video model and can simultaneously support video generation at 480P and 720P resolutions, either portrait or landscape.


##### (1) Without Prompt Extension

To facilitate implementation, we will start with a basic version of the inference process that skips the [prompt extension](#2-using-prompt-extention) step.

- Single-GPU, Single-prompt inference

``` sh
python generate.py  --task t2v-A14B --size "1280*720" --ckpt_dir ./Wan2.2-T2V-A14B --lora_dir ./Wan2.2-Lightning/Wan2.2-T2V-A14B-4steps-lora-rank64-Seko-V1 --offload_model True --base_seed 42 --prompt "Two anthropomorphic cats in comfy boxing gear and bright gloves fight intensely on a spotlighted stage."
```

- Single-GPU, Multiple-prompt inference
``` sh
python generate.py  --task t2v-A14B --size "1280*720" --ckpt_dir ./Wan2.2-T2V-A14B --lora_dir ./Wan2.2-Lightning/Wan2.2-T2V-A14B-4steps-lora-rank64-Seko-V1 --offload_model True --base_seed 42 --prompt_file examples/prompt_list.txt
```

> 💡 This command can run on a GPU with at least 80GB VRAM.

> 💡If you encounter OOM (Out-of-Memory) issues, you can use the `--offload_model True`, `--convert_model_dtype` and `--t5_cpu` options to reduce GPU memory usage.


- Multi-GPU inference using FSDP + DeepSpeed Ulysses

  We use [PyTorch FSDP](https://docs.pytorch.org/docs/stable/fsdp.html) and [DeepSpeed Ulysses](https://arxiv.org/abs/2309.14509) to accelerate inference.


``` sh
torchrun --nproc_per_node=8 generate.py --task t2v-A14B --size "1280*720" --ckpt_dir ./Wan2.2-T2V-A14B --lora_dir ./Wan2.2-Lightning/Wan2.2-T2V-A14B-4steps-lora-rank64-Seko-V1 --dit_fsdp --t5_fsdp --ulysses_size 8 --base_seed 42 --prompt_file examples/prompt_list.txt
```


##### (2) Using Prompt Extension

Extending the prompts can effectively enrich the details in the generated videos, further enhancing the video quality. Therefore, we recommend enabling prompt extension. We provide the following two methods for prompt extension:

- Use the Dashscope API for extension.
  - Apply for a `dashscope.api_key` in advance ([EN](https://www.alibabacloud.com/help/en/model-studio/getting-started/first-api-call-to-qwen) | [CN](https://help.aliyun.com/zh/model-studio/getting-started/first-api-call-to-qwen)).
  - Configure the environment variable `DASH_API_KEY` to specify the Dashscope API key. For users of Alibaba Cloud's international site, you also need to set the environment variable `DASH_API_URL` to 'https://dashscope-intl.aliyuncs.com/api/v1'. For more detailed instructions, please refer to the [dashscope document](https://www.alibabacloud.com/help/en/model-studio/developer-reference/use-qwen-by-calling-api?spm=a2c63.p38356.0.i1).
  - Use the `qwen-plus` model for text-to-video tasks and `qwen-vl-max` for image-to-video tasks.
  - You can modify the model used for extension with the parameter `--prompt_extend_model`. For example:
```sh
DASH_API_KEY=your_key torchrun --nproc_per_node=8 generate.py  --task t2v-A14B --size 1280*720 --ckpt_dir ./Wan2.2-T2V-A14B --lora_dir ./Wan2.2-Lightning/Wan2.2-T2V-A14B-4steps-lora-rank64-Seko-V1 --dit_fsdp --t5_fsdp --ulysses_size 8 --prompt "Two anthropomorphic cats in comfy boxing gear and bright gloves fight intensely on a spotlighted stage" --use_prompt_extend --prompt_extend_method 'dashscope' --prompt_extend_target_lang 'zh'
```

- Using a local model for extension.

  - By default, the Qwen model on HuggingFace is used for this extension. Users can choose Qwen models or other models based on the available GPU memory size.
  - For text-to-video tasks, you can use models like `Qwen/Qwen2.5-14B-Instruct`, `Qwen/Qwen2.5-7B-Instruct` and `Qwen/Qwen2.5-3B-Instruct`.
  - For image-to-video tasks, you can use models like `Qwen/Qwen2.5-VL-7B-Instruct` and `Qwen/Qwen2.5-VL-3B-Instruct`.
  - Larger models generally provide better extension results but require more GPU memory.
  - You can modify the model used for extension with the parameter `--prompt_extend_model` , allowing you to specify either a local model path or a Hugging Face model. For example:

``` sh
torchrun --nproc_per_node=8 generate.py  --task t2v-A14B --size 1280*720 --ckpt_dir ./Wan2.2-T2V-A14B --lora_dir ./Wan2.2-Lightning/Wan2.2-T2V-A14B-4steps-lora-rank64-Seko-V1 --dit_fsdp --t5_fsdp --ulysses_size 8 --prompt "Two anthropomorphic cats in comfy boxing gear and bright gloves fight intensely on a spotlighted stage" --use_prompt_extend --prompt_extend_method 'local_qwen' --prompt_extend_target_lang 'zh'
```


#### Run Image-to-Video Generation

This repository supports the `Wan2.2-I2V-A14B` Image-to-Video model and can simultaneously support video generation at 480P and 720P resolutions.


- Single-GPU inference
```sh
python generate.py  --task i2v-A14B  --size "1280*720" --ckpt_dir ./Wan2.2-I2V-A14B --lora_dir ./Wan2.2-Lightning/Wan2.2-I2V-A14B-4steps-lora-rank64-Seko-V1 --offload_model True --base_seed 42 --prompt_file examples/i2v_prompt_list.txt --image_path_file examples/i2v_image_path_list.txt
```

> This command can run on a GPU with at least 80GB VRAM.

> 💡For the Image-to-Video task, the `size` parameter represents the area of the generated video, with the aspect ratio following that of the original input image.


- Multi-GPU inference using FSDP + DeepSpeed Ulysses

```sh
torchrun --nproc_per_node=8 generate.py --task i2v-A14B --size 1280*720 --ckpt_dir ./Wan2.2-I2V-A14B --lora_dir ./Wan2.2-Lightning/Wan2.2-I2V-A14B-4steps-lora-rank64-Seko-V1 --dit_fsdp --t5_fsdp --ulysses_size 8 --base_seed 42 --prompt_file examples/i2v_prompt_list.txt --image_path_file examples/i2v_image_path_list.txt
```

<!-- 
- Image-to-Video Generation without prompt

```sh
DASH_API_KEY=your_key torchrun --nproc_per_node=8 generate.py --task i2v-A14B --size 1280*720 --ckpt_dir ./Wan2.2-I2V-A14B --prompt '' --image examples/i2v_input.JPG --dit_fsdp --t5_fsdp --ulysses_size 8 --use_prompt_extend --prompt_extend_method 'dashscope'
```

> 💡The model can generate videos solely from the input image. You can use prompt extension to generate prompt from the image.

> The process of prompt extension can be referenced [here](#2-using-prompt-extention).

#### Run Text-Image-to-Video Generation

This repository supports the `Wan2.2-TI2V-5B` Text-Image-to-Video model and can support video generation at 720P resolutions.


- Single-GPU Text-to-Video inference
```sh
python generate.py --task ti2v-5B --size 1280*704 --ckpt_dir ./Wan2.2-TI2V-5B --offload_model True --convert_model_dtype --t5_cpu --prompt "Two anthropomorphic cats in comfy boxing gear and bright gloves fight intensely on a spotlighted stage"
```

> 💡Unlike other tasks, the 720P resolution of the Text-Image-to-Video task is `1280*704` or `704*1280`.

> This command can run on a GPU with at least 24GB VRAM (e.g, RTX 4090 GPU).

> 💡If you are running on a GPU with at least 80GB VRAM, you can remove the `--offload_model True`, `--convert_model_dtype` and `--t5_cpu` options to speed up execution.


- Single-GPU Image-to-Video inference
```sh
python generate.py --task ti2v-5B --size 1280*704 --ckpt_dir ./Wan2.2-TI2V-5B --offload_model True --convert_model_dtype --t5_cpu --image examples/i2v_input.JPG --prompt "Summer beach vacation style, a white cat wearing sunglasses sits on a surfboard. The fluffy-furred feline gazes directly at the camera with a relaxed expression. Blurred beach scenery forms the background featuring crystal-clear waters, distant green hills, and a blue sky dotted with white clouds. The cat assumes a naturally relaxed posture, as if savoring the sea breeze and warm sunlight. A close-up shot highlights the feline's intricate details and the refreshing atmosphere of the seaside."
```

> 💡If the image parameter is configured, it is an Image-to-Video generation; otherwise, it defaults to a Text-to-Video generation.

> 💡Similar to Image-to-Video, the `size` parameter represents the area of the generated video, with the aspect ratio following that of the original input image.


- Multi-GPU inference using FSDP + DeepSpeed Ulysses

```sh
torchrun --nproc_per_node=8 generate.py --task ti2v-5B --size 1280*704 --ckpt_dir ./Wan2.2-TI2V-5B --dit_fsdp --t5_fsdp --ulysses_size 8 --image examples/i2v_input.JPG --prompt "Summer beach vacation style, a white cat wearing sunglasses sits on a surfboard. The fluffy-furred feline gazes directly at the camera with a relaxed expression. Blurred beach scenery forms the background featuring crystal-clear waters, distant green hills, and a blue sky dotted with white clouds. The cat assumes a naturally relaxed posture, as if savoring the sea breeze and warm sunlight. A close-up shot highlights the feline's intricate details and the refreshing atmosphere of the seaside."
```

> The process of prompt extension can be referenced [here](#2-using-prompt-extension). 
-->



## License Agreement
The models in this repository are licensed under the Apache 2.0 License. We claim no rights over the your generated contents, granting you the freedom to use them while ensuring that your usage complies with the provisions of this license. You are fully accountable for your use of the models, which must not involve sharing any content that violates applicable laws, causes harm to individuals or groups, disseminates personal information intended for harm, spreads misinformation, or targets vulnerable populations. For a complete list of restrictions and details regarding your rights, please refer to the full text of the [license](LICENSE.txt).


## Acknowledgements

We built upon and reused code from the following projects: [Wan2.1](https://github.com/Wan-Video/Wan2.1), [Wan2.2](https://github.com/Wan-Video/Wan2.2), licensed under the Apache License 2.0. 

We also adopt the evaluation text prompts from [Movie Gen Bench](https://github.com/facebookresearch/MovieGenBench), which is licensed under the Creative Commons Attribution-NonCommercial 4.0 (CC BY-NC 4.0) License. The original license can be found [here](https://github.com/facebookresearch/MovieGenBench/blob/main/LICENSE).

The selected prompts are further enhanced using the `Qwen/Qwen2.5-14B-Instruct`model [Qwen](https://huggingface.co/Qwen).

