from typing import Generator
import secrets

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from pydantic import ValidationError
from sqlalchemy.orm import Session

from app.models import user
from app.crud import crud_user
from app.schemas import token_schema
from app.core import security
from app.db.db_setup import Session, get_db

reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl=f"api/login/access-token"
)

SECRET_KEY = secrets.token_urlsafe(32)

def get_current_user(
    db: Session = Depends(get_db), token: str = Depends(reusable_oauth2)
) -> user.User:
    try:
        payload = jwt.decode(
            token, SECRET_KEY, algorithms=[security.ALGORITHM]
        )
        token_data = token_schema.TokenPayload(**payload)
    except (jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )
    user = crud_user.user.get(db, id=token_data.sub)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


def get_current_active_user(
    current_user: user.User = Depends(get_current_user),
) -> user.User:

    return current_user


def get_current_active_superuser(
    current_user: user.User = Depends(get_current_user),
) -> user.User:
    if not crud_user.user.is_superuser(current_user):
        raise HTTPException(
            status_code=400, detail="The user doesn't have enough privileges"
        )
    return current_user