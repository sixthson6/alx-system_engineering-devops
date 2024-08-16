#!/usr/bin/python3
"""Query Reddit API
"""

import requests
# import sys

def top_ten(subreddit):
    """
    Print first 10 hot posted listed for a given subreddit
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)

    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}
    params = { 'limit': 10}

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data.get('data').get('children')
        return posts 
    else:
        return 0