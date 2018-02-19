import unittest
from retirement import *


class TestRetirement(unittest.TestCase):

    def test_age_hundred_plus_fail(self):
        self.assertEqual(retirement(100, 10000, 20, 10000), -1)

    def test_goal_achieved(self):
        self.assertTrue(retirement(20, 100000, 35, 1000000) > 0)

    def test_goal_failed(self):
        self.assertEqual(retirement(20, 10000, 0, 100000000), -1)


if __name__ == '__main__':
    unittest.main()
