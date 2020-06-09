#!/usr/bin/python3
"""[Unittest cases por rectangle.py]"""
import unittest
import pep8
from models.rectangle import Rectangle
from models.base import Base
from contextlib import redirect_stdout as out
import io


class TestsRectangle(unittest.TestCase):
    """
    Args:
        unittest
    """
    pass

    def setUp(self):
        """ print('setUp') """
        Base._Base__nb_objects = 0

    def test_style_rectangle(self):
        """test pep8
        """
        style = pep8.StyleGuide()
        m = style.check_files(["models/base.py"])
        self.assertEqual(m.total_errors, 0, "fix pep8")

    def test_rect_id_r(self):
        """[OK]"""
        r = Rectangle(10, 2)
        self.assertEqual(r.id, 1)
        r = Rectangle(2, 10)
        self.assertEqual(r.id, 2)
        r = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r.id, 12)
        r = Rectangle(10, 10)
        self.assertEqual(r.id, 3)

    def test_subcls_r(self):
        """[sub class]"""
        r = Rectangle(10, 2)
        self.assertTrue(issubclass(Rectangle, Base))

    def test_w_neg_r(self):
        """[negative width]"""
        with self.assertRaises(ValueError):
            r = Rectangle(-2, 10)

    def test_h_neg_r(self):
        """[negative height]"""
        with self.assertRaises(ValueError):
            r = Rectangle(2, -10)

    def test_w_str_r(self):
        """[str as width]"""
        with self.assertRaises(TypeError):
            r = Rectangle('', 10)

    def test_h_str_r(self):
        """[str as height]"""
        with self.assertRaises(TypeError):
            r = Rectangle(10, '')

    def test_w_dict_r(self):
        """[dict as width]"""
        with self.assertRaises(TypeError):
            r = Rectangle({}, 10)

    def test_h_dict_r(self):
        """[dict as height]"""
        with self.assertRaises(TypeError):
            r = Rectangle(10, {})

    def test_w_tup_r(self):
        """[tuple as width]"""
        with self.assertRaises(TypeError):
            r = Rectangle((), 10)

    def test_h_tup_r(self):
        """[tuple as height]"""
        with self.assertRaises(TypeError):
            r = Rectangle(10, ())

    def test_w_list_r(self):
        """[list as width]"""
        with self.assertRaises(TypeError):
            r = Rectangle([], 10)

    def test_h_list_r(self):
        """[list as height]"""
        with self.assertRaises(TypeError):
            r = Rectangle(10, [])

    def test_w_float_r(self):
        """[float as width]"""
        with self.assertRaises(TypeError):
            r = Rectangle(3.14159, 10)

    def test_h_float_r(self):
        """[float as height]"""
        with self.assertRaises(TypeError):
            r = Rectangle(10, 3.14159)

    def test_w_none_r(self):
        """[none as width]"""
        with self.assertRaises(TypeError):
            r = Rectangle(None, 10)

    def test_h_none_r(self):
        """[none as height]"""
        with self.assertRaises(TypeError):
            r = Rectangle(10, None)

    def test_w_set_r(self):
        """[set as width]"""
        with self.assertRaises(TypeError):
            r = Rectangle({1}, 10)

    def test_h_set_r(self):
        """[set as height]"""
        with self.assertRaises(TypeError):
            r = Rectangle(2, {1})

    def test_x_neg_r(self):
        """[negative x]"""
        with self.assertRaises(ValueError):
            r = Rectangle(2, 10, -1)

    def test_y_neg_r(self):
        """[negative y]"""
        with self.assertRaises(ValueError):
            r = Rectangle(2, 10, 1, -1)

    def test_x_str_r(self):
        """[str as x]"""
        with self.assertRaises(TypeError):
            r = Rectangle(2, 10, '')

    def test_y_str_r(self):
        """[str as y]"""
        with self.assertRaises(TypeError):
            r = Rectangle(10, 2, 1, '')

    def test_x_dict_r(self):
        """[dict as x]"""
        with self.assertRaises(TypeError):
            r = Rectangle(2, 10, {})

    def test_y_dict_r(self):
        """[dict as y]"""
        with self.assertRaises(TypeError):
            r = Rectangle(10, 2, 1, {})

    def test_x_tup_r(self):
        """[tuple as x]"""
        with self.assertRaises(TypeError):
            r = Rectangle(2, 10, ())

    def test_y_tup_r(self):
        """[tuple as y]"""
        with self.assertRaises(TypeError):
            r = Rectangle(10, 2, 1, ())

    def test_x_list_r(self):
        """[list as x]"""
        with self.assertRaises(TypeError):
            r = Rectangle(2, 10, [])

    def test_y_list_r(self):
        """[list as y]"""
        with self.assertRaises(TypeError):
            r = Rectangle(10, 2, 1, [])

    def test_x_float_r(self):
        """[float as x]"""
        with self.assertRaises(TypeError):
            r = Rectangle(2, 10, 3.14159)

    def test_y_float_r(self):
        """[float as y]"""
        with self.assertRaises(TypeError):
            r = Rectangle(10, 2, 1, 3.14159)

    def test_x_none_r(self):
        """[none as x]"""
        with self.assertRaises(TypeError):
            r = Rectangle(2, 10, None)

    def test_y_none_r(self):
        """[none as y]"""
        with self.assertRaises(TypeError):
            r = Rectangle(10, 2, 1, None)

    def test_x_set_r(self):
        """[set as x]"""
        with self.assertRaises(TypeError):
            r = Rectangle(2, 10, {1})

    def test_y_set_r(self):
        """[set as y]"""
        with self.assertRaises(TypeError):
            r = Rectangle(2, 10, 1, {1})

    def test_area_r(self):
        """[area]"""
        r = Rectangle(15588, 1200)
        self.assertEqual(r.area(), 18705600)

    def test_display_with_w_and_h_r(self):
        """[stdout w and h]"""
        with io.StringIO() as buff, out(buff):
            r = Rectangle(10, 15)
            r.display()
            expected_display = '##########\n' * 15
            self.assertEqual(buff.getvalue(), expected_display)

    def test__str___r(self):
        """[__str__ validates]"""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), '[Rectangle] (12) 2/1 - 4/6')
        r = Rectangle(5, 5, 1)
        self.assertEqual(str(r), '[Rectangle] (1) 1/0 - 5/5')

    def test_display_with_x_and_y_r(self):
        """[stdout x and y]"""
        with io.StringIO() as buff, out(buff):
            r1 = Rectangle(2, 3, 2, 2)
            r1.display()
            print("---")
            r2 = Rectangle(3, 2, 1, 0)
            r2.display()

            expected_display = '\n\n' + \
                ('  ##\n' * 3) + '---\n' + (' ###\n' * 2)
            self.assertEqual(buff.getvalue(), expected_display)

    def test_update_with_args_r(self):
        """[update #0 with *args]"""
        r = Rectangle(10, 11, 12, 13, 55)
        r.update(100, 20, 30, 40, 50)
        self.assertEqual(r.id, 100)
        self.assertEqual(r.width, 20)
        self.assertEqual(r.height, 30)
        self.assertEqual(r.x, 40)
        self.assertEqual(r.y, 50)

    def test_update_with_args_and_kwargs_r(self):
        """[update #1 with *args and **kwargs]"""
        r = Rectangle(10, 11, 12, 13, 55)
        r.update(100, 20, id=69)
        self.assertEqual(r.id, 100)
        self.assertEqual(r.width, 20)
        self.assertEqual(r.height, 11)
        self.assertEqual(r.x, 12)
        self.assertEqual(r.y, 13)
        r.update(x=1, height=2, y=3, width=4)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.y, 3)
        self.assertEqual(r.width, 4)

    def test_docstring_r(self):
        """[docstring]"""
        self.assertIsNotNone(Rectangle.__doc__)
        self.assertIsNotNone(Rectangle.__init__.__doc__)
        self.assertIsNotNone(Rectangle.width.__doc__)
        self.assertIsNotNone(Rectangle.height.__doc__)
        self.assertIsNotNone(Rectangle.x.__doc__)
        self.assertIsNotNone(Rectangle.y.__doc__)
        self.assertIsNotNone(Rectangle.area.__doc__)
        self.assertIsNotNone(Rectangle.display.__doc__)
        self.assertIsNotNone(Rectangle.__str__.__doc__)
        self.assertIsNotNone(Rectangle.update.__doc__)
        self.assertIsNotNone(Rectangle.to_dictionary.__doc__)


if __name__ == "__main__":
    """[main]"""
    unittest.main()
