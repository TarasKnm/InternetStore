import os
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.db.db_setup import Session, get_db
from app.crud import crud_images
from app.models import user
from app.api import deps
from app.schemas import image_schema


router = APIRouter()


@router.get('/',response_model=List[image_schema.ImageBaseSchema])
def get_all_images(
    db: Session = Depends(get_db)):
    images = crud_images.images.get_multi(db=db)
    
    return images

@router.post('/{name}',description="Takes only jpg images")
def create_image(
    name,
    db:Session = Depends(get_db),
    current_user: user.User = Depends(deps.get_current_active_superuser)
    ):
    
    obj_in = image_schema.ImageCreate(
        image_path=f"../images/{name}",
        name=name
    )
    
    image = crud_images.images.create(db=db, obj_in=obj_in)