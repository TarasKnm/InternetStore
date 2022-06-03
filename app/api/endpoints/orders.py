from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.db_setup import Session, get_db
from app.crud import crud_orders
from app.schemas import orders_schema

router = APIRouter()

@router.get('/')
def get_all_orders(db:Session = Depends(get_db)):
    orders = crud_orders.orders.get_multi(db=db)
    return orders

@router.post('/',response_model=orders_schema.OrdersBase)
def add_order(*,
               db:Session = Depends(get_db),
               orders: orders_schema.OrdersBase):
    
    orders = crud_orders.orders.create(db=db,obj_in=orders)
    return orders

@router.get('/{user_id}')
def get_orders_for_user(user_id:int, db:Session = Depends(get_db)):
    orders = crud_orders.orders.get_orders_by_user_id(db=db,user_id=user_id)
    return orders