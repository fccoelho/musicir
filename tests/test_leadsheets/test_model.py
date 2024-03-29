import unittest

from musicir.leadsheets.model import Harmony
from musicir.leadsheets.model import Musician
from musicir.leadsheets.model import Song
from musicir.leadsheets.musicxml import ChordParser
from musicir.leadsheets.musicxml import SongParser


class MyTestCase(unittest.TestCase):
    def test_song_repr(self):
        HP = SongParser("tests/test_leadsheets/fixtures/Ambidextrous.xml")
        harm = [Harmony(measures=HP.number_of_measures, chords=HP.chords_as_json())]
        mus = Musician(name="myself")
        sng = Song(
            title="test title",
            composer=mus,
            copyright="me",
            harmony=harm,
        )
        self.assertIsInstance(sng.__repr__(), str)
        self.assertIsInstance(harm.__repr__(), str)
        self.assertIsInstance(mus.__repr__(), str)

    def test_chord_parser(self):
        SP = SongParser("tests/test_leadsheets/fixtures/Ambidextrous.xml")
        chords = SP.get_measure_chords(0)
        for chord in chords:
            CP = ChordParser(chord)
            self.assertIsInstance(CP.root, str)
            self.assertIsInstance(CP.kind, str)
            self.assertIsInstance(CP.alteration, str)



if __name__ == "__main__":
    unittest.main()
