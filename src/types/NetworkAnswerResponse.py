from typing import List

from pydantic import BaseModel


class NetworkAnswerResponse(BaseModel):
    answer: List[str]
    image: str