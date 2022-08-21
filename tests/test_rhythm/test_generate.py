import unittest
from musicir.rhythm.generate import Euclid

class EuclidTestCase(unittest.TestCase):
    def test_create(self):
        E = Euclid(5,13)
        self.assertEqual([1,0,0,1,0,1,0,0,1,0,1,0,0],E.rhythm)
        self.assertEqual('X..X.X..X.X..', str(E))

        E2 = Euclid(3,8)
        self.assertEqual('X..X..X.', str(E2))


if __name__ == '__main__':
    unittest.main()
