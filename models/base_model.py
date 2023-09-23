# See SqlAlchmey ORM Quick Start: https://docs.sqlalchemy.org/en/20/orm/quickstart.html

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import create_engine

engine = None

class Base(DeclarativeBase):
    pass

def create_database():

    # Create an engine
    global engine # this means we can now use "engine" from the global context where we defined it above
    engine = create_engine("sqlite:///models/cache.sqlite", echo=True)

    # Build tables
    Base.metadata.create_all(engine)