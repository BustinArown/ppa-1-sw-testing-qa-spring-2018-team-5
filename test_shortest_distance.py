import unittest

import shortest_distance

class Test_shortest_distance(unittest.TestCase):


    def test_greater(self):
        self.assertRaises(AssertionError, shortest_distance.enterValues())

    def test_subtract(self):
        self.assertEqual(shortest_distance.subtract(2,3,4,6), (2,3))
        self.assertNotEqual(shortest_distance.subtract(2,1,4,5),(3,2))

    def test_square(self):
        self.assertEqual(shortest_distance.square(3,4,5,6), (4,4))

    def test_add(self):
        self.assertEqual(shortest_distance.add(2,3,4,4),(5))

    def test_distance(self):
        self.assertEqual(shortest_distance.distance(4,3,6,5), 2.8284)
        self.assertEqual((shortest_distance.distance(-1,-1,0,0)),1.4142)



if __name__=='__main__':
    unittest.main()
