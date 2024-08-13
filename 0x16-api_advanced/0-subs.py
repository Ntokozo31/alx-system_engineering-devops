#!/usr/bin/python3

"""
WE write a script that queries the reddit api.
and return the number of subscribers
"""

import requests

def number_of_subscribers(subreddit):
    """Return the total number of subscribers."""
    url = "https://www.reddit.com/r/{}/about.json".format(subredit)
    headers = {"User-Agent": "Mozille/5.0"}
    response = request.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
