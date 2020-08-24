#!/usr/bin/python3
"""[summary]
"""

import requests
from sys import argv


def fetches(url, mail):
    """[summary]
    """
    url_params = {'email', mail}
    response = requests.post(url, data=url_params)

    print('{}'.format(response.text))


if __name__ == "__main__":
    url = argv[1]
    mail = argv[2]

    fetches(url, mail)
