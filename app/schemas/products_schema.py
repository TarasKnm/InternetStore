from decimal import Decimal
from typing import Optional

from pydantic import BaseModel
from app.schemas.base_schema import SchemaBase
class ProductsBase(SchemaBase):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[Decimal] = None
    quantity: Optional[int] = None
    
class ProductsInDb(ProductsBase):
    id: Optional[int] = None
    
class ProductUpdate(ProductsBase):
    pass