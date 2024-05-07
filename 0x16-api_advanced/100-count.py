#!/usr/bin/python3
"""
This module contains a function that queries the Reddit API to fetch
the titles of all hot posts for the given subreddit, recursively handling
pagination and counting the occurrence of given keywords in the title

If subreddit not valid prints nothing.
"""


from collections import Counter
import re
import requests
import sys


def count_words(subreddit, word_list, hot_list=[], after=None):
    """
    Fetch the titles for all hot posts for a given subreddit
    and count the occurrence of given keywords
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
        count_words(subreddit, word_list, hot_list, data["after"])
    else:
        word_count = Counter(
            word
            for title in hot_list
            for word in re.findall(r"\b\w+\b", title.lower())
            if word in word_list
        )
        for word, count in sorted(
            ((word, word_count[word]) for word in word_list
                if word_count[word]),
            key=lambda x: (-x[1], x[0]),
        ):
            print("{}: {}".format(word, count))


if __name__ == "__main__":
    word_list = [word.lower() for word in sys.argv[2].split()]
    count_words(sys.argv[1], word_list)
