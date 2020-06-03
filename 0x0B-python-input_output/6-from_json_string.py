#!/usr/bin/python3
"""[change a data from its JSON representation to object]
    """


import json


def from_json_string(my_str):
    """
    Arguments:
        my_str {[str]} -- [string in JSON format]

    Returns:
        [list] -- [an object (Python data structure) represented by
                 a JSON string]
    """
    return json.loads(my_str)
