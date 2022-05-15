from sqlalchemy import Column, Integer, ForeignKey, VARCHAR, DateTime, Boolean

from ..db.base_class import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    username = Column(VARCHAR(45))
    firstname = Column(VARCHAR(45))
    lastname = Column(VARCHAR(45))
    email = Column(VARCHAR(45))
    phone = Column(VARCHAR(45))
    city = Column(VARCHAR(45))
    zip = Column(VARCHAR(45))
    adress = Column(VARCHAR(45))
    city = Column(VARCHAR(45))
