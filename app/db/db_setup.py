from typing import final
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:0510@localhost/InternetStore"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,connect_args={},future=True
)
Session = sessionmaker(
    autocommit=False,autoflush=False,bind=engine,future=True
)

Base = declarative_base()

def get_db():
    db = Session()
    
    try: 
        yield db
    finally:
        db.close()