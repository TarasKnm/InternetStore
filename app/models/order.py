from sqlalchemy import  Column, Integer, ForeignKey, VARCHAR,TIMESTAMP,Table
from sqlalchemy.orm import relationship

from ..db.base_class import Base
order_detail = Table('order_details', Base.metadata,
                     Column('order_id',ForeignKey('orders.id')),
                     Column('product_id',ForeignKey('products.id'))
                     )

class Order(Base):
    __tablename__ = 'orders'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    created_at = Column(TIMESTAMP)
    city = Column(VARCHAR(45))
    zip = Column(VARCHAR(45))
    address = Column(VARCHAR(45))
    status = Column(VARCHAR(45))
    products = relationship('Product', secondary=order_detail)
    user = relationship('User')
    