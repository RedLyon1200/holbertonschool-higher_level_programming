#!/usr/bin/python3
"""[Class Rectangle]

    Raises:
        TypeError: [width must be an integer]
        ValueError: [width must be >= 0]
        TypeError: [height must be an integer]
        ValueError: [height must be >= 0]

    Returns:
        [int] -- [width or height of rectangle ]
    """


class Rectangle:
    pass

    def __init__(self, width=0, height=0):
        """[initializes rectangle]

        Keyword Arguments:
            width {int} -- [rectangle width] (default: {0})
            heigth {int} -- [rectangle height] (default: {0})
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """[Gets the width of the rectangle]

        Returns:
            [int] -- [width of the rectangle]
        """
        return self.__width

    @width.setter
    def width(self, value):
        """[Sets the width of the rectangle]

        Arguments:
            value {[int]} -- [New size for width]

        Raises:
            TypeError: [width must be an integer]
            ValueError: [width must be >= 0]
        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """[Gets the height of the rectangle]

        Returns:
            [int] -- [height of the rectangle]
        """
        return self.__height

    @height.setter
    def height(self, value):
        """[Sets the height of the rectangle]

        Arguments:
            value {[int]} -- [New size for height]

        Raises:
            TypeError: [height must be an integer]
            ValueError: [height must be >= 0]
        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
