#!/usr/bin/python3
"""[summary]
"""

import requests


def fetches(url):
    """[summary]
    """
    response = requests.get(url)

    print('{}'.format(response.headers['X-Request-Id']))


if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'

    fetches(url)
