#!/usr/bin/python3
"""
Query Reddit API
"""

import requests

def number_of_subscribers(subreddit):
    """Return the number of subscribers
    for a give subreddit
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
         data = response.json()
         subscribers = data.get('data').get('subscribers')
         return subscribers
    else:
        return 0