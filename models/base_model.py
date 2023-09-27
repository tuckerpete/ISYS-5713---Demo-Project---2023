# See SqlAlchmey ORM Quick Start: https://docs.sqlalchemy.org/en/20/orm/quickstart.html

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import create_engine

class Base(DeclarativeBase):
    pass

engine = None

def create_database():

    # create an engine
    global engine
    engine = create_engine("sqlite:///models/cache.sqlite", echo=True)

    Base.metadata.create_all(engine)

