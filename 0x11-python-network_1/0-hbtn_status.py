#!/usr/bin/python3
"""
"""
import urllib.request


def fetche(url):
    """
    """
    pass

    with urllib.request.urlopen(url) as response:
        html_content = response.read()

        print("""Body response:
\t- type: {}
\t- content: {}
\t- utf8 content: {}""".format(
            type(html_content), html_content, html_content.decode('utf-8')
        ))


if __name__ == "__main__":
    """[summary]
    """
    url = 'https://intranet.hbtn.io/status'

    fetche(url)
