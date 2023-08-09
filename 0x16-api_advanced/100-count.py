#!/usr/bin/python3
"""
A recursive function that queries the Reddit API, parses the title of all hot
articles, and prints a sorted count of given keywords
"""
import requests


def count_words(subreddit, word_list, after=None, word_count={}):
    """
    Prints a sorted count of given kwywords
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    word_list_lower = [word.lower() for word in word_list]

    if after:
        url += "&after={}".format(after)

    headers = {"User-Agent": "My-App/0.0.3"}
    r = requests.get(url, headers=headers)
    result = r.json()

    if "error" in result or r.status_code != 200:
        return ()
    hot_data = result["data"]["children"]
    if not hot_data or len(hot_data) == 0:
        if word_count and len(word_count) > 0:
            return (word_count)
        return ()
    for q in hot_data:
        words = q["data"]["title"].split(' ')
        for word in words:
            if word.lower() in word_list_lower:
                if not word.lower() in word_count:
                    word_count[word.lower()] = 0
                word_count[word.lower()] += 1
    new_after = result["data"]["after"]
    count_words(subreddit, word_list, new_after, word_count)
