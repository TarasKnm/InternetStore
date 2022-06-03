from typing import List
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase 
from app.models.order import Order
from app.schemas.orders_schema import OrdersCreate,OrdersUpdate


class CRUDOrder(CRUDBase[Order,OrdersCreate, OrdersUpdate]):
    def get_orders_by_user_id(
        self, db: Session, user_id:int, skip:int = 0, limit:int=100
    )->List[Order]:
        return (
            db.query(self.model)
            .filter(Order.user_id == user_id)
            .offset(skip)
            .limit(limit)
            .all()
        )

orders = CRUDOrder(Order)