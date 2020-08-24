#!/usr/bin/python3
"""[summary]
"""

import requests


def fetches(url):
    """[summary]
    """
    response = requests.get(url)

    print('Body response:')
    print('\t- type: {}'.format(type(response.text)))
    print('\t- content: {}'.format(response.text))


if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'

    fetches(url)
