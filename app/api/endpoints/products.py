from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.db_setup import Session, get_db
from app.models.product import Product
from app.crud import crud_products
from app.schemas import products_schema

router = APIRouter()

@router.get('/')
def get_products():
    pass

@router.get('/{id}')
def get_products_by_id(id=id):
    return id

@router.post('/', response_model=products_schema.ProductsBase)
def add_products(*,
              db:Session =  Depends(get_db),
              goods: products_schema.ProductsBase):
    goods = crud_products.goods.create(db=db,obj_in=goods)
    return goods
    
    
@router.put('/{id}')
def update_goods(id=id):
    pass

@router.delete('/{id}')
def delete_goods(id=id):
    pass