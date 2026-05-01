# https://docs.python.org/3/library/base64.html

from base64 import b64encode, b64decode
from io import BytesIO
from PIL import Image



#this will be useful at the beggining

def base64_to_image(base64_string: str):
    """
    decodifica y devuelve la imagen original.
    """
    image_bytes = b64decode(base64_string)
    return Image.open(BytesIO(image_bytes)).convert("RGB")

def base64_to_image_resized(base64_string: str, size=(224, 224)):
    """
    decodifica y devuelve la imagen ajustada a un tamaño estándar.
    """

    from base64 import b64decode
    from io import BytesIO
    from PIL import Image
    image_bytes = b64decode(base64_string)
    image = Image.open(BytesIO(image_bytes)).convert("RGB")
    image = image.resize(size)
    return image