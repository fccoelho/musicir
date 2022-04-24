import json
import os
from glob import glob
from xml.dom.minidom import parse

from music21 import converter
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from .model import Base
from .model import Harmony
from .model import Musician
from .model import Song


class ChordParser:
    alt_symbols: dict[str, str] = {"-1": "♭", "1": "♯"}

    def __init__(self, element: object):
        self.root = element.getElementsByTagName("root-step")[0].childNodes[0].data
        alterations = element.getElementsByTagName("root-alter")
        self.alteration = (
            "" if not len(alterations) else alterations[0].childNodes[0].data
        )
        self.alteration = self.alt_symbols.get(self.alteration, self.alteration)
        self.kind = element.getElementsByTagName("kind")[0].getAttribute("text")
        self.function = element.getElementsByTagName("kind")[0].childNodes[0].data

    def __repr__(self) -> str:
        return f"{self.root}{self.alteration}{self.kind} - {self.function}"

    def __str__(self) -> str:
        return self.__repr__()


# @define
class HarmonyParser:
    def __init__(self, xmlfile: str):
        """
        Extracts the harmony from musicxml file when available.
        Args:
            xmlfile: path of a musicxml file
        """
        dom = parse(xmlfile)
        self.measures = dom.getElementsByTagName("measure")
        self.number_of_measures = len(self.measures)

    def get_measure_chords(self, measure: int = 0) -> list[object]:
        """
        return a list of Chords as xml elements from a specific measure.
        Args:
            measure: measure number starting at 0

        Returns: List of xml elements

        """
        meas = self.measures[measure]
        chords: list[object] = meas.getElementsByTagName("harmony")
        return chords

    def as_json(self) -> str:
        """
        Return full harmony as a JSON array.
        Returns: JSON string

        """
        hj: list[dict[str, object]] = []
        for m in range(self.number_of_measures):
            h: list[object] = self.get_measure_chords(m)
            hj.append({"measure": m, "chords": [ChordParser(c).__str__() for c in h]})
        return json.dumps(hj)


def import_into_db(path: str) -> None:
    eng = create_engine("sqlite:///leadsheets.sqlite", echo=False, future=True)
    Base.metadata.create_all(eng)
    songs: list[str] = glob(os.path.join(path , "*.xml")) + glob(os.path.join(path, "*.musicxml"))
    with Session(eng) as session:
        objs = []
        for i, song in enumerate(songs):
            print(f"{i+1} of {len(songs)}: {song}loading {song}...\r", end="")
            SO = converter.parse(song)
            HP = HarmonyParser(song)
            sng = Song(
                title=SO.metadata.title,
                composer=Musician(name=SO.metadata.composer),
                copyright=SO.metadata.all()[1][1],
                harmony=[Harmony(measures=HP.number_of_measures, chords=HP.as_json())],
            )
            objs.append(sng)
        session.add_all(objs)
        session.commit()
