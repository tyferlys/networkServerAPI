import base64
from io import BytesIO
from typing import List

import PIL
from fastapi import APIRouter

from src.database.operations.operationsNetworks import getAllNetworks, getNetwork, getReviewForNetwork
from src.networks.models.Hole.NetworkHole import predictHole
from src.networks.models.cifar.networkCifar import predictCifar
from src.networks.models.visDrone.networkVisDrone import predictVisDrone
from src.types.NetworksDataResponse import NetworksDataResponse, NetworksDataResponseWithReviews
from src.functions.base64ToImage import base64ToImage
from src.networks.models.numbers.networkNumbers import predictNumbers
from src.types.ImageBase64Request import ImageBase64Request
from src.types.NetworkAnswerResponse import NetworkAnswerResponse

routerNetworks = APIRouter()


@routerNetworks.get("/")
def data_networks() -> List[NetworksDataResponse]:
    networks = getAllNetworks()

    return networks


@routerNetworks.get("/{idNetwork}")
def data_network(idNetwork: int) -> NetworksDataResponseWithReviews:
    networks = getNetwork(idNetwork)
    reviews = getReviewForNetwork(idNetwork)
    networks.reviews = reviews
    return networks


@routerNetworks.post("/{idNetwork}")
def answer_network(idNetwork: int, imageData: ImageBase64Request) -> NetworkAnswerResponse:
    fileName = base64ToImage(imageData.image)
    numbersData = None

    if idNetwork == 1:
        numbersData = predictNumbers(fileName)
    elif idNetwork == 2:
        numbersData = predictCifar(fileName)
    elif idNetwork == 3:
        numbersData = predictVisDrone(fileName)
    elif idNetwork == 4:
        numbersData = predictHole(fileName)

    image = PIL.Image.open(numbersData["image"])

    img_byte_array = BytesIO()
    image.save(img_byte_array, format=image.format)
    base64_image = base64.b64encode(img_byte_array.getvalue()).decode('utf-8')

    answer = [str(item) for item in numbersData["array"]]

    return NetworkAnswerResponse(answer=answer, image=base64_image)
