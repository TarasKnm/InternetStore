from sqlalchemy import Column, Integer, ForeignKey, VARCHAR, DateTime, Boolean

from ..db_setup import Base

class UserStatus(Base):
    __tablename__ = "user_statuses"

    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(45))

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(VARCHAR(45))
    firstname = Column(VARCHAR(45))
    lastname = Column(VARCHAR(45))
    email = Column(VARCHAR(45))
    password = Column(VARCHAR(45))
    phone = Column(VARCHAR(45))
    user_status_id = Column(Integer, ForeignKey(UserStatus.id,ondelete="CASCADE"))

    def __str__(self):
        return f"User ID    : {self.id}\n" \
               f"Username      : {self.username}\n" \
               f"Email      : {self.email}\n" \
               f"phone      : {self.phone}\n"
            
