
import pyzbar
from pyzbar.pyzbar import decode
from pyzbar.pyzbar import ZBarSymbol
import numpy
from PIL import Image

class Scanner():
    def __init__(self):
        # do i even need a class?
        pass

    # scan image for QR code
    def scan(self, image):
        # scan image for qr code
        decoded = decode(Image.open(image), symbols=[ZBarSymbol.QRCODE])
        # if decoded is empty, no QR code was detected: don't try to navigate
        if len(decoded) == 0:
            print("No QR code detected")
        else:
            # navigate to link
            link = decoded[0][0]
            print(link)
            #navigate(link)

    # follow QR code
    def navigate(self, link):
        pass

scanner = Scanner()
scanner.scan('madfunny.jpg')
scanner.scan('trollface.jpg')