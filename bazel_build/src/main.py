import os

from diffusers import StableDiffusionPipeline
import fire
import torch

class Runner:
    """Runner """

    @staticmethod
    def run(working_dir):
        prompt_simple = 'check'
        model_id = "runwayml/stable-diffusion-v1-5"
        pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float32)

        prompt = "A white dragon as a business logo vector art with 12 triangles"
        image = pipe(prompt).images[0]  

        output_img_filename = os.path.join(working_dir, f'{prompt_simple}.png')
        image.save(output_img_filename)

if __name__ == '__main__':
  fire.Fire(Runner)