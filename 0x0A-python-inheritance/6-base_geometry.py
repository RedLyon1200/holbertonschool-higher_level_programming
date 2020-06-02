#!/usr/bin/python3
"""[ a class BaseGeometry (based on 5-base_geometry.py).]
"""


class BaseGeometry:
    """[Public instance method: def area(self): that raises an
       Exception with the message area() is not implemented]
    """
    pass

    def area(self):
        """[raises an Exception]

        Raises:
            Exception: [area() is not implemented]
        """
        raise Exception('area() is not implemented')
