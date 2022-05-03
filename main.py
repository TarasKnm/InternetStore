from fastapi import FastAPI

from db.db_setup import engine
from db.models import user, store, good, order

user.Base.metadata.create_all(bind=engine)
store.Base.metadata.create_all(bind=engine)
good.Base.metadata.create_all(bind=engine)
order.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def smth():
    return "hello"