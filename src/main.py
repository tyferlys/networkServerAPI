from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import PlainTextResponse

from src.endpoints.networks.networkCifar.RouterNetworkCifar import routerNetworkCifar
from src.endpoints.networks.networkNumbers.RouterNetworkNumbers import routerNetworkNumbers
from src.endpoints.networks.networkVisDrone.RouterNetworkVisDrone import routerNetworkVisDrone

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routerNetworkNumbers, prefix="/networkNumbers")
app.include_router(routerNetworkCifar, prefix="/networkCifar")
app.include_router(routerNetworkVisDrone, prefix="/networkVisDrone")


@app.get("/")
def readRoot():
    return {"message": "Hello World"}


@app.get(".well-known/pki-validation/8104DF13AB2E96B890659D509A2C51CA.txt", response_class=PlainTextResponse)
def letsencrypt_verification():
    verification_file_path = f".well-known/pki-validation/8104DF13AB2E96B890659D509A2C51CA.txt"

    with open(verification_file_path, "r") as file:
        content = file.read()
        return content


