#!/usr/bin/python3
"""
Definition for top_ten which queries the Reddit API and prints the titles of
the hot posts listed for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], count=None):
    """
    Recursively queries the Redddit API and returns a list of all hot articles
    for a given subreddit
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)

    if count:
        url += "?count={}".format(count)
    else:
        count = 0

    headers = {"User-Agent": "My-App/0  .0.2"}

    r = requests.get(url, headers=headers)
    result = r.json()

    if "error" in result or r.status_code != 200:
        return (hot_list)
    hot_data = result["data"]["children"]
    if len(hot_data) == 0:
        return (hot_list)
    for q in hot_data:
        hot_list.append(q["data"]["title"])
        count += 1
    recurse(subreddit, hot_list, count)
