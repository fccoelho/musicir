import unittest

import music21 as m21

from musicir.harmony import get_enharmonic
from musicir.harmony.scale import Scale


class ScaleTestCase(unittest.TestCase):
    def test_class(self):
        S = Scale("C")
        self.assertIsInstance(S, Scale)

    def test_get_scale_notes2(self):
        S = Scale("E-", mode="Harmonic Minor")
        notes = S.get_notes()
        answer = ["E-", "F", "G-", "A-", "B-", "C-", "D"]
        for i, n in enumerate(notes[: len(answer)]):
            self.assertIn(n, [answer[i], get_enharmonic(answer[i]).upper()])

    def test_stream(self):
        s = Scale("F", acc="#", mode="RagAsawari")
        st = s.stream
        self.assertIsInstance(st, m21.stream.Stream)

    def test_as_scale(self):
        S = Scale("E-", mode="Harmonic Minor")
        self.assertIsInstance(S.as_scale(), m21.scale.Scale)


if __name__ == "__main__":
    unittest.main()
