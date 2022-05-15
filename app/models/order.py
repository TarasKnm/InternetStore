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
    create_at = Column(TIMESTAMP)   
    ship_address = Column(VARCHAR(100))
    products = relationship('Product', secondary=order_detail)
    