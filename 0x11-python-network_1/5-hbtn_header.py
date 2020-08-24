#!/usr/bin/python3
"""[summary]
"""

import requests
from sys import argv


def fetches(url):
    """[summary]
    """
    response = requests.get(url)

    print('{}'.format(response.headers.get('X-Request-Id')))


if __name__ == "__main__":
    url = argv[1]

    fetches(url)
