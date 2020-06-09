#!/usr/bin/python3
"""[the first class Base]"""

import json


class Base:
    """[manage id attribute in all your future classes
    and to avoid duplicating the same code]
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

    @staticmethod
    def to_json_string(list_dictionaries):
        """[JSON is one of the standard formats for sharing
            data representation.]

        Args:
            list_dictionaries ([list])

        Returns:
            [JSON string]: [representation of list_dictionaries]
        """
        if list_dictionaries is None or len(list_dictionaries) <= 0:
            return []
        return json.dumps(list_dictionaries, indent=4, sort_keys=True)

    @classmethod
    def save_to_file(cls, list_objs):
        """[writes the JSON string representation of list_objs to a file]"""
        with open('{}.json'.format(cls.__name__), 'w') as f_obj:
            f_obj.write(cls.to_json_string(
                [cls.to_dictionary(item) for item in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """[the list of the JSON string representation json_string]"""
        if json_string is None or len(json_string) <= 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """[Create, update and return a new Rectangle or Square instance]

        Returns:
            [instane]: [an instance with all attributes already set]
        """
        r = cls(55, 56)
        r.update(**dictionary)
        return r

    @classmethod
    def load_from_file(cls):
        """[load information from a file]

        Returns:
            [list]: [list of instances]
        """
        try:
            with open('{}.json'.format(cls.__name__), 'r') as f_obj:
                tmp_dict = cls.from_json_string(f_obj.read())
                return [cls.create(**item) for item in tmp_dict]
        except IOError:
            return []
