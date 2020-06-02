#!/usr/bin/python3
"""[a class BaseGeometry (based on 6-base_geometry.py).]
"""


class BaseGeometry:
    """[BaseGeometry]
    """
    pass

    def area(self):
        """[Public instance method that raises an Exception]

        Raises:
            Exception: [area() is not implemented]
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """[method that validates value]

        Arguments:
            name {[string]}
            value {[int]}

        Raises:
            TypeError: [<name> must be an integer]
            ValueError: [<name> must be greater than 0]
        """
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))

        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
