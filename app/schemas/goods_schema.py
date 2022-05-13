from pydantic import BaseModel

class GoodsBase(BaseModel):
    id: int
    name: str
    is_available: bool
    photo_URL: str
    store_id: int
    good_status_id: int
    order_id: int