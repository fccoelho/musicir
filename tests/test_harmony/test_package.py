import unittest  # type: ignore
from musicir.harmony import get_scale_notes

class HarmonyPackageTestCase(unittest.TestCase):
    def test_something(self):
        notes = get_scale_notes('Mixolydian', 'C')
        self.assertEqual(notes, ['C', 'D', 'E', 'F', 'G', 'A', 'A#'])

if __name__ == '__main__':
    unittest.main()
