from fastapi import APIRouter
from app.api.endpoints import orders, products,user,login,images

api_router = APIRouter()

api_router.include_router(products.router, prefix="/products",tags=["products"])
api_router.include_router(user.router,prefix="/users",tags=["users"])
api_router.include_router(orders.router,prefix="/orders",tags=["orders"])
api_router.include_router(login.router,prefix="/login",tags=["login"])
api_router.include_router(images.router,prefix="/images", tags=["images"])