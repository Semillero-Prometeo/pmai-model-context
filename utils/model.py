#https://huggingface.co/docs/transformers/main/en/model_doc/blip#transformers.BlipForConditionalGeneration

from transformers import AutoProcessor, BlipForConditionalGeneration
from PIL import Image
from io import BytesIO
import base64
from utils import local_object
from utils.decoder import base64_to_image


def import_Blip_model ():
    """
    Importa el modelo BLIP y su procesador desde HuggingFace.
    """
    processor = AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
    return processor, model
    
    
def generate_context(variablexenbase: str, processor, model) :
    """
    Genera contexto a partir de una imagen en base64 usando el modelo y procesador BLIP.
    Falta definir la variable 'prompt' si es necesaria.
    """
    pil_image = base64_to_image(variablexenbase)
    # prompt = "Describe la imagen"  # Descomentar y personalizar si se requiere un prompt
    inputs = processor(images=pil_image, return_tensors="pt")
    out = model.generate(**inputs, max_length=200, num_beams=20)
    context = processor.decode(out[0], skip_special_tokens=True)
    return context



def import_x_model():
    """
    Placeholder para importar otro modelo personalizado.
    """
    return ()