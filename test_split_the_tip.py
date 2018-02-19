# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 20:25:11 2018

@author: Kazi Zakia
"""

import unittest
from split_the_tip import *


class TestSplitTheTip(unittest.TestCase):

    def test_even_tip(self):  # it checks if even amount of tips is equally distributed
        self.assertEqual(split_the_tip(12, 3), [4.6, 4.6, 4.6])
        self.assertEqual(split_the_tip(3.68, 3), [1.41, 1.41, 1.41])

    def test_uneven_tip(self):  # it checks if uneven amount of tips is distributed deterministically
        self.assertEqual(split_the_tip(3.66, 3), [1.41, 1.4, 1.4])
        self.assertEqual(split_the_tip(3.67, 3), [1.41, 1.41, 1.4])


if __name__ == '__main__':
    unittest.main()
