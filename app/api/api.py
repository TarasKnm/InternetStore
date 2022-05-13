from fastapi import APIRouter
from app.api.endpoints import goods,users

api_router = APIRouter()

api_router.include_router(goods.router, prefix="/goods",tags=["goods"])
api_router.include_router(users.router,prefix="/users",tags=["users"])