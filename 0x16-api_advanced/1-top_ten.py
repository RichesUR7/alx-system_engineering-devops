i#!/usr/bin/python3
"""
This module contains a function that queries the Reddit API to fetch
the titles of the first 10 hot posts listed for a given subreddit.

If the subreddit is invalid or does not exist, the function prints None.
"""

import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts listed for a given subreddit

    Parameters:
    subreddit (str): The name of the subreddit.

    Returns:
    None
    """
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) "
            "Gecko/20100101 Firefox/124.0"
        )
    }
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    response = requests.get(
        url,
        headers=headers,
        allow_redirects=False,
    )

    if response.status_code == 200:
        posts = response.json()["data"]["children"]
        for post in posts:
            print(post["data"]["title"])
    else:
        print(None)i#!/usr/bin/python3
"""
This module contains a function that queries the Reddit API to fetch
the titles of the first 10 hot posts listed for a given subreddit.

If the subreddit is invalid or does not exist, the function prints None.
"""

import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts listed for a given subreddit

    Parameters:
    subreddit (str): The name of the subreddit.

    Returns:
    None
    """
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) "
            "Gecko/20100101 Firefox/124.0"
        )
    }
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    response = requests.get(
        url,
        headers=headers,
        allow_redirects=False,
    )

    if response.status_code == 200:
        posts = response.json()["data"]["children"]
        for post in posts:
            print(post["data"]["title"])
    else:
        print(None)
