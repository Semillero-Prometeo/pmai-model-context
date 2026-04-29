import time
import torch
from transformers import AutoProcessor, BlipForConditionalGeneration
from utils.decoder import base64_to_image

DEVICE = "cpu" 

#toca probar mas alternativa de esto 
TEST_OPTIONS = {
    "test1": dict(max_length=52, min_length=10, num_beams=2, repetition_penalty=1.2),
    "test2": dict(max_length=55, min_length=15, num_beams=2, repetition_penalty=1.3, length_penalty=2, no_repeat_ngram_size=2, early_stopping=False),
    "test3": dict(max_length=100, min_length=35, num_beams=5, repetition_penalty=1.2, early_stopping=True),
    "test4": dict(max_length=120, min_length=50, num_beams=3, repetition_penalty=1.4, early_stopping=True, length_penalty=0.9),
    "test5": dict(max_length=150, min_length=60, num_beams=3, repetition_penalty=1.5, early_stopping=True, length_penalty=0.85),
    "test6": dict(max_length=80, min_length=20, num_beams=1, repetition_penalty=2.0, early_stopping=True),
}

def generate_context(variablexenbase, processor, model):
    print("ENTRÉ A LA FUNCIÓN NUEVA5") 
    start = time.time() 
    pil_image = base64_to_image(variablexenbase)
    inputs = processor(images=pil_image, return_tensors="pt", truncation=True).to(DEVICE)
    model = model.to(DEVICE) 

    with torch.inference_mode():
        output = model.generate(
            **inputs,
            max_length=55,
            min_length=15,
            num_beams=3,
            repetition_penalty=1.3,
            length_penalty=0.95,
            no_repeat_ngram_size=2,
            early_stopping=True
        )
    
    context = processor.batch_decode(output, skip_special_tokens=True)[0]
    return context

