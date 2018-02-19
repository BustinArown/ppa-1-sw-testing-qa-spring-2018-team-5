import unittest
from shortest_distance import *


class TestShortestDistance(unittest.TestCase):

    def test_distance(self):  # tests that the distance calculation is correct
        self.assertEqual(shortest_distance(4, 3, 6, 5), 2.8284)
        self.assertEqual((shortest_distance(-1, -1, 0, 0)), 1.4142)


if __name__ == '__main__':
    unittest.main()
