import base64
from io import BytesIO
from typing import List

import PIL
from fastapi import APIRouter, Request, HTTPException

from src.database.operations.operationsUsers import getAllUsers, getUser, createUser, createLike, createReview
from src.types.UsersRequests import createReviewRequest
from src.types.UsersResponses import UsersDataResponse, UsersCreateResponse

routerUsers = APIRouter()


@routerUsers.get("/")
def data_users() -> List[UsersDataResponse]:
    users = getAllUsers()

    return users


@routerUsers.get("/{idUser}")
def data_user(idUser: int) -> UsersDataResponse:
    users = getUser(idUser)

    return users


@routerUsers.post("/{username}")
def create_user(request: Request, username: str) -> UsersCreateResponse:
    try:
        result = createUser(request.client.host, username)

        return UsersCreateResponse(result=result)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"ошибка при создании")
