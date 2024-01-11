import base64
import json
from io import BytesIO
from PIL import Image


def base64ToImage(imageString):
    image_data = base64.b64decode(imageString.split(',')[1])
    image = Image.open(BytesIO(image_data))

    return image
