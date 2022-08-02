import unittest
from musicir.harmony.scale import Scale
from musicir.harmony import get_enharmonic
import music21 as m21


class ScaleTestCase(unittest.TestCase):
    def test_class(self):
        S = Scale('C')
        self.assertIsInstance(S, Scale)

    def test_get_scale_notes2(self):
        S = Scale('E-', mode="Harmonic Minor")
        notes = S.get_notes()
        answer = ["E-", "F", "G-", "A-", "B-", "C-", "D"]
        for i, n in enumerate(notes[:len(answer)]):
            self.assertIn(n, [answer[i], get_enharmonic(answer[i]).upper()])

    def test_stream(self):
        s = Scale('F', acc='#', mode='RagAsawari')
        st = s.stream
        self.assertIsInstance(st, m21.stream.Stream)


if __name__ == '__main__':
    unittest.main()
