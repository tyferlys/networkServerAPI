import base64
from io import BytesIO

import PIL
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import PlainTextResponse

from src.functions.base64ToImage import base64ToImage
from src.types.ImageBase64 import ImageBase64
from src.types.NetworkData import NetworkData
from src.networks.models.cifar.networkCifar import predictCifar
from src.networks.models.numbers.networkNumbers import predictNumbers
from src.networks.models.visDrone.networkVisDrone import predictVisDrone

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


@app.get("/networkNumbers")
def data_numbers() -> NetworkData:
    title = "Распознавание чисел"
    description = "Данная нейронная сеть способна распознать цифры на изображении, чтобы ею воспользоваться, вы можете нарисовать на черном холсте любые цирфы."
    link = "digits"
    badges = ["Тестовая"]

    return NetworkData(
        title=title,
        description=description,
        link=link,
        badges=badges
    )


@app.get("/networkCifar")
def data_numbers() -> NetworkData:
    title = "Cifar: Распознавание предметов"
    description = "Данная нейронная сеть способна распознать предмет на изображении, чтобы ею воспользоваться, вы можете загрузить любое изображение и отправить его"
    link = "cifar"
    badges = ["Тестовая"]

    return NetworkData(
        title=title,
        description=description,
        link=link,
        badges=badges
    )


@app.get("/networkVisDrone")
def data_numbers() -> NetworkData:
    title = "VisDrone: Распознавание предметов"
    description = "Данная нейронная сеть способна распознать предметы на изображении с видом сверху, чтобы ею воспользоваться, вы можете загрузить любое изображение и отправить его"
    link = "drone"
    badges = ["Тестовая"]

    return NetworkData(
        title=title,
        description=description,
        link=link,
        badges=badges
    )


@app.post("/networkNumbers")
def predict_numbers(imageData: ImageBase64):
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
def predict_cifar(imageData: ImageBase64):
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


@app.post("/networkVisDrone")
def predict_visDrone(imageData: ImageBase64):
    fileName = base64ToImage(imageData.image)
    numbersData = predictVisDrone(fileName)

    image = PIL.Image.open(numbersData["image"])

    img_byte_array = BytesIO()
    image.save(img_byte_array, format=image.format)
    base64_image = base64.b64encode(img_byte_array.getvalue()).decode('utf-8')

    return {"result": {
        "answer": numbersData["array"],
        "image": base64_image
    }}


# ДЛЯ SSL КЛЮЧА

@app.get("src/.well-known/pki-validation/8104DF13AB2E96B890659D509A2C51CA.txt", response_class=PlainTextResponse)
def letsencrypt_verification():
    verification_file_path = f"src/.well-known/pki-validation/8104DF13AB2E96B890659D509A2C51CA.txt"

    with open(verification_file_path, "r") as file:
        content = file.read()
        return content


