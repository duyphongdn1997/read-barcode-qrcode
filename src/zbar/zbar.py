from typing import Union

import cv2
import numpy
import numpy as np
from PIL import Image
from pyzbar.pyzbar import decode


class Zbar:
    """
    This is a wrapper class for easier to using method from pyzbar.
    Read one-dimensional barcodes and QR codes from Python 3 using the zbar library.
    """

    def __init__(self):
        pass

    @staticmethod
    def __decode(image: Union[numpy.array, Image.Image]):
        """
        Decode the qrcode/barcode from the image.
        This method accept both PIL.Image and numpy.array.
        >>> decode(Image.open('pyzbar/tests/code128.png'))
        [
            Decoded(
                data=b'Foramenifera', type='CODE128',
                rect=Rect(left=37, top=550, width=324, height=76),
                polygon=[
                    Point(x=37, y=551), Point(x=37, y=625), Point(x=361, y=626),
                    Point(x=361, y=550)
                ],
                orientation="UP",
                quality=77
            )
            Decoded(
                data=b'Rana temporaria', type='CODE128',
                rect=Rect(left=4, top=0, width=390, height=76),
                polygon=[
                    Point(x=4, y=1), Point(x=4, y=75), Point(x=394, y=76),
                    Point(x=394, y=0)
                ],
                orientation="UP",
                quality=77
            )
        ]
        >>> decode(cv2.imread('pyzbar/tests/code128.png'))
        [
            Decoded(
                data=b'Foramenifera', type='CODE128',
                rect=Rect(left=37, top=550, width=324, height=76),
                polygon=[
                    Point(x=37, y=551), Point(x=37, y=625), Point(x=361, y=626),
                    Point(x=361, y=550)
                ],
                orientation="UP",
                quality=77
            )
            Decoded(
                data=b'Rana temporaria', type='CODE128',
                rect=Rect(left=4, top=0, width=390, height=76),
                polygon=[
                    Point(x=4, y=1), Point(x=4, y=75), Point(x=394, y=76),
                    Point(x=394, y=0)
                ],
                orientation="UP",
                quality=77
            )
        ]
        """
        return decode(image)

    def decode(self, img: numpy.array):
        """

        :param img:
        :return:
        """
        codes = self.__decode(img)
        data = []
        for barcode in codes:
            my_data = barcode.data.decode("utf-8")
            data.append(my_data)
            pts = np.array([barcode.polygon], np.int32)
            pts = pts.reshape((-1, 1, 2))
            cv2.polylines(img, [pts], True, (255, 0, 255), 5)
            pts2 = barcode.rect
            cv2.putText(img, my_data, (pts2[0], pts2[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 255), 2)
        return data, img
