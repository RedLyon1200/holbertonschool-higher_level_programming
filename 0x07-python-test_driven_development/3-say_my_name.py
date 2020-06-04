#!/usr/bin/python3
"""[Function that prints My name is <first name> <last name>]
    """


def say_my_name(first_name, last_name=""):
    """
    Args:
        first_name: first name :v
        last_name: (optional) lastname
    Raises:
        TypeError:
            first_name must be a string
            last_name must be a string
    """

    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
