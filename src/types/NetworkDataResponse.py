from typing import List

from pydantic import BaseModel


class NetworkDataResponse(BaseModel):
    title: str
    description: str
    link: str
    badges: List[str]
