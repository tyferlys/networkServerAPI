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
    tags: List[TagBase]


class NetworksDataResponse(NetworkBase):
    class Config:
        orm_mode = True