# https://docs.python.org/3/library/base64.html

from base64 import b64decode
from binascii import Error as Base64Error
from io import BytesIO

from PIL import Image, UnidentifiedImageError



#this will be useful at the beggining

def base64_to_image(base64_string: str):
    """Decodifica una imagen Base64 y la devuelve como RGB."""
    if not isinstance(base64_string, str) or not base64_string.strip():
        raise ValueError("La imagen Base64 debe ser una cadena no vacía.")

    encoded = base64_string.strip()
    if "," in encoded and encoded.startswith("data:"):
        encoded = encoded.split(",", 1)[1]

    try:
        image_bytes = b64decode(encoded, validate=True)
        with Image.open(BytesIO(image_bytes)) as image:
            image.verify()
        with Image.open(BytesIO(image_bytes)) as image:
            return image.convert("RGB")
    except (Base64Error, ValueError, UnidentifiedImageError) as exc:
        raise ValueError("La imagen Base64 no es válida.") from exc

def base64_to_image_resized(base64_string: str, size=(224, 224)):
    """Decodifica una imagen Base64 y la redimensiona."""
    if (
        not isinstance(size, tuple)
        or len(size) != 2
        or not all(isinstance(value, int) and value > 0 for value in size)
    ):
        raise ValueError("size debe ser una tupla de dos enteros positivos.")
    return base64_to_image(base64_string).resize(size)