import torch
from app.config import config

pipeImage = config.pipeImage

def generate_image(prompt: str) -> str:
    # Load model
    pipeImage = pipeImage.to("cuda" if torch.cuda.is_available() else "cpu")
    image = pipeImage(
        prompt,
        guidance_scale=0.0,
        num_inference_steps=4,
        max_sequence_length=256,
        generator=torch.Generator("cpu").manual_seed(0)
    ).images[0]
    image.save("flux-schnell.png")
    # Generate image
    image = pipeImage(prompt).images[0]
    # Save image to file
    image_path = f"generated_images/{prompt.replace(' ', '_')}.png"
    image.save(image_path)
    return image_path
