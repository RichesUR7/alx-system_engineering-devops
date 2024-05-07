#!/usr/bin/python3
"""
This module contains a function that queries the Reddit API to fetch
the titles of all hot posts for the given subreddit, recursivley handling
pagenations

If subreddit not valid returns None.
"""


import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Fetch the titles for all hot posts for a given subreddit
    """
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) "
            "Gecko/20100101 Firefox/124.0"
        )
    }
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    if after:
        url += "?after={}".format(after)
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json()["data"]
    hot_list.extend([post["data"]["title"] for post in data["children"]])

    if data["after"] is not None:
        return recurse(subreddit, hot_list, data["after"])
    else:
        return hot_list
