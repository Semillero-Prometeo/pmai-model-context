import torch

DEVICE = "cpu"


def generate_context(pil_image, processor, model):
    """
    """

    prompt = "a photo of"
    
    gen_kwargs = dict(
        max_length=100,
        min_length=20,        # menos presión = menos alucinación
        num_beams=5,         # menos beams = más rápido y más conservador
        repetition_penalty=1.25,  # penaliza repetir palabras, respuestas más variadas
        early_stopping=True,
        length_penalty=1.0,  # penaliza longitud, respuestas más cortas y precisas
        no_repeat_ngram_size=2,
        use_cache=True,
        
    )

    # gen_kwargs = dict(
    #     max_length=55,
    #     min_length=12,
    #     num_beams=3,
    #     repetition_penalty=1.2,
    #     early_stopping=True,
    #     length_penalty=1.0,
    #     no_repeat_ngram_size=3,
    #     use_cache=True,
    #     temperature=0.2,
    # )

    inputs = processor(
        images=pil_image,
        text=prompt,
        return_tensors="pt",
        truncation=True,
    ).to(DEVICE)

    with torch.inference_mode():
        output = model.generate(**inputs, **gen_kwargs)

    context = processor.batch_decode(output, skip_special_tokens=True)[0]
    return context, prompt

