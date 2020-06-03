#!/usr/bin/python3
"""[ script that adds all arguments to a Python list,
    and then save them to a file]
    """

import sys

Save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
Load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
filename = 'add_item.json'

try:
    """[it is validated if the file exists
        and its content is stored in the object]"""
    my_obj = Load_from_json_file(filename)
except Exception:
    """[If it does not exist the empty object is created]"""
    my_obj = []
finally:
    """[Arguments are added]"""
    my_obj.extend(sys.argv[1:])

    Save_to_json_file(my_obj, filename)
