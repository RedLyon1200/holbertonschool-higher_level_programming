#!/usr/bin/python3
"""
[function that returns True if the object is exactly an
instance of the specified class ; otherwise False]
"""


def is_same_class(obj, a_class):
    """[summary]

    Arguments:
        obj -- [object]
        a_class -- [class]

    Returns:
        [bool] -- [if the object is exactly an
instance of the specified class]
    """
    return True if type(obj) == a_class else False
