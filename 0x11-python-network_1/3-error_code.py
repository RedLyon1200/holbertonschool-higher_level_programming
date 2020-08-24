#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL and
displays the value of the X-Request-Id variable found in
the header of the response
"""
import urllib.request
from urllib.error import HTTPError
from sys import argv


def fetche(url):
    """
    fetches X-Request-Id value in a url
    """
    pass

    try:
        with urllib.request.urlopen(url) as response:
            html_content = response.read()

            print(html_content.decode('utf-8'))
    except HTTPError as e:
        print('Error code: {}'.format(e.code))


if __name__ == "__main__":
    """
    entry point
    """
    url = argv[1]

    fetche(url)
