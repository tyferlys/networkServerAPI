from fastapi import FastAPI, HTTPException
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request
from starlette.responses import PlainTextResponse, JSONResponse

from src.database.operations.operationsUsers import checkIP
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

# Middleware для проверки существования ip адреса клиента в базе данных, если ip нет - запрос не проходит дальше.
# Данный middleware действует только на определенных энпоинтах, они находятся в paths

app.include_router(routerNetworks, prefix="/networks", tags=["networks"])
app.include_router(routerUsers, prefix="/users", tags=["users"])
app.include_router(routerLikes, prefix="/likes", tags=["likes"])
app.include_router(routerReviews, prefix="/reviews", tags=["reviews"])


@app.get("/")
def readRoot():
    return {"message": "Hello World"}



#TODO ДОКУМЕНТАЦИЯ
# В приницпе все необходимо сделано, дальше можно рефакторить и документироваться потихоньку + добавлять еще нс, надо еще пнуть рмоу