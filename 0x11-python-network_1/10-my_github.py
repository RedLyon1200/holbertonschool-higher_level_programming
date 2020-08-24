#!/usr/bin/python3
"""[summary]
"""

import requests
from sys import argv


def fetches(user, pwd):
    """[summary]
    """
    url = 'https://api.github.com/user'
    response = requests.get(url, auth=(user, pwd))
    print(response.json().get('id'))


if __name__ == "__main__":
    user = argv[1]
    pwd = argv[2]

    fetches(user, pwd)
