import torch

DEVICE = "cpu"


def generate_context(pil_image, processor, model):
    """
    esta funcion toma una imagen, la procesa con BLIP,
    genera un caption optimizado en CPU y lo devuelve como texto limpio
    """

    gen_kwargs = dict(
        max_length=55,
        min_length=15,
        num_beams=1, #3
        repetition_penalty=1.3,   
        early_stopping=False,   
        length_penalty=2.0,    #0.95
        no_repeat_ngram_size=2,   # 
        use_cache=True,
    )


    inputs = processor(images=pil_image, return_tensors="pt", truncation=True).to(DEVICE)

    with torch.inference_mode():
        output = model.generate(**inputs, **gen_kwargs)

    context = processor.batch_decode(output, skip_special_tokens=True)[0]
    return context
