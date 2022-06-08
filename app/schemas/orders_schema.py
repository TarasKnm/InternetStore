from datetime import datetime
from typing import Optional,List
from app.schemas.base_schema import SchemaBase
from app.schemas.products_schema import ProductsBase, ProductsInDb

class OrdersBase(SchemaBase):
    zip: str
    city: str
    address: str
    created_at: Optional[datetime] = None
    status: Optional[str] = None

class OrdersCreate(OrdersBase):
    user_id: Optional[int]=None


class OrdersUpdate(OrdersBase):
    pass
class OrdersGet(OrdersBase):
    id: int
    products: List[ProductsInDb] = None