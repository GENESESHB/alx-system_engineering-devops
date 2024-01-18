#!/usr/bin/python3
""" a function that queries the Reddit API and returns
    the number of subscribers."""
import requests


def number_of_subscribers(subreddit):
    """ it returns the number of subscribers
        (not active users, total subscribers)
        for a given subreddit. If an invalid subreddit is given,
        the function should return 0. """
    if subreddit is None:
        return 0
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "0x16. API advanced/Task0"}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        try:
            data = response.json()
            return data['data']['subscribers']
        except KeyError:
            return 0
    return 0
