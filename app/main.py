from fastapi import FastAPI

from db.db_setup import engine
from db.models import user, store, good, order

user.Base.metadata.create_all(bind=engine)
store.Base.metadata.create_all(bind=engine)
good.Base.metadata.create_all(bind=engine)
order.Base.metadata.create_all(bind=engine)


def get_application() -> FastAPI:
    application = FastAPI()

    return application


app = get_application()
