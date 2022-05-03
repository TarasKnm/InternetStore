from sqlalchemy import Column, Integer, ForeignKey, VARCHAR, DateTime, Boolean

from ..db_setup import Base
from .store import Store
from .order import Order

class GoodStatus(Base):
    __tablename__ = "good_statuses"

    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(45))


class Good(Base):
    __tablename__ = "goods"

    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(45))
    is_available = Column(Boolean)
    photo_URL = Column(VARCHAR(45))
    store_id = Column(Integer, ForeignKey(Store.id))
    good_status_id = Column(Integer, ForeignKey(GoodStatus.id,ondelete="CASCADE"))
    order_id = Column(Integer, ForeignKey(Order.id))