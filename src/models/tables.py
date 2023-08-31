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


# from src.models.base import Base, N_1, N_2, N_3, N_4

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


# from sqlalchemy import  (
#     validate_email,
#     validate_length,
#     validate_range,
#     validate_max_length,
#     validate_min_length,
# )


# class User(Base):
#     __tablename__ = "user"

#     id = Column(Integer, primary_key=True)
#     username = Column(String(N_2))
#     email = Column(String(N_2))


class Source(Base):
    """Source Model"""

    __tablename__ = "source"

    id_source: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(N_2))
    # possible values : ["boiteachansons", "ultimateguitar", "youtube"]
    base_url: Mapped[str] = mapped_column(String(N_2))
    comments: Mapped[str] = mapped_column(String(N_2))


class Artist(Base):
    """Artist Model"""

    __tablename__ = "artist"

    id_artist: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(N_2))
    alt_name: Mapped[str] = mapped_column(String(N_2))
    date_artist: Mapped[str] = mapped_column(Date)

    birthdate: Mapped[str] = mapped_column(Date)
    deathdate: Mapped[str] = mapped_column(Date)
    language: Mapped[str] = mapped_column(String(N_1))
    country: Mapped[str] = mapped_column(String(N_1))

    popularity: Mapped[int] = mapped_column(Integer)

    style_1: Mapped[str] = mapped_column(String(N_1))
    style_2: Mapped[str] = mapped_column(String(N_1))
    style_3: Mapped[str] = mapped_column(String(N_1))

    comments: Mapped[str] = mapped_column(String(N_2))


class Song(Base):
    """Song Model"""

    __tablename__ = "song"

    id_song: Mapped[str] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(N_2))
    alt_title: Mapped[str] = mapped_column(String(N_2))
    date_song: Mapped[str] = mapped_column(Date)

    # lyrics: Mapped[str] = mapped_column(Text)

    comments: Mapped[str] = mapped_column(String(N_2))

    # def __repr__(self) -> str:
    #     return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"


class Version(Base):
    """Version Model"""

    __tablename__ = "version"

    id_version: Mapped[str] = mapped_column(primary_key=True)
    id_song: Mapped[int] = mapped_column(Integer, ForeignKey("song.id_song"))
    id_artist: Mapped[int] = mapped_column(Integer, ForeignKey("artist.id_artist"))
    date_version: Mapped[str] = mapped_column(Date)

    year: Mapped[int] = mapped_column(Integer)
    album: Mapped[str] = mapped_column(String(N_2))

    style: Mapped[str] = mapped_column(String(N_1))
    popularity: Mapped[int] = mapped_column(Integer)
    intensity: Mapped[int] = mapped_column(Integer)
    mood: Mapped[str] = mapped_column(String(N_1))
    bpm: Mapped[int] = mapped_column(Integer)

    is_original: Mapped[int] = mapped_column(Integer)
    is_live: Mapped[int] = mapped_column(Integer)

    comments: Mapped[str] = mapped_column(String(N_2))


class Submission(Base):
    """Submission Model"""

    __tablename__ = "submission"

    id_submission: Mapped[int] = mapped_column(primary_key=True)
    id_version: Mapped[str] = mapped_column(
        String(N_3), ForeignKey("version.id_version")
    )
    date_submission: Mapped[str] = mapped_column(Date)

    processed: Mapped[int] = mapped_column(Integer)
    date_processed: Mapped[str] = mapped_column(Date)
    result: Mapped[str] = mapped_column(String(N_1))

    comments: Mapped[str] = mapped_column(String(N_2))


class Search(Base):
    """Search Base"""

    __tablename__ = "search"

    id_search: Mapped[int] = mapped_column(primary_key=True)
    id_submission: Mapped[int] = mapped_column(
        Integer, ForeignKey("submission.id_submission")
    )
    date_search: Mapped[str] = mapped_column(Date)

    id_source: Mapped[int] = mapped_column(
        Integer, ForeignKey("source.id_source")
    )  # boiteachansons, ultimateguitar, youtube
    found: Mapped[int] = mapped_column(Integer)
    is_alternative_version: Mapped[int] = mapped_column(Integer)

    query: Mapped[str] = mapped_column(String(N_2))
    engine: Mapped[str] = mapped_column(String(N_1))
    data_type: Mapped[str] = mapped_column(
        String(N_1)
    )  #  ["video", "audio", "lyrics", "tab"]

    _artist: Mapped[str] = mapped_column(String(N_2))
    _song: Mapped[str] = mapped_column(String(N_2))

    # id_version: Mapped[str] = mapped_column(String(N_3), ForeignKey("version.id_version"))

    comments: Mapped[str] = mapped_column(String(N_2))


class Result(Base):
    """Results Base"""

    __tablename__ = "result"

    id_result: Mapped[int] = mapped_column(primary_key=True)
    id_search: Mapped[int] = mapped_column(Integer, ForeignKey("search.id_search"))
    date_result: Mapped[str] = mapped_column(Date)

    url: Mapped[str] = mapped_column(String(N_4))
    filepath: Mapped[str] = mapped_column(String(N_4))
    filename: Mapped[str] = mapped_column(String(N_4))

    human_validation: Mapped[int] = mapped_column(Integer)
    retired: Mapped[int] = mapped_column(Integer)

    data_type: Mapped[str] = mapped_column(
        String(N_1)
    )  #  ["video", "audio", "lyrics", "tab"]

    id_version: Mapped[str] = mapped_column(
        String(N_3), ForeignKey("version.id_version")
    )

    # id_source: Mapped[int] = mapped_column(Integer, ForeignKey("source.id_source"))
    # id_version: Mapped[str] = mapped_column(String(N_3), ForeignKey("version.id_version"))

    comments: Mapped[str] = mapped_column(String(N_2))


class Tab(Base):
    """Raw Tab Base"""

    __tablename__ = "tab"

    id_tab: Mapped[int] = mapped_column(primary_key=True)
    id_result: Mapped[int] = mapped_column(Integer, ForeignKey("result.id_result"))
    date_tab: Mapped[str] = mapped_column(Date)

    tab_type: Mapped[str] = mapped_column(String(N_1))  # raw cleaned final

    filepath: Mapped[str] = mapped_column(String(N_2))
    filename: Mapped[str] = mapped_column(String(N_2))

    website: Mapped[str] = mapped_column(String(N_2))
    id_version: Mapped[str] = mapped_column(
        String(N_3), ForeignKey("version.id_version")
    )
    # id_source: Mapped[int] = mapped_column(Integer, ForeignKey("source.id_source"))
    human_validation: Mapped[int] = mapped_column(Integer)

    comments: Mapped[str] = mapped_column(String(N_2))


class AudioRecord(Base):
    """AudioRecord Base"""

    __tablename__ = "audiorecord"

    id_audiorecord: Mapped[int] = mapped_column(primary_key=True)
    id_result: Mapped[int] = mapped_column(Integer, ForeignKey("result.id_result"))
    date_audiorecord: Mapped[str] = mapped_column(Date)

    filepath: Mapped[str] = mapped_column(String(N_2))
    filename: Mapped[str] = mapped_column(String(N_2))

    id_version: Mapped[str] = mapped_column(
        String(N_3), ForeignKey("version.id_version")
    )
    website: Mapped[str] = mapped_column(String(N_2))

    # id_source: Mapped[int] = mapped_column(Integer, ForeignKey("source.id_source"))
    human_validation: Mapped[int] = mapped_column(Integer)

    comments: Mapped[str] = mapped_column(String(N_2))


def make_engine(fn: str = "db_guitar_book.sqlite3", subfolder: str = "data"):
    """Create an engine to interact with the database"""

    # Create an SQLite database named "db.sqlite3"
    cwd = os.getcwd()
    # fn = "db.sqlite3"

    # url = f"{cwd}/{fn}"

    uri = os.path.join(cwd, subfolder, fn)
    # db = os.path.join(cwd, fn)
    database_uri = f"sqlite:///{uri}"

    engine = create_engine(database_uri)
    return engine


def create_database():
    """Create the database"""

    engine = make_engine()
    Base.metadata.create_all(engine)


def create_session():
    """Create a session to interact with the database"""

    engine = make_engine()
    Session = sessionmaker(bind=engine)
    session = Session()
    return session
