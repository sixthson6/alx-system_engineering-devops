#!/usr/bin/python3
"""function that queries the Reddit API and returns the number of subscribers
   for a given subreddit
   If an invalid subreddit is given, the function should return 0.
"""
import requests


def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    sub = requests.get(url, allow_redirects=False)
    if sub.status_code == 200:
        subs = sub.json()
        if 'data' in subs and 'subscribers' in subs['data']:
            return subs['data']['subscribers']
        else:
            return
    else:
        return 0
