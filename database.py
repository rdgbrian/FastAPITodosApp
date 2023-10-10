from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
#from sqlalchemy.ext.declarative import declarative_base depreciated
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import text
from settings import Settings

SQLALCHEMY_DATABASE_URL = "sqlite:///./todos.db"

settings = Settings()

engine = create_engine(settings.SQLALCHEMY_PGRES_DATABASE_URL)

# MYSQL Series
# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL
# )

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


async def check_db_connected():
    try:
        database = SessionLocal()
        database.execute(text("SELECT 1"))
        print("Database is connected (^_^)")
    except Exception as e:
        print("Looks like there is some problem in connection,see below traceback")
        raise e


async def check_db_disconnected():
    try:
        database = SessionLocal()
        database.close()
        print("Database is Disconnected (-_-) zZZ")
    except Exception as e:
        raise e

