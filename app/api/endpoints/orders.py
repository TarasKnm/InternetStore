from datetime import datetime
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Any, List
from fastapi.exceptions import HTTPException

from app.db.db_setup import Session, get_db
from app.crud import crud_orders,crud_products
from app.schemas import orders_schema
from app.models import user
from app.api import deps

router = APIRouter()

@router.get('/')
def get_all_orders(db:Session = Depends(get_db)):
    orders = crud_orders.orders.get_multi(db=db)
    return orders

@router.post('/{product_id}',response_model=orders_schema.OrdersBase)
def add_order(*,
            product_id: int,
            db:Session = Depends(get_db),
            order: orders_schema.OrdersCreate,
            current_user: user.User=Depends(deps.get_current_active_user)):
    order.status = "In progress"
    order.user_id = current_user.id
    order.created_at = datetime.now()
    product = crud_products.products.get(db=db,id=product_id)
    if not product.quantity:
        raise HTTPException(status_code=404, detail="Product unavailable")
    order = crud_orders.orders.create(db=db,order_in=order,product=product)
    return order

@router.get('/{user_id}')
def get_orders_for_user(user_id:int, db:Session = Depends(get_db)):
    orders = crud_orders.orders.get_orders_by_user_id(db=db,user_id=user_id)
    return orders

@router.delete('/{id}')
def delete_order_by_id(id, 
                       db:Session = Depends(get_db),
                       current_user: user.User=Depends(deps.get_current_active_user)):
    
    order = crud_orders.orders.remove(db=db,id=id)
    
    return order

@router.put('/{id}')
def update_order(
    *,
    id: int,
    order_in: orders_schema.OrdersUpdate,
    db:Session = Depends(get_db),
    current_user: user.User=Depends(deps.get_current_active_user)
) -> Any: 
    order = crud_orders.orders.get(db=db,id=id)
    
    order = crud_orders.orders.update(db,db_obj=order,obj_in=order_in)
    return order

@router.get('/history/', response_model=List[orders_schema.OrdersGet])
def get_user_orders(
    db: Session=Depends(get_db),
    current_user: user.User=Depends(deps.get_current_user)
):
    
    orders = crud_orders.orders.get_orders_by_user_id(db=db,user_id=current_user.id)
    
    return orders