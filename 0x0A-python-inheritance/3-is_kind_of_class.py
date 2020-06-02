#!/usr/bin/python3
"""
[function that returns True if the object is an instance of,
or if the object is an instance of a class that inherited from,
the specified class ; otherwise False.]
"""


def is_kind_of_class(obj, a_class):
    """[if the object is an instance of, or if the object is an
    instance of a class that inherited from, the specified class]

    Arguments:
        obj -- [object]
        a_class  -- [class]

    Returns:
        [Bool] -- [if the object is an instance of a class]
    """
    return isinstance(obj, a_class)
