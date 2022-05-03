from sqlalchemy import Column, Integer, ForeignKey, VARCHAR, DateTime, Boolean

from ..db.base_class import Base
from .user import User

class OrderStatus(Base):
    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(45))


class Order(Base):
    id = Column(Integer, primary_key=True)
    ship_date = Column(DateTime)
    complete = Column(Boolean)
    order_status_id = Column(Integer, ForeignKey(OrderStatus.id,ondelete="CASCADE"))
    user_id = Column(Integer, ForeignKey(User.id))