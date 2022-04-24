from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import JSON
from sqlalchemy import String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Song(Base):
    __tablename__ = "song"
    id = Column(Integer, primary_key=True)
    title = Column(String(128))
    copyright = Column(String)
    composer_id = Column(Integer, ForeignKey("musician.id"))
    composer = relationship("Musician", back_populates="songs")
    harmony = relationship("Harmony", back_populates="song")

    def __repr__(self) -> str:
        return f"Song(id={self.id!r}, title={self.title!r}, composer={self.composer!r})"


class Musician(Base):
    __tablename__ = "musician"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    songs = relationship(
        "Song", back_populates="composer", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"Musician(id={self.id!r}, name={self.name!r})"


class Harmony(Base):
    __tablename__ = "harmony"
    id = Column(Integer, primary_key=True)
    measures = Column(Integer)
    chords = Column(JSON)
    song_id = Column(Integer, ForeignKey("song.id"), nullable=False)
    song = relationship("Song", back_populates="harmony")

    def __repr__(self) -> str:
        return f"Harmony(id={self.id!r}), measures={self.measures!r}"
