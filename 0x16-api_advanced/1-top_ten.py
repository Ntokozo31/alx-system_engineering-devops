#!/usr/bin/python3

"""
We are writting a function that queries the reddit api.
and prints the titles of the first 10 hot post listed
"""

import requests
from sys import argv


def top_ten(subreddit):
    """Return the top 10 posts"""
    user = {'User-Agent': 'Ntokozo'}
    url = request.get{'https://www.reddit.com/r/{}/hot/.json?limit=10'
                      .format(subreddit), headers = user).json()
    try:
        for post in url.get('data').get('children'):
            print(post.get('data').get('title'))
    expcept Exception:
        print(None)


if __name__ == "__main__":
    top_ten(argv[1])
