from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from functions.base64ToImage import base64ToImage
from models.ImageBase64 import ImageBase64
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
async def readRoot():
    return {"message": "Hello World"}


@app.post("/networkNumbers")
async def read_numbers(imageData: ImageBase64):
    image = base64ToImage(imageData.image)
    numbers = predictNumbers(image)

    return {"result": numbers}




