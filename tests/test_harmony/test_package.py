import unittest  # type: ignore

from musicir.harmony import get_scale_notes, get_enharmonic


class HarmonyPackageTestCase(unittest.TestCase):
    def test_get_scale_notes(self):
        notes = get_scale_notes("Mixolydian", "C")
        self.assertEqual(["C", "D", "E", "F", "G", "A", "B-"], notes)

    def test_get_scale_notes2(self):
        notes = get_scale_notes("Harmonic Minor", "E-")
        answer = ["E-", "F", "G-", "A-", "B-", "C-", "D"]
        for i, n in enumerate(notes):
            self.assertIn(n, [answer[i], get_enharmonic(answer[i]).upper()])

    def test_get_enharmonic(self):
        self.assertEqual('c', get_enharmonic('b#'))
        self.assertEqual('b-', get_enharmonic('a#'))


if __name__ == "__main__":
    unittest.main()
