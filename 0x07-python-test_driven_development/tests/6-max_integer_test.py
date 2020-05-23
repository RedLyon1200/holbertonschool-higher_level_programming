#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    """Unittests for max_integer([integers])"""

    def test_ascending(self):
        """ascending list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_descending(self):
        """descending list"""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_middle(self):
        """max in the middle of the list"""
        self.assertEqual(max_integer([3, 2, 5, 4, 1]), 5)

    def test_one_integer(self):
        """list of one integer"""
        self.assertEqual(max_integer([-1]), -1)

    def test_duplicate(self):
        """list of duplicated integer"""
        self.assertEqual(max_integer([420, 420]), 420)

    def test_empty_list(self):
        """empty list"""
        self.assertEqual(max_integer([]), None)

    def test_int(self):
        """integer"""
        with self.assertRaises(Exception):
            max_integer(1)

    def test_float(self):
        """float"""
        with self.assertRaises(Exception):
            max_integer(3.1415926)

    def test_boolean(self):
        """boolean"""
        with self.assertRaises(Exception):
            max_integer(True)

    def test_string(self):
        """string"""
        result = max_integer('')
        self.assertRaises(Exception, result)

    def test_tuple(self):
        """tuple"""
        result = max_integer(())
        self.assertRaises(Exception, result)

    def test_dict(self):
        """dictionary"""
        result = max_integer({})
        self.assertRaises(Exception, result)

    def test_void(self):
        """None"""
        with self.assertRaises(Exception):
            max_integer(None)

    def test_float_list(self):
        """list of floats"""
        result = max_integer([3.14159265])
        self.assertRaises(Exception, result)

    def test_none_list(self):
        """list with None"""
        result = max_integer([None])
        self.assertRaises(Exception, result)

    def test_string_list(self):
        """list of strings"""
        result = max_integer([''])
        self.assertRaises(Exception, result)

    def test_string_list(self):
        """list of lists"""
        result = max_integer([[1]])
        self.assertRaises(Exception, result)

    def test_string_list(self):
        """list of dic"""
        result = max_integer([{}])
        self.assertRaises(Exception, result)

    def test_string_list(self):
        """list of tuples"""
        result = max_integer([()])
        self.assertRaises(Exception, result)
