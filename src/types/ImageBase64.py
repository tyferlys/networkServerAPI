from pydantic import BaseModel


class ImageBase64(BaseModel):
    image: str
