import torch
from transformers import AutoProcessor, BlipForConditionalGeneration
from utils.cache import get_cache, update_cache


MODEL_ID = "Salesforce/blip-image-captioning-base"


def import_Blip_model(model_id: str = MODEL_ID):
    """
     Primero asegura que el modelo BLIP se cargue una sola vez y se guarde en caché,
    y luego aplica cuantización dinámica para optimizar rendimiento en CPU, 
     siempre verificando si ya existe una versión lista para usar.
    
    """
    cache = get_cache()
    if cache.get("processor") is not None and cache.get("model") is not None:
        if cache.get("current_model_name") == model_id:
            return cache["processor"], cache["model"]

    try:
        processor = AutoProcessor.from_pretrained(model_id, use_fast=True)
    except ImportError:
        processor = AutoProcessor.from_pretrained(model_id)




    """
    modelo se cargue una sola vez y quede almacenado en caché para reutilización.
    """


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


"""esta función verifica si ya existe una versión cuantizada del modelo BLIP en caché
con los mismos parámetros de cuantización, y si es así, la devuelve directamente para uso.
Si no, toma el modelo BLIP normal, lo convierte en una versión más ligera y rápida para CPU 
mediante cuantización dinámica, y lo deja listo para inferencia. La versión cuantizada se 
guarda en caché para evitar repetir este proceso costoso, y se devuelve lista para usar.
"""

def get_quantized_blip_model(
    model,
    model_name: str = MODEL_ID,
    engine: str = "qnnpack",
    dtype=torch.qint8,
):
    
    """
    esta función verifica si ya existe una versión cuantizada del modelo BLIP en caché
    con los mismos parámetros de cuantización, y si es así, la devuelve directamente para uso
    
    """
    cache = get_cache()
    if (
        cache.get("model_quantized") is not None
        and cache.get("current_model_name") == model_name
        and cache.get("quant_dtype") == str(dtype)
        and cache.get("quant_engine") == engine
    ):
        return cache["model_quantized"]




    """
    Torch
    Es la librería que hace los cálculos matemáticos pesados
    """


    """
    este bloque toma el modelo BLIP normal, 
    lo convierte en una versión más ligera y rápida para
    CPU mediante cuantización dinámica, y lo deja listo para inferencia.
    """


    torch.backends.quantized.engine = engine


    """
    configuración interna de PyTorch que selecciona el motor
    de cuantización. Sin ella, el modelo no sabría 
    cómo ejecutar las operaciones comprimidas en CPU.
    """



    model_quantized = torch.quantization.quantize_dynamic(
        model.cpu(), {torch.nn.Linear}, dtype=dtype
    )
    model_quantized = model_quantized.cpu().eval()


    """
     la versión cuantizada se guarda en caché para evitar repetir este proceso costoso,
     y se devuelve lista para usar.
    """
    update_cache(
        model=model,
        model_name=model_name,
        model_quantized=model_quantized,
        quant_dtype=str(dtype),
        quant_engine=engine,
    )
    return model_quantized
    
    

 