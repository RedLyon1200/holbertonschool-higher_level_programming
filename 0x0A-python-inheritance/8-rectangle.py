#!/usr/bin/python3
"""[a class Rectangle that inherits from BaseGeometry (7-base_geometry.py).]
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
