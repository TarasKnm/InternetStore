from decimal import Decimal
from app.schemas.base_schema import SchemaBase
class ProductsBase(SchemaBase):
    name: str
    price: Decimal
