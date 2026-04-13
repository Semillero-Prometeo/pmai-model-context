
_MODEL_CACHE = {"processor": None, "model": None, "current_model_name": None}

def get_cache():
    return _MODEL_CACHE


def update_cache(processor, model, model_name):
    global _MODEL_CACHE
    _MODEL_CACHE.update({
        "processor": processor,
        "model": model,
        "current_model_name": model_name
    })


def clear_cache():
    global _MODEL_CACHE
    _MODEL_CACHE = {"processor": None, "model": None, "current_model_name": None}
