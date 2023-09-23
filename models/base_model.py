# See SqlAlchmey ORM Quick Start: https://docs.sqlalchemy.org/en/20/orm/quickstart.html

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import create_engine

class Base(DeclarativeBase):
    pass
