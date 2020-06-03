#!/usr/bin/python3
"""[a class Student that defines a student]"""


class Student:
    """
    """
    pass

    def __init__(self, first_name, last_name, age):
        """[Instantiation with first_name, last_name and age]

        Args:
            first_name ([str])
            last_name ([str])
            age ([int])
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """[summary]

        Returns:
            [list, dictionary, string, integer and boolean]:
            [the dictionary description with simple data structure]
        """
        return self.__dict__
