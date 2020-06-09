#!/usr/bin/python3
"""[Test cases por base.py]"""

import unittest
import pep8
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestsBase(unittest.TestCase):
    """
    Args:
        unittest
    """

    def setUp(self):
        """ print('setUp') """
        Base._Base__nb_objects = 0

    def test_style_base(self):
        """test pep8
        """
        style = pep8.StyleGuide()
        m = style.check_files(["models/base.py"])
        self.assertEqual(m.total_errors, 0, "fix pep8")

    def test_id_ok_b(self):
        """[OK]"""
        base = Base()
        self.assertEqual(base.id, 1)
        base = Base()
        self.assertEqual(base.id, 2)
        base = Base(5)
        self.assertEqual(base.id, 5)
        base = Base(None)
        self.assertEqual(base.id, 3)
        self.assertEqual(type(base.id), int)

    def test_id_none_b(self):
        """[none]"""
        base = Base(None)
        self.assertEqual(base.id, 1)
        self.assertEqual(type(base.id), int)

    def test_id_neg_b(self):
        """[negative]"""
        base = Base(-1)
        self.assertEqual(base.id, -1)
        self.assertEqual(type(base.id), int)

    def test_id_dict_b(self):
        """[dictionary]"""
        base = Base({})
        self.assertEqual(base.id, {})
        self.assertEqual(type(base.id), dict)

    def test_id_tuple_b(self):
        """[tuple]"""
        base = Base(())
        self.assertEqual(base.id, ())
        self.assertEqual(type(base.id), tuple)

    def test_id__list_b(self):
        """[list]"""
        base = Base([])
        self.assertEqual(base.id, [])
        self.assertEqual(type(base.id), list)

    def test_id_str_b(self):
        """[string]"""
        base = Base('str')
        self.assertEqual(base.id, 'str')
        self.assertEqual(type(base.id), str)

    def test_id_float_b(self):
        """[float]"""
        base = Base(0.8)
        self.assertEqual(base.id, 0.8)
        self.assertEqual(type(base.id), float)

    def test_id_bool_b(self):
        """[bool]"""
        base = Base(True)
        self.assertEqual(base.id, True)
        self.assertEqual(type(base.id), bool)

    def test_id_set_b(self):
        """[set]"""
        base = Base({1, 3, 1, 4})
        self.assertEqual(base.id, {1, 3, 1, 4})
        self.assertEqual(type(base.id), set)

    def test_dict_to_string_b(self):
        """[dictionary to string]"""
        base = Base()
        tmp_dict = {
            'width': 12,
            'height': 5,
            'x': 2,
            'y': 10,
            'id': 1
        }
        self.assertEqual(type(base.to_json_string(tmp_dict)), str)

    def test_empty_dict_b(self):
        """[empty dictionary]"""
        base = Base()
        self.assertEqual(base.to_json_string(None), '[]')

    def test_to_dict_b(self):
        """[rectangle to dictioanry]"""
        r = Rectangle(10, 2, 11, 7, id=9)
        self.assertEqual(type(r.to_dictionary()), dict)

    def test_from_json_str_b(self):
        """[from json str]"""
        base = Base()
        tmp_dict = '{"width": 10, "height": 2, "x": 4, "y": 7, "id": 1}'
        self.assertEqual(type(base.from_json_string(tmp_dict)), dict)
        tmp_dict = '[{"width": 10, "height": 2, "x": 4, "y": 7, "id": 1}]'
        self.assertEqual(type(base.from_json_string(tmp_dict)), list)

    def test_from_empy_json_str_b(self):
        """[empty json str]"""
        base = Base()
        self.assertEqual(type(base.from_json_string(None)), list)

    def test_to_file_b(self):
        """[save file]"""
        r = Rectangle(2, 4)
        Rectangle.save_to_file([r])
        a = 0
        with open("Rectangle.json", "r"):
            a = 1
        self.assertEqual(a, 1)

    def test_create_b(self):
        """[create]"""
        r = Rectangle(3, 5, 1)
        r_dict = r.to_dictionary()
        r1 = Rectangle.create(**r_dict)
        self.assertEqual(str(r), str(r1))

    def test_loadFrom_b(self):
        """[load]"""
        s = Square(7, 9, 1)
        list_squares_input = [s]
        Square.save_to_file(list_squares_input)
        li = Square.load_from_file()
        self.assertEqual(type(li) is list and
                         li[0].__class__.__name__ is "Square", True)


if __name__ == "__main__":
    """[main]"""
    unittest.main()
