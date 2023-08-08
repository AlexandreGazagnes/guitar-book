from typing import List
from typing import Optional

from sqlalchemy import ForeignKey
from sqlalchemy import Table, Column, Integer, String, Date, Text
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Source(Base):
    """Source Model"""

    __tablename__ = "source"

    id_source: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    base_url: Mapped[str] = mapped_column(String(30))

    comments: Mapped[str] = mapped_column(String(300))


class Artist(Base):
    """Artist Model"""

    __tablename__ = "artist"

    id_artist: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    alt_name: Mapped[str] = mapped_column(String(30))
    date_artist: Mapped[str] = mapped_column(Date)

    birthdate: Mapped[str] = mapped_column(Date)
    deathdate: Mapped[str] = mapped_column(Date)
    language: Mapped[str] = mapped_column(String(30))
    country: Mapped[str] = mapped_column(String(30))

    popularity: Mapped[int] = mapped_column(Integer)

    style_1: Mapped[str] = mapped_column(String(30))
    style_2: Mapped[str] = mapped_column(String(30))
    style_3: Mapped[str] = mapped_column(String(30))

    comments: Mapped[str] = mapped_column(String(300))


class Song(Base):
    """Song Model"""

    __tablename__ = "song"

    id_song: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(30))
    alt_title: Mapped[str] = mapped_column(String(30))
    date_song: Mapped[str] = mapped_column(Date)

    lyrics: Mapped[str] = mapped_column(Text)

    comments: Mapped[str] = mapped_column(String(300))

    # def __repr__(self) -> str:
    #     return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"


class Version(Base):
    """Version Model"""

    __tablename__ = "version"

    id_version: Mapped[int] = mapped_column(primary_key=True)
    id_song: Mapped[int] = mapped_column(Integer, ForeignKey("song.id_song"))
    id_artist: Mapped[int] = mapped_column(Integer, ForeignKey("artist.id_artist"))
    date_version: Mapped[str] = mapped_column(Date)

    year: Mapped[int] = mapped_column(Integer)

    #

    style: Mapped[str] = mapped_column(String(30))
    popularity: Mapped[int] = mapped_column(Integer)
    intensity: Mapped[int] = mapped_column(Integer)
    mood: Mapped[str] = mapped_column(String(30))
    bpm: Mapped[int] = mapped_column(Integer)
    is_original: Mapped[int] = mapped_column(Integer)

    comments: Mapped[str] = mapped_column(String(300))


class Submission(Base):
    """Submission Model"""

    __tablename__ = "submission"

    id_submission: Mapped[int] = mapped_column(primary_key=True)
    id_version: Mapped[int] = mapped_column(Integer, ForeignKey("version.id_version"))
    date_submission: Mapped[str] = mapped_column(Date)

    processed = Mapped[int] = mapped_column(Integer)
    date_processed: Mapped[str] = mapped_column(Date)
    result: Mapped[str] = mapped_column(String(30))

    comments: Mapped[str] = mapped_column(String(300))


class Search(Base):
    """Search Base"""

    __tablename__ = "search"

    id_search: Mapped[int] = mapped_column(primary_key=True)
    id_submission: Mapped[int] = mapped_column(
        Integer, ForeignKey("submission.id_submission")
    )
    date_search: Mapped[str] = mapped_column(Date)

    id_source: Mapped[int] = mapped_column(Integer, ForeignKey("source.id_source"))
    found = Mapped[int] = mapped_column(Integer)
    is_alternative_version = Mapped[int] = mapped_column(Integer)

    query = Mapped[str] = mapped_column(String(30))
    engine = Mapped[str] = mapped_column(String(30))

    _artist = Mapped[str] = mapped_column(String(30))
    _song = Mapped[str] = mapped_column(String(30))

    # id_version: Mapped[int] = mapped_column(Integer, ForeignKey("version.id_version"))

    # id_type = ["video", "audio", "lyrics", "tab"]

    comments: Mapped[str] = mapped_column(String(300))


class Results(Base):
    """Results Base"""

    __tablename__ = "results"

    id_results: Mapped[int] = mapped_column(primary_key=True)
    id_search: Mapped[int] = mapped_column(Integer, ForeignKey("search.id_search"))
    date_results: Mapped[str] = mapped_column(Date)

    url: Mapped[str] = mapped_column(String(300))
    retired: Mapped[int] = mapped_column(Integer)

    # id_source: Mapped[int] = mapped_column(Integer, ForeignKey("source.id_source"))
    # id_version: Mapped[int] = mapped_column(Integer, ForeignKey("version.id_version"))

    comments: Mapped[str] = mapped_column(String(300))


class RawTab(Base):
    """Raw Tab Base"""

    __tablename__ = "rawtab"

    id_rawtab: Mapped[int] = mapped_column(primary_key=True)
    id_results: Mapped[int] = mapped_column(Integer, ForeignKey("results.id_results"))
    date_rawtab: Mapped[str] = mapped_column(Date)

    filepath = Mapped[str] = mapped_column(String(30))
    filename = Mapped[str] = mapped_column(String(30))

    # id_version: Mapped[int] = mapped_column(Integer, ForeignKey("version.id_version"))
    # id_source: Mapped[int] = mapped_column(Integer, ForeignKey("source.id_source"))

    comments: Mapped[str] = mapped_column(String(300))
