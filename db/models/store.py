from sqlalchemy import Column, Integer, ForeignKey, VARCHAR, DateTime, Boolean

from ..db_setup import Base

class Store(Base):
    __tablename__ = "stores"

    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(45))
    category = Column(VARCHAR(45))