import unittest

import pytest

from musicir.leadsheets.musicxml import ChordParser
from musicir.leadsheets.musicxml import import_into_db
from musicir.leadsheets.musicxml import NoteParser
from musicir.leadsheets.musicxml import SongParser


class MyTestCase(unittest.TestCase):
    def test_parse_file(self) -> None:
        ls = SongParser("tests/test_leadsheets/fixtures/Ambidextrous.xml")

    def test_ChordParser(self) -> None:
        ls = SongParser("tests/test_leadsheets/fixtures/Ambidextrous.xml")
        self.assertIsInstance(ls.measures, list)
        c = ls.get_measure_chords(1)[0]
        chord = ChordParser(c)
        self.assertIsInstance(chord, ChordParser)
        self.assertIsInstance(chord.root, str)
        self.assertIsInstance(chord.kind, str)
        self.assertIsInstance(chord.function, str)

    def test_Chord_repr(self) -> None:
        ls = SongParser("tests/test_leadsheets/fixtures/Ambidextrous.xml")
        c = ls.get_measure_chords(1)[0]
        chord = ChordParser(c)
        self.assertIsInstance(c.__repr__(), str)  # .startswith(chord.root)
        # assert c.__str__().startswith(chord.root)

    def test_get_measures(self):
        ls = SongParser("tests/test_leadsheets/fixtures/Ambidextrous.xml")
        c = ls.get_measure_chords(1)[0]
        # self.assertIsInstance(c, list)

    def test_load_directory(self) -> None:
        import_into_db("tests/test_leadsheets/fixtures")

    def test_get_melody(self) -> None:
        ls = SongParser("tests/test_leadsheets/fixtures/Ambidextrous.xml")
        ns = ls.get_measure_melody(1)
        for n in ns:
            note = NoteParser(n)
            self.assertIsInstance(note.__repr__(), str)
            self.assertIn(note.note, [None, 'C', 'D', 'E', 'F', 'G', 'A', 'B'])


if __name__ == "__main__":
    unittest.main()
