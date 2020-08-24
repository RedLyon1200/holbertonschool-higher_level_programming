#!/usr/bin/python3
"""[summary]
"""

import requests


def fetches(url):
    """[summary]
    """
    response = requests.get(url)
    status_code = response.status_code

    if status_code >= 400:
        print('Error code: {}'.format(status_code))
    else:
        print(response.text)


if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'

    fetches(url)
