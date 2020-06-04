#!/usr/bin/python3
"""[a class Student that defines a student (based on 12-student.py)]"""


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

    def to_json(self, attrs=None):
        """
        Returns:
            [If attrs is a list of strings, only attribute names contained in
            this list must be retrieved. Otherwise,
            all attributes must be retrieved]
        """
        my_dic = {}

        if attrs is None:
            return self.__dict__

        for item in attrs:
            if hasattr(self, item):
                my_dic[item] = getattr(self, item)

        return my_dic

    def reload_from_json(self, json):
        """
        Args:
            json ([dic])
        """
        for key, value in json.items():
            if hasattr(self, key):
                setattr(self, key, value)
