
_MODEL_CACHE = {
    "processor": None,
    "model": None,
    "model_quantized": None,
    "current_model_name": None,
    "quant_dtype": None,
    "quant_engine": None,
}

_UNCHANGED = object()


"""
    gestor de caché 
    permite reutilizar recursos, optimizar memoria y acelerar 
    inferencia al evitar cargas repetidas y mantener versiones cuantizadas listas para usar.

"""




def get_cache():
    return _MODEL_CACHE


def update_cache(
    processor=_UNCHANGED,
    model=_UNCHANGED,
    model_name=_UNCHANGED,
    model_quantized=_UNCHANGED,
    quant_dtype=_UNCHANGED,
    quant_engine=_UNCHANGED,
):
    global _MODEL_CACHE
    if processor is not _UNCHANGED:
        _MODEL_CACHE["processor"] = processor
    if model is not _UNCHANGED:
        _MODEL_CACHE["model"] = model
    if model_name is not _UNCHANGED:
        _MODEL_CACHE["current_model_name"] = model_name
    if model_quantized is not _UNCHANGED:
        _MODEL_CACHE["model_quantized"] = model_quantized
    if quant_dtype is not _UNCHANGED:
        _MODEL_CACHE["quant_dtype"] = quant_dtype
    if quant_engine is not _UNCHANGED:
        _MODEL_CACHE["quant_engine"] = quant_engine


def clear_cache():
    global _MODEL_CACHE
    _MODEL_CACHE = {
        "processor": None,
        "model": None,
        "model_quantized": None,
        "current_model_name": None,
        "quant_dtype": None,
        "quant_engine": None,
    }
