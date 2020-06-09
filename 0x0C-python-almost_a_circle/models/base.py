#!/usr/bin/python3
"""[the first class Base]"""

import json
import csv
import os


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
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """[writes the JSON string representation of list_objs to a file]"""
        with open('{}.json'.format(cls.__name__), 'w') as f_obj:
            if list_objs is None:
                f_obj.write(cls.to_json_string(None))
            else:
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
        if cls.__name__ == "Square":
            dummy = cls(55)
            dummy.update(**dictionary)
        elif cls.__name__ == "Rectangle":
            dummy = cls(55, 40)
            dummy.update(**dictionary)
        return dummy

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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Save to csv file"""
        tmp_list_two = []
        for i in list_objs:
            tmp_list = []
            dic = i.to_dictionary()
            tmp_list.append(dic['id'])
            if cls.__name__ == "Rectangle":
                tmp_list.append(dic['width'])
                tmp_list.append(dic['height'])
            if cls.__name__ == "Square":
                tmp_list.append(dic['size'])
            tmp_list.append(dic['x'])
            tmp_list.append(dic['y'])
            tmp_list_two.append(tmp_list)
        with open(cls.__name__ + ".csv", mode='w') as f:
            csw = csv.writer(f)
            for i in tmp_list_two:
                csw.writerow(i)

    @classmethod
    def load_from_file_csv(cls):
        """Load from csv file"""
        if not os.path.isfile(cls.__name__ + ".csv"):
            return []
        ls = []
        with open(cls.__name__ + ".csv", 'r') as f:
            csr = csv.reader(f)
            csr = list(csr)
            lsdir = []
            for i in range(len(csr)):
                dic = {}
                dic.setdefault('id', int(csr[i][0]))
                if cls.__name__ == 'Rectangle':
                    dic.setdefault('width', int(csr[i][1]))
                    dic.setdefault('height', int(csr[i][2]))
                if cls.__name__ == 'Square':
                    dic.setdefault('size', int(csr[i][1]))
                dic.setdefault('x', int(csr[i][-2]))
                dic.setdefault('y', int(csr[i][-1]))
                lsdir.append(dic)
        for i in lsdir:
            dummy = cls.create(**i)
            ls.append(dummy)
        return ls
