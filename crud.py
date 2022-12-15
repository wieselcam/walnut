from sqlalchemy.orm import Session
from datetime import datetime

from . import models, schemas


def get_image(db: Session, image_id: int):
    return db.query(models.Image).filter(models.Image.id == image_id).first()


def get_image_by_date(db: Session, date: datetime):
    return db.query(models.Image).filter(models.Image.date == date).first()


def get_images(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Image).offset(skip).limit(limit).all()


def create_image(db: Session, image: schemas.ImageCreate):
    db_image = models.Image(date=image.date, image=image.image)
    db.add(db_image)
    db.commit()
    db.refresh(db_image)
    return db_image