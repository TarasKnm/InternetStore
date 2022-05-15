from pydantic import BaseModel

class ProductsBase(BaseModel):
    id: int
    name: str
    price: float