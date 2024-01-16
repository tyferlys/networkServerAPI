from pydantic import BaseModel


class ImageBase64Request(BaseModel):
    image: str
