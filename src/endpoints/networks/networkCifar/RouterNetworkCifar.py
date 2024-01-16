import base64
from io import BytesIO

import PIL
from fastapi import APIRouter

from src.functions.base64ToImage import base64ToImage
from src.networks.models.cifar.networkCifar import predictCifar
from src.types.ImageBase64Request import ImageBase64Request
from src.types.NetworkAnswerResponse import NetworkAnswerResponse
from src.types.NetworkDataResponse import NetworkDataResponse

routerNetworkCifar = APIRouter()


@routerNetworkCifar.get("/")
def data_cifar():
    return "test"


@routerNetworkCifar.post("/")
def predict_cifar(imageData: ImageBase64Request) -> NetworkAnswerResponse:
    fileName = base64ToImage(imageData.image)
    numbersData = predictCifar(fileName)

    image = PIL.Image.open(numbersData["image"])

    img_byte_array = BytesIO()
    image.save(img_byte_array, format=image.format)
    base64_image = base64.b64encode(img_byte_array.getvalue()).decode('utf-8')

    answer = [str(item) for item in numbersData["array"]]

    return NetworkAnswerResponse(answer=answer, image=base64_image)
