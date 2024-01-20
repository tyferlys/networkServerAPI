from typing import List

from pydantic import BaseModel


class NetworkBase(BaseModel):
    id: int
    title: str


class ReviewBase(BaseModel):
    network: NetworkBase
    text: str


class UserBase(BaseModel):
    id: int
    ip_address: str
    username: str
    likes: List[NetworkBase]
    reviews: List[ReviewBase]


class UsersDataResponse(UserBase):
    class Config:
        from_attributes = True