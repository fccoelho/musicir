import unittest

from musicir.rhythm.generate import Euclid, RhythmViewer
from musicir.rhythm import generate
from music21 import stream


class EuclidTestCase(unittest.TestCase):
    def test_create(self):
        E = Euclid(5, 13)
        self.assertEqual([1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0], E.rhythm)
        self.assertEqual("X..X.X..X.X..", str(E))
        self.assertIsInstance(E.get_beat(), stream.Stream)

        E2 = Euclid(3, 8)
        self.assertEqual("X..X..X.", str(E2))

    def test_create_5_8(self):
        E = Euclid(5, 8)
        self.assertEqual([1, 0, 1, 1, 0, 1, 1, 0], E.rhythm)
        self.assertIsInstance(E.get_beat(), stream.Stream)

    def test_create_samba(self):
        E = Euclid(7, 16)
        self.assertEqual([1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0], E.rhythm)
        self.assertIsInstance(E.get_beat(), stream.Stream)

    def test_rhythmviewer(self):
        E = Euclid(7, 16)
        rv = RhythmViewer(E.rhythm)



if __name__ == "__main__":
    unittest.main()
