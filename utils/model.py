import torch
from transformers import AutoProcessor, BlipForConditionalGeneration

from utils.cache import get_cache, update_cache


MODEL_ID = "Salesforce/blip-image-captioning-base"


def import_Blip_model(model_id: str = MODEL_ID):
    """
    
    """
    cache = get_cache()
    if cache.get("processor") is not None and cache.get("model") is not None:
        if cache.get("current_model_name") == model_id:
            return cache["processor"], cache["model"]

    try:
        processor = AutoProcessor.from_pretrained(model_id, use_fast=True)
    except ImportError:
        processor = AutoProcessor.from_pretrained(model_id)

    model = BlipForConditionalGeneration.from_pretrained(model_id)
    update_cache(
        processor=processor,
        model=model,
        model_name=model_id,
        model_quantized=None,
        quant_dtype=None,
        quant_engine=None,
    )
    return processor, model


def get_quantized_blip_model(
    model,
    model_name: str = MODEL_ID,
    engine: str = "qnnpack",
    dtype=torch.qint8,
):
    """Return a cached dynamic-quantized BLIP model when config matches."""
    cache = get_cache()
    if (
        cache.get("model_quantized") is not None
        and cache.get("current_model_name") == model_name
        and cache.get("quant_dtype") == str(dtype)
        and cache.get("quant_engine") == engine
    ):
        return cache["model_quantized"]

    torch.backends.quantized.engine = engine
    model_quantized = torch.quantization.quantize_dynamic(
        model.cpu(), {torch.nn.Linear}, dtype=dtype
    )
    model_quantized = model_quantized.cpu().eval()

    update_cache(
        model=model,
        model_name=model_name,
        model_quantized=model_quantized,
        quant_dtype=str(dtype),
        quant_engine=engine,
    )
    return model_quantized
    
    