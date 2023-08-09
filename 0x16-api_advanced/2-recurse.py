#!/usr/bin/python3
"""
Definition for top_ten which queries the Reddit API and prints the titles of
the hot posts listed for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Redddit API and returns a list of all hot articles
    for a given subreddit
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)

    if after:
        url += "&after={}".format(after)

    headers = {"User-Agent": "My-App/0  .0.2"}

    r = requests.get(url, headers=headers)
    result = r.json()

    if "error" in result or r.status_code != 200:
        return (None)
    hot_data = result["data"]["children"]
    if len(hot_data) == 0:
        return (None if len(hot_list) == 0 else hot_list)
    for q in hot_data:
        hot_list.append(q["data"]["title"])
    next_after = result["data"]["after"]
    recurse(subreddit, hot_list, next_after)
