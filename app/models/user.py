from sqlalchemy import Column, Integer,  VARCHAR, Boolean

from ..db.base_class import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    username = Column(VARCHAR(45))
    firstname = Column(VARCHAR(45))
    lastname = Column(VARCHAR(45))
    email = Column(VARCHAR(45))
    phone = Column(VARCHAR(45))
    hashed_password = Column(VARCHAR(100), nullable=False)
    is_superuser = Column(Boolean(), default=False)
    sex = Column(VARCHAR(45))
