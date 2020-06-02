#!/usr/bin/python3
"""[a class MyInt that inherits from int]
"""


class MyInt(int):
    """[summary]

    Arguments:
        int {[class]} -- [inheritance class]

    Returns:
        [bool] -- [MyInt is a rebel. MyInt has == and != operators inverted]
    """
    pass

    def __eq__(self, other):
        """[it's a revealing comparison]
        Returns:
            [bool] -- [false if other is equal]
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """[it's a revealing comparison]
        Returns:
            [bool] -- [true if other is not equal]
        """
        return super().__eq__(other)
