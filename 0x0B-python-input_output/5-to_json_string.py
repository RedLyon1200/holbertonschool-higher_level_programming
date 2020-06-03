#!/usr/bin/python3
"""[function that change a data to its JSON representation]
    """

import json


def to_json_string(my_obj):
    """
    Arguments:
        my_obj {[type]} -- [description]

    Returns:
        [str] -- [returns the JSON representation of an object (string)]
    """
    return json.dumps(my_obj)
