import os
from dotenv import load_dotenv

def get_huggingface_apikey():
    """
    Here we will load the HuggingFace APIKEY since the .env file
    """

    load_dotenv()
    return os.getenv("HUGGINGFACEHUB_API_TOKEN")
