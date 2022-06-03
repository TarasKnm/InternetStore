from datetime import datetime
from app.schemas.base_schema import SchemaBase

class OrdersBase(SchemaBase):
    user_id: int
    create_at: datetime
    ship_address: str

class OrdersCreate(OrdersBase):
    pass

class OrdersUpdate(OrdersBase):
    pass