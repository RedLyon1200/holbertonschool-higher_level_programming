#!/usr/bin/python3
"""[Test cases por rectangle.py]"""
import unittest
import pep8
from models.base import Base
from models.rectangle import Rectangle


class TestsRectangle(unittest.TestCase):
    """
    Args:
        unittest
    """
    pass

    @classmethod
    def setUpClass(cls):
        """ print('setUpClass') """

    @classmethod
    def tearDownClass(cls):
        """ print('tearDownClass') """

    def setUp(self):
        """ print('setUp') """
        Base._Base__nb_objects = 0

    def tearDown(self):
        """ print('tearDown\n') """

    def test_style_base(self):
        """[pep8]"""
        style = pep8.StyleGuide()
        m = style.check_files(["models/rectangle.py"])
        self.assertEqual(m.total_errors, 0, "fix pep8")

    def test_rect_id(self):
        """[OK]"""
        r = Rectangle(10, 2)
        self.assertEqual(r.id, 1)
        r = Rectangle(2, 10)
        self.assertEqual(r.id, 2)
        r = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r.id, 12)
        r = Rectangle(10, 10)
        self.assertEqual(r.id, 3)

    def test_w_neg(self):
        """[negative width]"""
        with self.assertRaises(ValueError):
            r = Rectangle(-2, 10)

    def test_h_neg(self):
        """[negative height]"""
        with self.assertRaises(ValueError):
            r = Rectangle(2, -10)

    def test_w_str(self):
        """[str as width]"""
        with self.assertRaises(TypeError):
            r = Rectangle("2", 10)

    def test_h_str(self):
        """[str as height]"""
        with self.assertRaises(TypeError):
            r = Rectangle(10, "2")

    def test_w_dict(self):
        """[dict as width]"""
        with self.assertRaises(TypeError):
            r = Rectangle({}, 10)

    def test_h_dict(self):
        """[dict as height]"""
        with self.assertRaises(TypeError):
            r = Rectangle(10, {})

    def test_w_tup(self):
        """[tuple as width]"""
        with self.assertRaises(TypeError):
            r = Rectangle((), 10)

    def test_h_tup(self):
        """[tuple as height]"""
        with self.assertRaises(TypeError):
            r = Rectangle(10, ())

    def test_w_list(self):
        """[list as width]"""
        with self.assertRaises(TypeError):
            r = Rectangle([], 10)

    def test_h_list(self):
        """[list as height]"""
        with self.assertRaises(TypeError):
            r = Rectangle(10, [])

    def test_w_float(self):
        """[float as width]"""
        with self.assertRaises(TypeError):
            r = Rectangle((), 10)

    def test_h_float(self):
        """[float as height]"""
        with self.assertRaises(TypeError):
            r = Rectangle(10, ())


if __name__ == "__main__":
    unittest.main()
