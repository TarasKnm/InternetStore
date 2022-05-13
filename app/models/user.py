from sqlalchemy import Column, Integer, ForeignKey, VARCHAR, DateTime, Boolean

from ..db.base_class import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    username = Column(VARCHAR(45))
    firstname = Column(VARCHAR(45))
    lastname = Column(VARCHAR(45))
    email = Column(VARCHAR(45))
    password = Column(VARCHAR(45))
    phone = Column(VARCHAR(45))

    def __str__(self):
        return f"User ID    : {self.id}\n" \
               f"Username      : {self.username}\n" \
               f"Email      : {self.email}\n" \
               f"phone      : {self.phone}\n"
            
