import unittest
from retirement import *


class TestRetirement(unittest.TestCase):

    def test_goal_achieved(self):
        self.assertTrue(retirement(20, 100000, 35, 1000000) > 0)

    def test_goal_failed(self):
        self.assertEqual(retirement(20, 10000, 1, 100000000), -1)


if __name__ == '__main__':
    unittest.main()
