# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 20:25:11 2018

@author: Kazi Zakia
"""

import unittest
import function5

class TestsplitTip(unittest.TestCase):

    def test_emptylist(self):  #it checks if the list is empty
        self.assertEqual(len(function5.splitTip(12, 3)), 3)
    
    def test_input(self): #it check the valid input
        self.assertRaises(ValueError, function5.takeInput())
    
    def test_eventip(self):  #it checks if even amount of tips is equally distributed
        self.assertEqual(function5.splitTip(12, 3),[4.6, 4.6, 4.6])
        self.assertEqual(function5.splitTip(3.68, 3),[1.41, 1.41, 1.41])

    def test_uneventip(self): #it checks if uneven amount of tips is distributed deterministically
        self.assertEqual(function5.splitTip(3.66, 3),[1.41, 1.4, 1.4])
        self.assertEqual(function5.splitTip(3.67, 3),[1.41, 1.41, 1.4])

if __name__ == '__main__':
    unittest.main()