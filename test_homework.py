# Unit 1 Homework 9000 Test script
# Author: Chris Proctor and Jacob Wolf
# --------------------
# YOU DO NOT NEED TO UNDERSTAND THIS CODE RIGHT NOW!
# This script imports all the functions from your homework and tests them out. Hopefully they work!
# Testing is really important in computer science, so some nice functions are provided. We'll use them.

import unittest

from hw_01_9000_solutions import *

class TestHomework_01_9000(unittest.TestCase):

    def test_list_add(self):
        self.assertEqual(list_add([1, 2, 3], [2, 2, 2]), [3, 4, 5])
        self.assertEqual(list_add([3, 2, 1], [2, 2, 2]), [5, 4, 3])
        self.assertEqual(list_add([3, 2, 1], [-2, -2, -2]), [1, 0, -1])
        self.assertEqual(list_add([2, 3, 2, 6, 7], [2, 2, 2, 3, 1]), [4, 5, 4, 9, 8])
        self.assertEqual(list_add([2], [4]), [6])
        self.assertEqual(list_add([], []), [])

    def test_list_subtract(self):
        self.assertEqual(list_subtract([1, 2, 3], [3, 2, 1]), [-2, 0, 2])
        self.assertEqual(list_subtract([3, 2, 1], [3, 2, 1]), [0, 0, 0])
        self.assertEqual(list_subtract([1, 2, 3], [1, 0, -1]), [0, 2, 4])
        self.assertEqual(list_subtract([1, 2, 3, 3, 2], [3, 2, 1, 0, 1]), [-2, 0, 2, 3, 1])
        self.assertEqual(list_subtract([4], [3]), [1])
        self.assertEqual(list_subtract([], []), [])

    def test_list_max(self):
        self.assertEqual(list_max([1, 2, 3, 4], [5, 4, 3, 2]), [5, 4, 3, 4])
        self.assertEqual(list_max([5, 7, 3, 5], [11, 4, 6, 5]), [11, 7, 6, 5])
        self.assertEqual(list_max([1, 3, 4], [5, 3, 2]), [5, 3, 4])
        self.assertEqual(list_max([1, 2, 3, 4], [-1, -2, -3, -4]), [1, 2, 3, 4])
        self.assertEqual(list_max([3], [2]), [3])
        self.assertEqual(list_max([], []), [])
    def test_dict_merge(self):
        self.assertEqual(dict_merge({'red': 'rojo', 'blue': 'azul'}, {'purple': '紫色', 'blue': '蓝色'}), {'red': 'rojo', 'blue': '蓝色', 'purple': '紫色'})
        self.assertEqual(dict_merge({'red': 'rojo'}, {'purple': '紫色', 'blue': '蓝色'}), {'red': 'rojo', 'blue': '蓝色', 'purple': '紫色'})
        self.assertEqual(dict_merge({'red': 'rojo', 'blue': 'azul'}, {'red': '红色', 'blue': '蓝色'}), {'red': '红色', 'blue': '蓝色'})
        self.assertEqual(dict_merge({}, {'red': '红色', 'blue': '蓝色'}), {'red': '红色', 'blue': '蓝色'})
        self.assertEqual(dict_merge({}, {}), {})

# This runs all the tests.
unittest.main()
