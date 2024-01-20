import base64
from io import BytesIO
from typing import List

import PIL
from fastapi import APIRouter

from src.database.operations.operationsUsers import getAllUsers
from src.types.UsersResponses import UsersDataResponse

routerUsers = APIRouter()


@routerUsers.get("/")
def data_users() -> List[UsersDataResponse]:
    users = getAllUsers()

    return users

