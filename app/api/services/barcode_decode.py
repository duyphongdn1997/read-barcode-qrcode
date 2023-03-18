"""
Invoice Extraction Service
"""

import numpy as np

from src.utils.utils import encode_base64_image
from src.zbar.zbar import Zbar


class BarcodeDecoder:
    def __init__(self):
        # Init the decoder
        self.zbar = Zbar()

    def decode(self, image: np.ndarray):
        """
        Take an image, processing and return qrcode/barcode information.
        Args:
            image:

        Returns:

        """
        codes, bar_image = self.zbar.decode(image)

        result = {
            "has_code": True if codes else False,
            "codes": codes,
            "bar_image": encode_base64_image(bar_image),
        }
        return result


barcode_decode_service = BarcodeDecoder()
