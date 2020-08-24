#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL and
displays the value of the X-Request-Id variable found in
the header of the response.
"""
import urllib.request
import sys


def fetche(url, email):
    """
    fetches X-Request-Id value in a url
    """
    data = urllib.parse.urlencode({'email': email})
    data = data.encode('utf-8')

    with urllib.request.urlopen(url, data) as response:
        html_content = response.read()

        print(html_content.decode('utf-8'))


if __name__ == "__main__":
    """entry point
    """
    url = sys.argv[1]
    mail = sys.argv[2]

    fetche(url, mail)
