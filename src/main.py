from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import PlainTextResponse

from src.endpoints.likes.RouterLikes import routerLikes
from src.endpoints.networks.RouterNetworks import routerNetworks
from src.endpoints.reviews.RouterReviews import routerReviews
from src.endpoints.users.RouterUser import routerUsers

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routerNetworks, prefix="/networks", tags=["networks"])
app.include_router(routerUsers, prefix="/users", tags=["users"])
app.include_router(routerLikes, prefix="/likes", tags=["likes"])
app.include_router(routerReviews, prefix="/reviews", tags=["reviews"])

@app.get("/")
def readRoot():
    return {"message": "Hello World"}


@app.get("/.well-known/pki-validation/8104DF13AB2E96B890659D509A2C51CA.txt", response_class=PlainTextResponse)
def letsencrypt_verification():
    verification_file_path = f"./src/.well-known/pki-validation/8104DF13AB2E96B890659D509A2C51CA.txt"

    with open(verification_file_path, "r") as file:
        content = file.read()
        return content


#TODO ПОДУМАТЬ НАД РАБОЧИМ ПРОСТРАНСТВОМ, ВСЕ ЛИ НОРМ ПО ПАПКАМ РАСПРЕДЕЛНО + ДОКУМЕНТИРУЙ И ТЕСТИРОВАНИЕ