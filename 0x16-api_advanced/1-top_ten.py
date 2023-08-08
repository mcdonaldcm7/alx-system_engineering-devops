#!/usr/bin/python3
"""
Definition for top_ten which queries the Reddit API and prints the titles of
the first 10 post hot posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "My-App/0.0.2"}

    r = requests.get(url, headers=headers)
    result = r.json()["data"]["children"]

    for q in result:
        print(q["data"]["title"])
