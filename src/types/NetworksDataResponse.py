from typing import List

from pydantic import BaseModel


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


class NetworksDataResponse(NetworkBase):
    class Config:
        from_attributes = True