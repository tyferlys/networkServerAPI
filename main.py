from fastapi import FastAPI

from functions.base64ToImage import base64ToImage
from models.ImageBase64 import ImageBase64
from networks.models.numbers.networkNumbers import predictNumbers

app = FastAPI()


@app.get("/")
async def readRoot():
    return {"message": "Hello World"}


@app.get("/networkNumbers")
async def read_numbers(imageData: ImageBase64):
    image = base64ToImage(imageData.image)
    numbers = predictNumbers(image)

    return {"result": numbers}




