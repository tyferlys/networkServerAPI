from typing import List

from pydantic import BaseModel


class NetworkData(BaseModel):
    title: str
    description: str
    link: str
    badges: List[str]
