import unittest

import pytest

from musicir.leadsheets.musicxml import ChordParser
from musicir.leadsheets.musicxml import HarmonyParser, import_into_db


class MyTestCase(unittest.TestCase):
    def test_parse_file(self):
        ls = HarmonyParser("test_leadsheets/fixtures/Ambidextrous.xml")

    def test_ChordParser(self):
        ls = HarmonyParser("test_leadsheets/fixtures/Ambidextrous.xml")
        c = ls.get_measure_chords(1)[0]
        chord = ChordParser(c)
        self.assertIsInstance(chord, ChordParser)

    def test_load_directory(self):
        import_into_db("test_leadsheets/fixtures")


if __name__ == "__main__":
    unittest.main()
