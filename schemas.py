from pydantic import BaseModel
from datetime import datetime


class ImageBase(BaseModel):
    pass


class ImageCreate(ImageBase):
    image: str


class Image(ImageBase):
    id: int
    date: datetime

    class Config:
        orm_mode = True