from typing import Optional

from pydantic import BaseModel, EmailStr


# Shared properties
class UserBase(BaseModel):
    email: Optional[EmailStr] = None
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    username: Optional[str] = None
    phone: Optional[str] = None


# Properties to receive via API on creation
class UserCreate(UserBase):
    is_superuser: bool = False
    password: str
    email: EmailStr
    


# Properties to receive via API on update
class UserUpdate(UserBase):
    pass
class UserInDBBase(UserBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class User(UserInDBBase):
    pass


# Additional properties stored in DB
class UserInDB(UserInDBBase):
    hashed_password: str