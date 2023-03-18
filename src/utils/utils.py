from base64 import b64decode, b64encode
from typing import Text

import cv2
import numpy as np


def read_encode_image(image_str: Text) -> np.ndarray:
    """
    Get encoded image from base 64 image.
    Args:
        image_str:

    Returns:

    """
    nparr = np.frombuffer(b64decode(image_str), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return img


def encode_base64_image(image: np.ndarray):
    """
    Encode an image to base 64
    Args:
        image:

    Returns:

    """
    _, buffer = cv2.imencode(".jpg", image)
    base64_image = b64encode(buffer).decode("utf-8")
    return base64_image
