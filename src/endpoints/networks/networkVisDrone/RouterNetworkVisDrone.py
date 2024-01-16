import base64
from io import BytesIO

import PIL
from fastapi import APIRouter

from src.functions.base64ToImage import base64ToImage
from src.networks.models.visDrone.networkVisDrone import predictVisDrone
from src.types.ImageBase64Request import ImageBase64Request
from src.types.NetworkAnswerResponse import NetworkAnswerResponse
from src.types.NetworkDataResponse import NetworkDataResponse

routerNetworkVisDrone = APIRouter()


@routerNetworkVisDrone.get("/")
def data_numbers():
    return "test"


@routerNetworkVisDrone.post("/")
def predict_visDrone(imageData: ImageBase64Request) -> NetworkAnswerResponse:
    fileName = base64ToImage(imageData.image)
    numbersData = predictVisDrone(fileName)

    image = PIL.Image.open(numbersData["image"])

    img_byte_array = BytesIO()
    image.save(img_byte_array, format=image.format)
    base64_image = base64.b64encode(img_byte_array.getvalue()).decode('utf-8')

    return NetworkAnswerResponse(answer=numbersData["array"], image=base64_image)

