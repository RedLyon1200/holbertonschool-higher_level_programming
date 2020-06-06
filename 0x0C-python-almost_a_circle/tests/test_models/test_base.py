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

    @classmethod
    def setUpClass(cls):
        """ print('setUpClass') """

    @classmethod
    def tearDownClass(cls):
        """ print('tearDownClass') """

    def setUp(self):
        """ print('setUp') """

    def tearDown(self):
        """ print('tearDown\n') """
        Base._Baje__nb_objects = 0

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

    def test_instance_id(self):
        """[instance of class Base]"""
        base = Base()
        self.assertIsInstance(base, Base)

    @unittest.expectedFailure
    def test_id_more_args(self):
        """[more args]"""
        base = Base(1, 2)

    def test_style_base(self):
        """[pep8]"""
        style = pep8.StyleGuide()
        m = style.check_files(["models/base.py"])
        self.assertEqual(m.total_errors, 0, "fix pep8")


if __name__ == "__main__":
    unittest.main()
