from typing import List

from pydantic import BaseModel


class ReviewBase(BaseModel):
    id_user: int
    text: str


class UserBase(BaseModel):
    id: int
    ip_address: str
    username: str


class TagBase(BaseModel):
    id: int
    title: str


class NetworkBase(BaseModel):
    id: int
    title: str
    description: str
    descriptionResult: str
    image: str
    tags: List[TagBase]
    likes: List[UserBase]


class NetworksDataResponse(NetworkBase):
    class Config:
        from_attributes = True


class NetworksDataResponseWithReviews(NetworkBase):
    reviews: List[ReviewBase]
    class Config:
        from_attributes = True