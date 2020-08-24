#!/usr/bin/python3
"""[summary]
"""

import requests
from sys import argv


def fetches(repo, user):
    """[summary]
    """
    url = 'https://api.github.com/repos/{}/{}/commits'.format(
        user, repo
    )
    response = requests.get(url)
    json_obj = response.json()
    for item in json_obj[:10]:
        sha = item.get('sha')
        item = item.get('commit')
        print('{}: {}'.format(sha, item.get('author').get('name')))


if __name__ == "__main__":
    repo = argv[1]
    user = argv[2]

    fetches(repo, user)
