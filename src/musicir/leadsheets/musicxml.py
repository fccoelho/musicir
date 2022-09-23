import json
import os
import xml.etree.ElementTree as ET
from glob import glob
from typing import List

from music21 import converter
from numpy import full
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from .model import Base
from .model import Harmony
from .model import Melody
from .model import Musician
from .model import Song


class ChordParser:
    alt_symbols: dict[str, str] = {"-1": "♭", "1": "♯"}

    def __init__(self, element: ET.Element):
        self.root: str = element.find("root").find("root-step").text
        alterations: List[ET.Element] = [el for el in element.iter("root-alter")]
        self.alteration = "" if not len(alterations) else alterations[0].text
        self.alteration = self.alt_symbols.get(self.alteration, self.alteration)
        self.kind = element.find("kind").attrib["text"]
        self.function = element.find("kind").text

    def __repr__(self) -> str:
        return f"{self.root}{self.alteration}{self.kind} - {self.function}"

    def __str__(self) -> str:
        return self.__repr__()


class NoteParser:
    alt_symbols: dict[str, str] = {"-1": "♭", "1": "♯"}

    def __init__(self, element: ET.Element):
        pitch = element.find("pitch")
        if not pitch:
            self.is_rest = True
            ftype = element.find("type")
            if ftype is None:
                self.figure = 'whole'
            else:
                self.figure = ftype.text
            self.duration = element.find("duration").text
            self.voice = element.find("voice").text
            self.note = None
            if element.find('dot'):
                self.dotted = True
            return
        else:
            self.is_rest = False
        self.note = pitch.find("step").text
        self.octave = pitch.find("octave").text
        try:
            self.alter = pitch.find("alter").text
            self.accidental = element.find("accidental").text
        except AttributeError:
            self.alter = ""
            self.accidental = ""
        self.figure = element.find("type").text
        self.duration = element.find("duration").text
        self.voice = element.find("voice").text
        if element.find('dot'):
            self.dotted = len(element.findall('dot'))
        else:
            self.dotted = 0

    def __repr__(self) -> str:
        if self.note:
            return f"{self.note}{self.alt_symbols.get(self.alter, '')}"
        return f"Rest {self.figure}"

    def __str__(self) -> str:
        return self.__repr__()


# @define
class SongParser:
    def __init__(self, xmlfile: str):
        """
        Extracts the harmony from musicxml file when available.
        Args:
            xmlfile: path of a musicxml file
        """
        tree = ET.parse(xmlfile)
        xmlroot = tree.getroot()
        self.measures = [measure for measure in xmlroot.iter("measure")]
        self.number_of_measures = len(self.measures)

    def get_measure_chords(self, measure: int = 0) -> List[object]:
        """
        return a list of Chords as xml elements from a specific measure.
        Args:
            measure: measure number starting at 0

        Returns: List of xml elements

        """
        meas = self.measures[measure]
        chords: List[object] = meas.findall("harmony")
        return chords

    def chords_as_json(self) -> str:
        """
        Return full harmony as a JSON array.
        Returns: JSON string

        """
        hj: List[dict[str, object]] = []
        for m in range(self.number_of_measures):
            h: List[object] = self.get_measure_chords(m)
            hj.append({"measure": m, "chords": [ChordParser(c).__str__() for c in h]})
        return json.dumps(hj)

    def melody_as_json(self) -> str:
        """
        Returns the melody as a JSON string
        Returns: JSON string
        """
        full_melody: List[dict[str, object]] = []
        for m in range(self.number_of_measures):
            notes: List[object] = self.get_measure_melody(m)
            full_melody.append(
                {"measure": m, "notes": [NoteParser(n).__str__() for n in notes]}
            )
        return json.dumps(full_melody)

    def get_measure_melody(self, measure: int = 0) -> List[object]:
        """
        Returns list of notes in the specified measure. Each note is an xml element
        """
        meas = self.measures[measure]
        notes: List[object] = meas.findall("note")
        return notes or []


def import_into_db(path: str) -> None:
    eng = create_engine("sqlite:///leadsheets.sqlite", echo=False, future=True)
    Base.metadata.create_all(eng)
    songs: List[str] = glob(os.path.join(path, "*.xml"), recursive=True) + glob(
        os.path.join(path, "*.musicxml"), recursive=True
    )
    with Session(eng) as session:
        objs = []
        for i, song in enumerate(songs):
            print(f"{i+1} of {len(songs)}: {song}loading {song}...\r", end="")
            SO = converter.parse(song)
            HP = SongParser(song)
            sng = Song(
                title=SO.metadata.title,
                composer=Musician(name=SO.metadata.composer),
                copyright=SO.metadata.all()[1][1],
                harmony=[
                    Harmony(measures=HP.number_of_measures, chords=HP.chords_as_json())
                ],
            )
            objs.append(sng)
        session.add_all(objs)
        session.commit()
