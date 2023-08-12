import os

import logging

# logging.basicConfig(
#     encoding="utf-8",
#     level=logging.INFO,
#     format="%(filename)s:%(module)s:%(funcName)s:%(lineno)d:%(levelname)s:%(message)s",
# )


from typing import List
from typing import Optional

import sqlalchemy
import sqlalchemy as db

from sqlalchemy import ForeignKey
from sqlalchemy import Table, Column, Integer, String, Date, Text, create_engine
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import declarative_base

from sqlalchemy.orm import sessionmaker

# from sqlalchemy import  (
#     validate_email,
#     validate_length,
#     validate_range,
#     validate_max_length,
#     validate_min_length,
# )


N_1 = 10
N_2 = 50
N_3 = 100
N_4 = 300


def make_engine(fn: str = "db.sqlite3"):
    """Create an engine to interact with the database"""

    # Create an SQLite database named "db.sqlite3"
    cwd = os.getcwd()
    fn = "db.sqlite3"

    # url = f"{cwd}/{fn}"

    url = os.path.join(cwd, fn)

    # db = os.path.join(cwd, fn)
    database_url = f"sqlite:///{url}"

    engine = create_engine(database_url)
    return engine


def create_database(Base):
    """Create the database"""

    engine = make_engine()
    Base.metadata.create_all(engine)


def create_session():
    """Create a session to interact with the database"""

    engine = make_engine()
    Session = sessionmaker(bind=engine)
    session = Session()
    return session
