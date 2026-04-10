#https://huggingface.co/docs/transformers/main/en/model_doc/blip#transformers.BlipForConditionalGeneration

from transformers import AutoProcessor, BlipForConditionalGeneration
from PIL import Image
from io import BytesIO
import base64
from utils import local_object
from utils.decoder import base64_to_image



DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
MODEL_NAME = "Salesforce/blip-image-captioning-base"



def import_Blip_model ():
    """
    Importa el modelo BLIP y su procesador desde HuggingFace.
    """
    processor = AutoProcessor.from_pretrained(MODEL_NAME)
    model = BlipForConditionalGeneration.from_pretrained(MODEL_NAME).to(DEVICE)
    if DEVICE == "cuda":
        model = model.half()
    return processor, model
    
    
def generate_context(variablexenbase: str, processor, model) :
    """
    Genera contexto a partir de una imagen en base64 usando el modelo y procesador BLIP.
    Falta definir la variable 'prompt' si es necesaria.
    """
    pil_image = base64_to_image(variablexenbase)
    inputs = processor(images=pil_image, return_tensors="pt",truncation=True)
    out = model.generate(
    **inputs,
    max_length=70,
    min_length=40,
    num_beams=5,
    repetition_penalty=1.2
    )
    context = processor.decode(out[0], skip_special_tokens=True)
    return context



def import_x_model():
    """
    Placeholder para importar otro modelo personalizado.
    """
    return ()