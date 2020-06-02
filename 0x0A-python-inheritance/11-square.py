#!/usr/bin/python3
"""[a class Square that inherits from Rectangle (9-rectangle.py):]
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """[summary]

    Arguments:
        Rectangle {[class]} -- [inheritance class]
    """
    pass

    def __init__(self, size):
        """[Instantiation with size]

        Arguments:
            size {[int]} -- [width and height of the Square]
        """
        super().integer_validator('size', size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def __str__(self):
        """
        Returns:
            [string] -- [the following square description:
            [Square] <width>/<height>]
        """
        return '[Square] {}/{}'.format(self.__size, self.__size)
