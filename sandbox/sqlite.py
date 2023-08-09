import os
import sqlalchemy

import sqlalchemy as db


from sqlalchemy.orm import DeclarativeBase


from typing import List
from typing import Optional

from sqlalchemy import ForeignKey
from sqlalchemy import Table, Column, Integer, String, Date, Text
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


class Base(DeclarativeBase):
    pass


from sqlalchemy import create_engine, Column, Integer, String

# from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import sessionmaker

# # Define the SQLAlchemy base class
# Base = declarative_base()


# Define the User class which represents the "user" table
class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    phone = Column(String)


# Create an SQLite database named "db.sqlite3"
cwd = os.getcwd()
fn = "db.sqlite3"

# url = f"{cwd}/{fn}"

url = os.path.join(cwd, fn)

# db = os.path.join(cwd, fn)
database_url = f"sqlite:///{url}"


engine = create_engine(database_url)

# Create the table in the database
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Example: Adding a user to the database
new_user = User(name="John Doe", phone="123-456-7890")
session.add(new_user)
session.commit()

# Example: Querying users from the database
users = session.query(User).all()
for user in users:
    print(f"User ID: {user.id}, Name: {user.name}, Phone: {user.phone}")

# Close the session when done
session.close()


# engine = db.create_engine("sqlite:///my_db.sqlite")
# conn = engine.connect()
