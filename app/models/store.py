from sqlalchemy import Column, Integer, ForeignKey, VARCHAR, DateTime, Boolean

from ..db.base_class import Base

class Store(Base):
    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(45))
    category = Column(VARCHAR(45))