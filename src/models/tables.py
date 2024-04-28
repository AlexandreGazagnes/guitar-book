import os
import logging
import secrets
import datetime

# logging.basicConfig(
#     encoding="utf-8",
#     level=logging.INFO,
#     format="%(filename)s:%(module)s:%(funcName)s:%(lineno)d:%(levelname)s:%(message)s",
# )


from typing import List, Optional

import sqlalchemy
import sqlalchemy as db
from sqlalchemy import (
    ForeignKey,
    Table,
    Column,
    Integer,
    String,
    Date,
    Text,
    create_engine,
)

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.orm import DeclarativeBase, declarative_base, sessionmaker
from src.helpers import now

# from src.models.base import Base, N_1, N_2, N_3, N_4

N_1 = 10
N_2 = 50
N_3 = 100
N_4 = 300


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


class Base(DeclarativeBase):
    """
    # # Define the SQLAlchemy base class
    # Base = declarative_base()

    OK
    """

    pass


class Status(Base):
    """Status Model

    OK
    """

    __tablename__ = "_status"

    # raw, cleaned, final
    id_status: Mapped[str] = mapped_column(
        String(N_1), primary_key=True, nullable=False, unique=True
    )
    status: Mapped[str] = mapped_column(String(N_1), nullable=False)

    comments: Mapped[str] = mapped_column(String(N_2), nullable=True)

    def __repr__(self) -> str:
        data = {k: v for k, v in self.__dict__.items() if not k.startswith("_")}
        return str(data)


class DataType(Base):
    """data_type Model

    OK
    """

    #  ["video", "audio", "lyrics", "tab"]
    __tablename__ = "_datatype"

    id_datatype: Mapped[str] = mapped_column(
        String(N_1), primary_key=True, nullable=False, unique=True
    )
    datatype: Mapped[str] = mapped_column(String(N_1), nullable=False)

    comments: Mapped[str] = mapped_column(String(N_2), nullable=True)

    def __repr__(self) -> str:
        data = {k: v for k, v in self.__dict__.items() if not k.startswith("_")}
        return str(data)


class Source(Base):
    """Source Model

    OK"""

    # ultimate boite achanson, youtube, abcthabs, france tabs"
    __tablename__ = "_source"

    id_source: Mapped[str] = mapped_column(
        String(N_2), primary_key=True, nullable=False, unique=True
    )
    source: Mapped[str] = mapped_column(String(N_2), nullable=False)

    base_url: Mapped[str] = mapped_column(String(N_2), nullable=True)
    comments: Mapped[str] = mapped_column(String(N_2), nullable=True)

    def __repr__(self) -> str:
        data = {k: v for k, v in self.__dict__.items() if not k.startswith("_")}
        return str(data)


class Artist(Base):
    """Artist Model

    OK
    """

    __tablename__ = "artist"

    id_artist: Mapped[str] = mapped_column(
        String(N_2), primary_key=True, nullable=False, unique=True
    )
    name: Mapped[str] = mapped_column(String(N_2), nullable=False)
    date_artist: Mapped[str] = mapped_column(
        Date, nullable=False, default=datetime.datetime.now()
    )

    alt_name: Mapped[str] = mapped_column(String(N_2), nullable=True)
    birthdate: Mapped[str] = mapped_column(Date, nullable=True)
    deathdate: Mapped[str] = mapped_column(Date, nullable=True)
    language: Mapped[str] = mapped_column(String(N_1), nullable=True)
    country: Mapped[str] = mapped_column(String(N_1), nullable=True)
    popularity: Mapped[int] = mapped_column(Integer, nullable=True)
    style_1: Mapped[str] = mapped_column(String(N_1), nullable=True)
    style_2: Mapped[str] = mapped_column(String(N_1), nullable=True)
    style_3: Mapped[str] = mapped_column(String(N_1), nullable=True)
    comments: Mapped[str] = mapped_column(String(N_2), nullable=True)

    def __repr__(self) -> str:
        data = {k: v for k, v in self.__dict__.items() if not k.startswith("_")}
        return str(data)


class Song(Base):
    """Song Model

    OK
    """

    __tablename__ = "song"

    id_song: Mapped[str] = mapped_column(
        String(N_2), primary_key=True, nullable=False, unique=True
    )
    title: Mapped[str] = mapped_column(String(N_2), nullable=False)
    date_song: Mapped[str] = mapped_column(
        Date, nullable=False, default=datetime.datetime.now()
    )

    alt_title: Mapped[str] = mapped_column(String(N_2), nullable=True)
    # lyrics: Mapped[str] = mapped_column(Text)
    comments: Mapped[str] = mapped_column(String(N_2), nullable=True)

    def __repr__(self) -> str:
        data = {k: v for k, v in self.__dict__.items() if not k.startswith("_")}
        return str(data)


class Version(Base):
    """Version Model"""

    __tablename__ = "version"

    id_version: Mapped[str] = mapped_column(
        String(N_3), primary_key=True, nullable=False, unique=True
    )
    id_song: Mapped[str] = mapped_column(
        String(N_2), ForeignKey("song.id_song"), nullable=False
    )
    id_artist: Mapped[str] = mapped_column(
        String(N_2), ForeignKey("artist.id_artist"), nullable=False
    )
    date_version: Mapped[str] = mapped_column(
        Date, nullable=False, default=datetime.datetime.now()
    )

    year: Mapped[int] = mapped_column(Integer, nullable=True)
    album: Mapped[str] = mapped_column(String(N_2), nullable=True)
    style: Mapped[str] = mapped_column(String(N_1), nullable=True)
    popularity: Mapped[int] = mapped_column(Integer, nullable=True)
    intensity: Mapped[int] = mapped_column(Integer, nullable=True)
    mood: Mapped[str] = mapped_column(String(N_1), nullable=True)
    bpm: Mapped[int] = mapped_column(Integer, nullable=True)
    is_original: Mapped[int] = mapped_column(Integer, nullable=True)
    is_live: Mapped[int] = mapped_column(Integer, nullable=True)
    comments: Mapped[str] = mapped_column(String(N_2), nullable=True)

    def __repr__(self) -> str:
        data = {k: v for k, v in self.__dict__.items() if not k.startswith("_")}
        return str(data)


class Submission(Base):
    """Submission Model"""

    __tablename__ = "submission"

    id_submission: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        unique=True,
        autoincrement=True,
    )  # nullable=False, unique=True, autoincrement=True
    id_version: Mapped[str] = mapped_column(
        String(N_3),
        ForeignKey(
            "version.id_version",
        ),  # nullable=False
    )
    date_submission: Mapped[str] = mapped_column(
        Date, nullable=False, default=datetime.datetime.now()
    )
    processed: Mapped[int] = mapped_column(Integer, nullable=False, default=0)

    date_processed: Mapped[str] = mapped_column(Date, nullable=True)
    result: Mapped[str] = mapped_column(String(N_1), nullable=True)

    comments: Mapped[str] = mapped_column(String(N_2), nullable=True)


# class Search(Base):
#     """Search Base"""

#     __tablename__ = "search"

#     id_search: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
#     id_submission: Mapped[int] = mapped_column(
#         Integer, ForeignKey("submission.id_submission"), nullable=False
#     )
#     id_source: Mapped[str] = mapped_column(
#         String(N_2), ForeignKey("_source.id_source"), nullable=False
#     )
#     id_version: Mapped[str] = mapped_column(
#         String(N_3), ForeignKey("version.id_version"), nullable=False
#     )

#     id_datatype: Mapped[str] = mapped_column(
#         String(N_1), ForeignKey("_datatype.id_datatype"), nullable=False
#     )
#     date_search: Mapped[str] = mapped_column(
#         Date, nullable=False, default=datetime.datetime.now()
#     )

#     found: Mapped[int] = mapped_column(Integer, nullable=True)
#     is_alternative_version: Mapped[int] = mapped_column(Integer, nullable=True)
#     query: Mapped[str] = mapped_column(String(N_2), nullable=True)
#     engine: Mapped[str] = mapped_column(String(N_1), nullable=True)
#     _artist: Mapped[str] = mapped_column(String(N_2), nullable=True)
#     _song: Mapped[str] = mapped_column(String(N_2), nullable=True)
#     comments: Mapped[str] = mapped_column(String(N_2), nullable=True)


# class Result(Base):
#     """Results Base"""

#     __tablename__ = "result"

#     id_result: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
#     id_search: Mapped[int] = mapped_column(
#         Integer, ForeignKey("search.id_search"), nullable=False
#     )
#     id_version: Mapped[str] = mapped_column(
#         String(N_3), ForeignKey("version.id_version"), nullable=False
#     )
#     id_datatype: Mapped[str] = mapped_column(String(N_1), nullable=True)
#     id_source: Mapped[str] = mapped_column(
#         String, ForeignKey("source.id_source"), nullable=False
#     )
#     date_result: Mapped[str] = mapped_column(
#         Date, nullable=False, default=datetime.datetime.now()
#     )

#     url: Mapped[str] = mapped_column(String(N_4), nullable=True)
#     # filepath: Mapped[str] = mapped_column(String(N_4), nullable=True)
#     # filename: Mapped[str] = mapped_column(String(N_4), nullable=True)
#     human_validation: Mapped[int] = mapped_column(Integer, nullable=True)
#     retired: Mapped[int] = mapped_column(Integer, nullable=True)
#     comments: Mapped[str] = mapped_column(String(N_2), nullable=True)


# class Tab(Base):
#     """Raw Tab Base"""

#     __tablename__ = "tab"

#     id_tab: Mapped[int] = mapped_column(primary_key=True, nullable=False)
#     id_result: Mapped[int] = mapped_column(
#         Integer, ForeignKey("result.id_result"), nullable=False
#     )
#     id_version: Mapped[str] = mapped_column(
#         String(N_3), ForeignKey("version.id_version"), nullable=False
#     )
#     id_source: Mapped[str] = mapped_column(
#         String(N_1), ForeignKey("source.id_source"), nullable=False
#     )
#     id_status: Mapped[str] = mapped_column(
#         String(N_1), ForeignKey("status.id_status"), nullable=False
#     )
#     date_tab: Mapped[str] = mapped_column(Date, nullable=False, default=datetime.datetime.now())

#     filepath: Mapped[str] = mapped_column(String(N_2), nullable=False)
#     filename: Mapped[str] = mapped_column(String(N_3), nullable=False)

#     # id_source: Mapped[int] = mapped_column(Integer, ForeignKey("source.id_source"))
#     human_validation: Mapped[int] = mapped_column(Integer, nullable=True, default=0)

#     comments: Mapped[str] = mapped_column(String(N_2), nullable=True)


# class AudioRecord(Base):
#     """AudioRecord Base"""

#     __tablename__ = "audiorecord"

#     id_audiorecord: Mapped[int] = mapped_column(primary_key=True, nullable=False)
#     id_result: Mapped[int] = mapped_column(
#         Integer, ForeignKey("result.id_result"), nullable=False
#     )
#     id_version: Mapped[str] = mapped_column(
#         String(N_3), ForeignKey("version.id_version"), nullable=False
#     )
#     id_source: Mapped[str] = mapped_column(
#         String(N_1), ForeignKey("source.id_source"), nullable=False
#     )
#     date_audiorecord: Mapped[str] = mapped_column(
#         Date, nullable=False, default=datetime.datetime.now()
#     )

#     filepath: Mapped[str] = mapped_column(String(N_2), nullable=True)
#     filename: Mapped[str] = mapped_column(String(N_3), nullable=True)

#     # id_source: Mapped[int] = mapped_column(Integer, ForeignKey("source.id_source"))
#     human_validation: Mapped[int] = mapped_column(Integer, nullable=True, default=0)

#     comments: Mapped[str] = mapped_column(String(N_2), nullable=True)


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


def drop_all():
    """Drop all tables"""

    engine = make_engine()
    Base.metadata.drop_all(engine)


def boot_database():
    """ """

    source_data = [
        "boiteachansons",
        "ultimate-guitar",
        "youtube",
        "abctabs",
        "france-tabs",
    ]

    status_data = ["raw", "cleaned", "final"]

    datatype_data = ["video", "audio", "lyrics", "tab"]

    # source
    with create_session() as session:
        for source in source_data:
            s = Source(id_source=source, source=source)
            session.add(s)
            session.commit()

    # status
    with create_session() as session:
        for status in status_data:
            s = Status(id_status=status, status=status)
            session.add(s)
            session.commit()

    # datatype
    with create_session() as session:
        for datatype in datatype_data:
            s = DataType(id_datatype=datatype, datatype=datatype)
            session.add(s)
            session.commit()

    # artist
    artist = "test_artist" + " " + secrets.token_hex(4)
    artist = Artist(id_artist=artist.replace(" ", "_"), name=artist)
    with create_session() as session:
        session.add(artist)
        session.commit()

    # song
    song = "test_song" + " " + secrets.token_hex(4)
    song = Song(id_song=song.replace(" ", "_"), title=song)
    with create_session() as session:
        session.add(song)
        session.commit()

    # version
    with create_session() as session:
        artist = "test_artist" + " " + secrets.token_hex(4)
        artist = Artist(id_artist=artist.replace(" ", "_"), name=artist)

        song = "test_song" + " " + secrets.token_hex(4)
        song = Song(id_song=song.replace(" ", "_"), title=song)

        version = "test_version" + " " + secrets.token_hex(4)
        version = Version(
            id_version=artist.id_artist + "___" + song.id_song + "___",
            id_artist=artist.id_artist,
            id_song=song.id_song,
        )
        session.add(artist)
        session.add(song)
        session.commit()

        session.add(version)
        session.commit()


def reboot_database():
    """ """

    drop_all()
    create_database()
    boot_database()
