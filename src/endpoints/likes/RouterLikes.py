from fastapi import APIRouter

import PIL
from fastapi import APIRouter, HTTPException

from src.database.operations.operationsUsers import createLike
from src.types.UsersResponses import UsersCreateResponse


routerLikes = APIRouter()


@routerLikes.post("/{idUser}/{idNetwork}")
def create_like(idUser: int, idNetwork: int) -> UsersCreateResponse:
    try:
        result = createLike(idUser, idNetwork)

        return UsersCreateResponse(result=result)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"ошибка при создании")
