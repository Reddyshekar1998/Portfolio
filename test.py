# # Install first:
# # pip install torch torchvision diffusers opencv-python

# from PIL import Image
# from diffusers import StableDiffusionPipeline
# import torch

# # Load Stable Diffusion Pipeline (modify to TryOnDiffusion checkpoint)
# pipe = StableDiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-2-1-base").to("cuda")

# # Load your person image and saree image
# person_image = Image.open("person.jpg").convert("RGB")
# saree_image = Image.open("saree.jpg").convert("RGB")

# # Use ControlNet or modify input embedding to inject cloth conditioning
# prompt = "A realistic photo of the same person wearing the given saree, studio lighting, high detail"

# # Generate the image
# with torch.no_grad():
#     output = pipe(prompt, image=person_image, cloth_image=saree_image, num_inference_steps=30)
#     result_image = output.images[0]

# result_image.save("person_wearing_saree.png")
# result_image.show()

import torch
import os

# os.environ['CUDA_LAUNCH_BLOCKING'] = '1'

print("CUDA Available:", torch.cuda.is_available())
print("CUDA Version:", torch.version.cuda)
print("Device Name:", torch.cuda.get_device_name(0))

a = torch.randn(256, 256, device='cuda')
b = torch.randn(256, 256, device='cuda')
c = torch.matmul(a, b)
print(c)
print("Matrix multiplication completed.")
print("Sum:", c.sum().item())
