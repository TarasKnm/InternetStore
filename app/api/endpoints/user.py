from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic import UrlSchemeError
from pydantic.networks import EmailStr
from sqlalchemy.orm import Session

from app.models import user
from app.schemas import user_schema
from app.crud import crud_user
from app.api import deps
from app.db.db_setup import get_db

router = APIRouter()


@router.get("/", response_model=List[user_schema.User])
def read_users(
    skip: int = 0,
    limit: int = 100,
    db:Session = Depends(get_db),
    current_user: user.User = Depends(deps.get_current_active_superuser),
    ) -> Any:
    """
    Retrieve users.
    """
    users = crud_user.user.get_multi(db, skip=skip, limit=limit)
    return users


@router.post("/", response_model=user_schema.User)
def create_user(
    *,
    db: Session = Depends(get_db),
    user_in: user_schema.UserCreate,
    current_user: user.User = Depends(deps.get_current_active_user))-> Any:
    """
    Create new user.
    """
    user = crud_user.user.get_by_email(db, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system.",
        )
    user = crud_user.user.create(db, obj_in=user_in)
    return user

@router.delete("/", response_model=user_schema.User)
def delete_user_me(
    *,
    db: Session = Depends(get_db),
    current_user: user.User = Depends(deps.get_current_active_user)) -> Any:
    
    user = crud_user.user.delete(db=db,username=current_user.username)
    return user

@router.put("/", response_model=user_schema.User)
def update_user_me(
    *,
    db: Session = Depends(get_db),
    user: user_schema.UserUpdate,
    current_user: user.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update own user.
    """
    current_user_data = jsonable_encoder(current_user)
    user_in = user_schema.UserUpdate(**current_user_data)
    if user.email:
        user_in.email = user.email
    if user.firstname:
        user_in.firstname = user.firstname
    if user.lastname:
        user_in.lastname = user.lastname
    if user.phone:
        user_in.phone = user.phone
    user = crud_user.user.update(db, db_obj=current_user, obj_in=user_in)
    return user


@router.get("/profile", response_model=user_schema.User)
def get_profile(
    db: Session = Depends(get_db),
    current_user: user.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get current user.
    """
    return current_user


@router.post("/register", response_model=user_schema.User)
def create_user_open(
    *,
    db: Session = Depends(deps.get_db),
    password: str = Body(...),
    email: EmailStr = Body(...),
    firstname: str = Body(None),
    lastname: str = Body(None),
    username: str = Body(None),
    phone: str = Body(None)
) -> Any:
    """
    Create new user without the need to be logged in.
    """
    # if not settings.USERS_OPEN_REGISTRATION:
    #     raise HTTPException(
    #         status_code=403,
    #         detail="Open user registration is forbidden on this server",
    #     )
    user = crud_user.user.get_by_username(db, username=username)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system",
        )
    user_in = user_schema.UserCreate(password=password, email=email, firstname=firstname,lastname=lastname,username=username,phone=phone)
    user = crud_user.user.create(db, obj_in=user_in)
    return user


@router.get("/{user_id}", response_model=user_schema.User)
def read_user_by_id(
    user_id: int,
    current_user: user.User = Depends(deps.get_current_active_user),
    db: Session = Depends(get_db),
) -> Any:
    """
    Get a specific user by id.
    """
    user = crud_user.user.get(db, id=user_id)
    if user == current_user:
        return user
    if not crud_user.user.is_superuser(current_user):
        raise HTTPException(
            status_code=400, detail="The user doesn't have enough privileges"
        )
    return user


@router.put("/{user_id}", response_model=user_schema.User)
def update_user(
    *,
    db: Session = Depends(get_db),
    user_id: int,
    user_in: user_schema.UserUpdate,
    current_user: user.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Update a user.
    """
    user = crud_user.user.get(db, id=user_id)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="The user with this username does not exist in the system",
        )
    user = crud_user.user.update(db, db_obj=user, obj_in=user_in)
    return user