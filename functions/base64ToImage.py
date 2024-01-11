import base64
from datetime import datetime
from io import BytesIO
from PIL import Image


def base64ToImage(imageString):
    image_data = base64.b64decode(imageString.split(',')[1])
    image = Image.open(BytesIO(image_data))

    now = datetime.now()
    timestamp = int(now.timestamp() * 1000)
    fileName = f"./images/image{timestamp}.png"

    image.save(fileName)

    return fileName
