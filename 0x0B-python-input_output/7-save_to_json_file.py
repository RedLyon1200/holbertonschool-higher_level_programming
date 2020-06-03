#!/usr/bin/python3
"""[function that writes an Object to a text file,
    using a JSON representation]
    """

import json


def save_to_json_file(my_obj, filename):
    """
    Arguments:
        my_obj [object]
        filename {[str]} -- [file path])
    """
    with open(filename, 'w') as f_obj:
        json.dump(my_obj, f_obj)
