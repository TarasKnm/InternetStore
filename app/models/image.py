from sqlalchemy import Column, Integer, VARCHAR
from sqlalchemy.orm import relationship

from ..db.base_class import Base

class Image(Base):
    __tablename__ = 'images'
    
    id = Column(Integer,primary_key=True)
    image_path = Column(VARCHAR(100))
    name = Column(VARCHAR(45))