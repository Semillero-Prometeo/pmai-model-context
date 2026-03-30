#https://www.aprendemachinelearning.com/prompt-engineering-para-desarrolladores-python-llm/

## todavia no se implementa el prompt tuning, pero se deja la estructura para cuando se quiera implementar este es un ejemplo de gpt peoro toca adaptarlo

from transformers import pipeline
pipe = pipeline("image-to-text", model="Salesforce/blip-image-captioning-large")



def get_prompt_for_tuning(prompt: str, temperature: float = 0.7, max_length: int = 128):
    """
    Genera una respuesta usando un modelo de Hugging Face con prompt tuning.

    """
    response = generator(
        prompt,
        max_length=max_length,
        temperature=temperature,
        num_return_sequences=1
    )
    
    return response[0]["generated_text"]

