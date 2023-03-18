from pydantic import BaseModel


class Image(BaseModel):
    imageData: str
