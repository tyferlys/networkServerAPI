from pydantic import BaseModel


class createReviewRequest(BaseModel):
    id_network: int
    id_user: int
    text: str