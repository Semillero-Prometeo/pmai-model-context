from utils.models_config import MODEL
from utils.metrics.rendimiento.cache import get_cache, update_cache
from transformers import AutoProcessor, BlipForConditionalGeneration
import torch

DEVICE = "cpu"

def import_Blip_model(model_size, use_cache=True):
    """
    """
    cache = get_cache()
    model_name = MODEL[model_size]


    if use_cache and cache["model"] is not None and cache["current_model_name"] == model_name:
        print(f" reutilizado el modelo desde el cache (modelo: {model_size})")
        return cache["processor"], cache["model"]


    processor = AutoProcessor.from_pretrained(model_name)
    model = BlipForConditionalGeneration.from_pretrained(model_name).to(DEVICE)
    model.eval()


    update_cache(processor, model, model_name)
    print(f"si se cargo en el cache (modelo: {model_size})")
    return processor, model
