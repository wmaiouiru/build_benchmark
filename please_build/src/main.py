from diffusers import StableDiffusionPipeline
import os
import fire
import torch

class Runner:
    """Runner """

    @staticmethod
    def run(working_dir):
        prompt_simple = 'check'
        model_id = "runwayml/stable-diffusion-v1-5"
        pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
        pipe = pipe.to("cuda")

        prompt = "a photo of an astronaut riding a horse on mars"
        image = pipe(prompt).images[0]  

        output_img_filename = os.path.join(working_dir, f'{prompt_simple}.png')
        image.save(output_img_filename)

if __name__ == '__main__':
  fire.Fire(Runner)