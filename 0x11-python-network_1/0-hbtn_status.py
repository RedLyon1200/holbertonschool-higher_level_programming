#!/usr/bin/python3
"""
script that fetches url
"""
import urllib.request


def fetche(url):
    """
    fetches url
    """
    pass

    with urllib.request.urlopen(url) as response:
        html_content = response.read()

        print('Body response:')
        print('\t- type: {}'.format(type(html_content)))
        print('\t- content: {}'.format(html_content))
        print('\t- utf8 content: {}'.format(html_content.decode('utf-8')))


if __name__ == "__main__":
    """[summary]
    """
    url = 'https://intranet.hbtn.io/status'

    fetche(url)
