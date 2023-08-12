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


class Base(DeclarativeBase):
    """
    # # Define the SQLAlchemy base class
    # Base = declarative_base()
    """

    pass
