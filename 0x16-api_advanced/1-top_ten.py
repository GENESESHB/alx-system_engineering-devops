#!/usr/bin/python3
""" top_ten model """
import requests


def top_ten(subreddit):
    """ a function that queries the Reddit API and prints
    the titles of the first 10 hot posts listed for
    a given subreddit."""
    if not subreddit:
        return None

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "0x16. API advanced/Task0"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        posts = data.get('data', {}).get('children', [])
        if posts:
            for post in posts:
                print(post.get('data').get('title'))
        else:
            print(None)
    else:
        print(None)
