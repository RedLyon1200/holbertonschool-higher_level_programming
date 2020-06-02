#!/usr/bin/python3
"""[function that adds a new attribute to an object if it’s possible]
"""


def add_attribute(own_instance, own_attribute, value):
    """[summary]

    Arguments:
        own_instance {[my instance]}
        own_attribute {[my attribute]}
        value {[value to add]}

    Raises:
        TypeError: [can't add new attribute]
    """
    if '__dict__' not in dir(own_instance):
        raise TypeError("can't add new attribute")
    setattr(type(own_instance), own_attribute, value)
