from fastapi import APIRouter
from app.api.endpoints import products,users

api_router = APIRouter()

api_router.include_router(products.router, prefix="/goods",tags=["goods"])
api_router.include_router(users.router,prefix="/users",tags=["users"])