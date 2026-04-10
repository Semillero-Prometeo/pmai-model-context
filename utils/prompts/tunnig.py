
 
#https://www.aprendemachinelearning.com/prompt-engineering-para-desarrolladores-python-llm/

#modelo de tunnign adecuar
from datasets import load_dataset
from transformers import AutoTokenizer, DataCollatorForLanguageModeling


MODEL_NAME_TUNNING = "Qwen/Qwen3-0.6B"

def model_tunning():
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME_TUNNING)
    dataset = load_dataset("karthiksagarn/astro_horoscope", split="train")
    return tokenizer, dataset


def tokenize(batch ,tokenizer):
    return tokenizer(
        batch["horoscope"],
        truncation=True,
        max_length=512,
    )


def preprocess_data():
    dataset = dataset.map(tokenize, batched=True, remove_columns=dataset.column_names)
    dataset = dataset.train_test_split(test_size=0.1)
    return dataset




