import unittest

import shortest_distance

class Test_shortest_distance(unittest.TestCase):

    def test_distance(self):

        self.assertEqual(shortest_distance.distance(1,1,1,1), 0.0)
        self.assertTrue((shortest_distance.distance(2,3,1,2)),round(1.4142135623730951,4))
        self.assertFalse(shortest_distance.distance())

    def test_floatvalues(self):
        #self.assertTrue(shortest_distance.floatValues(0,0,0,0))
        self.assertTrue(shortest_distance.floatValues(1,1,1,1))
        self.assertTrue(shortest_distance.floatValues(2,4,5,8))
        self.assertTrue(shortest_distance.floatValues(-2,-1,-3,-6))
        self.assertTrue(shortest_distance.floatValues(-2,1,-3,6))



if __name__=='__main__':
    unittest.main()
