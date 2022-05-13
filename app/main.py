from fastapi import FastAPI
import uvicorn

from app.db.db_setup import engine
from app.api.api import api_router

# user.Base.metadata.create_all(bind=engine)
# store.Base.metadata.create_all(bind=engine)
# good.Base.metadata.create_all(bind=engine)
# order.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(api_router)

