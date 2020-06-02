#!/usr/bin/python3
"""
[a class Rectangle that inherits from BaseGeometry (7-base_geometry.py).
(task based on 8-rectangle.py)]
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """[summary]

    Arguments:
        BaseGeometry {[class]} -- [inheritance class]
    """
    pass

    def __init__(self, width, height):
        """[Instantiation with width and height]

        Arguments:
            width {[int]} -- [width]
            height {[int]} -- [height]
        """
        super().integer_validator('width', width)
        super().integer_validator('height', height)
        self.__width = width
        self.__height = height

    def area(self):
        """[method must be implemented]

        Returns:
            [int] -- [area of Rectangle]
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns:
            [string] -- [the following rectangle description:
            [Rectangle] <width>/<height>]
        """
        return '[Rectangle] {}/{}'.format(self.__width, self.__height)
