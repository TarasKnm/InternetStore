from typing import List
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase 
from app.models.order import Order,order_detail
from app.schemas.orders_schema import OrdersCreate,OrdersUpdate
from fastapi.encoders import jsonable_encoder



class CRUDOrder(CRUDBase[Order,OrdersCreate, OrdersUpdate]):
    def get_orders_by_user_id(
        self, db: Session, user_id:int, skip:int = 0, limit:int=100
    )->List[Order]:
        return (
            db.query(self.model)
            .filter(Order.user_id == user_id)
            .order_by(Order.created_at.desc())
            .offset(skip)
            .limit(limit)
            .all()
        )
    def create(self, db: Session, *, order_in: OrdersCreate,product) -> None:
        order_in_data = jsonable_encoder(order_in)
        db_obj = self.model(**order_in_data) 
        db_obj.products.append(product)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


orders = CRUDOrder(Order)