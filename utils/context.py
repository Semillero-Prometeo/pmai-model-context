import time
import torch
from transformers import AutoProcessor, BlipForConditionalGeneration
from utils.decoder import base64_to_image


def generate_context(variablexenbase: str, processor, model) :
    """

    """
    pil_image = base64_to_image(variablexenbase)
    inputs = processor(images=pil_image, return_tensors="pt", truncation=True).to(DEVICE)

    with torch.inference_mode():
        output = model.generate(
            **inputs,
            max_length=40,
            min_length=20,
            num_beams=1,
            repetition_penalty=2.0,
            early_stopping=True
        )
    
    context = processor.batch_decode(output, skip_special_tokens=True)[0]
    return context


