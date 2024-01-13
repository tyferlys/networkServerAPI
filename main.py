import base64
from io import BytesIO

import PIL
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from functions.base64ToImage import base64ToImage
from models.ImageBase64 import ImageBase64
from networks.models.cifar.networkCifar import predictCifar
from networks.models.numbers.networkNumbers import predictNumbers

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def readRoot():
    return {"message": "Hello World"}


@app.post("/networkNumbers")
def read_numbers(imageData: ImageBase64):
    fileName = base64ToImage(imageData.image)
    numbersData = predictNumbers(fileName)

    image = PIL.Image.open(numbersData["image"])

    img_byte_array = BytesIO()
    image.save(img_byte_array, format=image.format)
    base64_image = base64.b64encode(img_byte_array.getvalue()).decode('utf-8')

    return {"result": {
        "answer": numbersData["array"],
        "image": base64_image
    }}


@app.post("/networkCifar")
def read_test(imageData: ImageBase64):
    fileName = base64ToImage(imageData.image)
    numbersData = predictCifar(fileName)

    image = PIL.Image.open(numbersData["image"])

    img_byte_array = BytesIO()
    image.save(img_byte_array, format=image.format)
    base64_image = base64.b64encode(img_byte_array.getvalue()).decode('utf-8')

    return {"result": {
        "answer": numbersData["array"],
        "image": base64_image
    }}




