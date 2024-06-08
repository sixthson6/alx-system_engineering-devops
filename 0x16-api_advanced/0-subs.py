#!/usr/bin/python3
"""function that queries the Reddit API and returns the number of subscribers
   for a given subreddit
   If an invalid subreddit is given, the function should return 0.
"""
import requests


def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "python3:1-subs:v1.0.0 (by /u/000)"}
    try:
        sub = requests.get(url, headers=headers, allow_redirects=False)
        if sub.status_code == 200:
            subs = sub.json()
            subscribers = subs['data']['subscribers']
            return subscribers
        else:
            return 0
    except (KeyError, ValueError):
        return 0
    return 0
