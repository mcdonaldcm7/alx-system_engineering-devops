#!/usr/bin/python3
"""
Definition for 'number_of_subscribers' which queries the Reddit API and returns
the number of subscribers for a given subredit.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Returns the total number of subscribers in the subreddit
    """
    url = "http://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "My-App/0.0.1"}

    r = requests.get(url, headers=headers)
    result = r.json()

    if result:
        if "error" in result or r.status_code != 200:
            return (0)
        else:
            return (result["data"]["subscribers"])
    return (0)
