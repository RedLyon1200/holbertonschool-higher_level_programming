#!/usr/bin/python3
"""[the first class Base]
"""


class Base:
    """[manage id attribute in all your future classes and
    to avoid duplicating the same code]
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """[id is not None, assign the public instance attribute id

        otherwise, increment __nb_objects and assign the
        new value to the public instance attribute id]

        Args:
            id ([int], optional). Defaults to None.
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
