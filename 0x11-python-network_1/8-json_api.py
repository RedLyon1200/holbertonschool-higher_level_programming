#!/usr/bin/python3
"""[summary]
"""

import requests
from sys import argv


def fetches(q=''):
    """[summary]
    """
    response = requests.post(url, data=q)

    try:
        json_obj = response.json()
        if json_obj:
            print('[{}] {}'.format(json_obj['id'], json_obj['name']))
        else:
            print('No result')
    except ValueError:
        print('Not a valid JSON')


if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    if len(argv) == 2:
        fetches(argv[1])
    else:
        fetches()
