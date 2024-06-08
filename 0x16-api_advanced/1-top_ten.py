#!/usr/bin/python3
"""Query Reddit API to print
   first 10 hot posts listed for
   give subreddit
"""

import requests


def top_ten(subreddit):
    """function for the query
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {"User-Agent": "python3:1-top_ten:v1.0.0 (by /u/000)"}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
                results = response.json().get("data")
                [print(c.get("data").get("title")) for c in results.get("children")]
    except (KeyError, ValueError, requests.RequestException):
        print(None)
        return
    print(None)
