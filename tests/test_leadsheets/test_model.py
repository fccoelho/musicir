import unittest
from musicir.leadsheets.model import Song, Musician, Harmony
from musicir.leadsheets.musicxml import ChordParser
from musicir.leadsheets.musicxml import HarmonyParser

class MyTestCase(unittest.TestCase):
    def test_song_repr(self):
        HP = HarmonyParser("tests/test_leadsheets/fixtures/Ambidextrous.xml")
        harm = [Harmony(measures=HP.number_of_measures, chords=HP.as_json())]
        mus = Musician(name='myself')
        sng = Song(
            title='test title',
            composer=mus,
            copyright='me',
            harmony=harm,
        )
        self.assertIsInstance(sng.__repr__(), str)
        self.assertIsInstance(harm.__repr__(), str)
        self.assertIsInstance(mus.__repr__(), str)


if __name__ == '__main__':
    unittest.main()
