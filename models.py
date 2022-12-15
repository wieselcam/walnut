from sqlalchemy import Column, DateTime, Integer, String

from .database import Base


class Image(Base):
    __tablename__ = "image"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime, index=True)
    image = Column(String)