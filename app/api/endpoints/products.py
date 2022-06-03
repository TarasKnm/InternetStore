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
def get_product_by_id(db:Session = Depends(get_db),
                      id=id):
    product = crud_products.products.get(db=db,id=id)
    return product

@router.post('/', response_model=products_schema.ProductsBase)
def add_products(*,
              db:Session =  Depends(get_db),
              products: products_schema.ProductsBase):
    products = crud_products.products.create(db=db,obj_in=products)
    return products
    
@router.get('')
def get_all_products(db:Session =  Depends(get_db)):
    products = crud_products.products.get_multi(db=db) 
    return products
@router.put('/{id}')
def update_goods(id=id):
    pass

@router.delete('/{id}')
def delete_goods(db:Session = Depends(get_db),
                      id=id):
    product = crud_products.products.remove(db=db,id=id)
    return product