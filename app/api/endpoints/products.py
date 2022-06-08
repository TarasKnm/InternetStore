from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.db_setup import Session, get_db
from app.models.product import Product
from app.models import user
from app.crud import crud_products
from app.schemas import products_schema
from app.api import deps

router = APIRouter()

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
def get_all_products(
    db:Session =  Depends(get_db)):
    products = crud_products.products.get_multi(db=db) 
    return products

@router.put('/{id}')
def update_goods(
    *,
    id=id,
    db:Session=Depends(get_db),
    product_in: products_schema.ProductsBase,
    current_user: user.User = Depends(deps.get_current_active_superuser)
    ):
    product = crud_products.products.get(db=db,id=id)
    
    product = crud_products.products.update(db=db,db_obj=product,obj_in=product_in)

    return product

@router.delete('/{id}')
def delete_goods(
    id=id,
    db:Session = Depends(get_db),
    current_user: user.User=Depends(deps.get_current_active_superuser)):
    product = crud_products.products.remove(db=db,id=id)
    return product