from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import PlainTextResponse

from src.endpoints.auth.auth import routerAuth
from src.endpoints.networks.RouterNetworks import routerNetworks
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

app.include_router(routerAuth, tags=["auth"])

app.include_router(routerNetworks, prefix="/networks", tags=["networks"])
app.include_router(routerNetworkNumbers, prefix="/networkNumbers", tags=["networkNumbers"])
app.include_router(routerNetworkCifar, prefix="/networkCifar", tags=["networkCifar"])
app.include_router(routerNetworkVisDrone, prefix="/networkVisDrone", tags=["networkVisDrone"])

@app.get("/")
def readRoot():
    return {"message": "Hello World"}


@app.get("/.well-known/pki-validation/8104DF13AB2E96B890659D509A2C51CA.txt", response_class=PlainTextResponse)
def letsencrypt_verification():
    verification_file_path = f"./src/.well-known/pki-validation/8104DF13AB2E96B890659D509A2C51CA.txt"

    with open(verification_file_path, "r") as file:
        content = file.read()
        return content


