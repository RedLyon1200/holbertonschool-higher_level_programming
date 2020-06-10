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
    pass

    def setUp(self):
        """ print('setUp') """
        Base._Base__nb_objects = 0

    def test_id_ok(self):
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

    def test_id_none(self):
        """[none]"""
        base = Base(None)
        self.assertEqual(base.id, 1)
        self.assertEqual(type(base.id), int)
        base = Base()
        self.assertEqual(base.id, 2)
        self.assertEqual(type(base.id), int)

    def test_id_neg(self):
        """[negative]"""
        base = Base(-1)
        self.assertEqual(base.id, -1)
        self.assertEqual(type(base.id), int)

    def test_id_dict(self):
        """[dictionary]"""
        base = Base({})
        self.assertEqual(base.id, {})
        self.assertEqual(type(base.id), dict)

    def test_id_tuple(self):
        """[tuple]"""
        base = Base(())
        self.assertEqual(base.id, ())
        self.assertEqual(type(base.id), tuple)

    def test_id__list(self):
        """[list]"""
        base = Base([])
        self.assertEqual(base.id, [])
        self.assertEqual(type(base.id), list)

    def test_id_str(self):
        """[string]"""
        base = Base('str')
        self.assertEqual(base.id, 'str')
        self.assertEqual(type(base.id), str)

    def test_id_float(self):
        """[float]"""
        base = Base(0.8)
        self.assertEqual(base.id, 0.8)
        self.assertEqual(type(base.id), float)

    def test_id_bool(self):
        """[bool]"""
        base = Base(True)
        self.assertEqual(base.id, True)
        self.assertEqual(type(base.id), bool)

    def test_id_set(self):
        """[set]"""
        base = Base({1, 3, 1, 4})
        self.assertEqual(base.id, {1, 3, 1, 4})
        self.assertEqual(type(base.id), set)

    def test_instance(self):
        """[instance of class Base]"""
        base = Base()
        self.assertIsInstance(base, Base)

    def test_conflicting_id(self):
        """[Conflicting id]"""
        base = Base(5)
        base1 = Base(5)
        self.assertEqual(base1.id, 5)
        self.assertEqual(type(base.id), int)

    def test_dict_to_string(self):
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

    def test_empty_dict(self):
        """[empty dictionary]"""
        base = Base()
        self.assertEqual(base.to_json_string(None), '[]')

    def test_to_dict(self):
        """[rectangle to dictioanry]"""
        r = Rectangle(10, 2, 11, 7, id=9)
        self.assertEqual(type(r.to_dictionary()), dict)

    def test_from_json_str(self):
        """[from json str]"""
        base = Base()
        tmp_dict = '{"width": 10, "height": 2, "x": 4, "y": 7, "id": 1}'
        self.assertEqual(type(base.from_json_string(tmp_dict)), dict)
        tmp_dict = '[{"width": 10, "height": 2, "x": 4, "y": 7, "id": 1}]'
        self.assertEqual(type(base.from_json_string(tmp_dict)), list)

    def test_from_empy_json_str(self):
        """[empty json str]"""
        base = Base()
        self.assertEqual(type(base.from_json_string(None)), list)

    def test_style_rectangle(self):
        """
        Tests for pep8
        """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/base.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_docstring(self):
        """[docstring]"""
        self.assertIsNotNone(Base.__doc__)
        self.assertIsNotNone(Base.__init__.__doc__)
        self.assertIsNotNone(Base.to_json_string.__doc__)
        self.assertIsNotNone(Base.save_to_file.__doc__)
        self.assertIsNotNone(Base.from_json_string.__doc__)
        self.assertIsNotNone(Base.create.__doc__)
        self.assertIsNotNone(Base.load_from_file.__doc__)


if __name__ == "__main__":
    """[main]"""
    unittest.main()
