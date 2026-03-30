# https://docs.python.org/3/library/base64.html

from base64 import b64encode, b64decode
from io import BytesIO
from PIL import Image


def standard_b64encode(s):
    """Encode bytes-like object s using the standard Base64 alphabet.

    The result is returned as a bytes object.
    """
    return b64encode(s)


def standard_b64decode(s):
    """Decode bytes encoded with the standard Base64 alphabet.

    Argument s is a bytes-like object or ASCII string to decode.  The result
    is returned as a bytes object.  A binascii.Error is raised if the input
    is incorrectly padded.  Characters that are not in the standard alphabet
    are discarded prior to the padding check.
    """
    
    return b64decode(s)


#this will be useful at the beggining
def base64_to_image(base64_string: str):
    """
    Decof a Base64 string back to an image file.
    
    """
    image_bytes = standard_b64decode(base64_string)
    return Image.open(BytesIO(image_bytes)).convert("RGB")

