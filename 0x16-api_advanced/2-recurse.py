#!/usr/bin/python3
"""Query Reddit API
   to retrieve hot posts titles
   using a recursive function
"""

import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """Query Reddit API
    to retrieve hot posts titles
    using a recursive function
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}
    params = {
        "after": after,
        "limit": 100
    }

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        if response.status_code == 404:
            return None

        results = response.json().get("data")
        after = results.get("after")
        for post in results.get("children"):
            hot_list.append(post.get("data").get("title"))
        if after is not None:
            return recurse(subreddit, hot_list, after)
        return hot_list
    except (KeyError, ValueError, RequestException):
        return None
