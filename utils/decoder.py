# https://docs.python.org/3/library/base64.html

from base64 import b64encode, b64decode
from io import BytesIO
from PIL import Image

#this will be useful at the beggining
def base64_to_image(base64_string: str):
    """
    Decof a Base64 string back to an image file.
    
    """
    image_bytes = b64decode(base64_string)
    return Image.open(BytesIO(image_bytes)).convert("RGB")
