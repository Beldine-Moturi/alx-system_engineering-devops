#!/usr/bin/python3
"""Defines function to query first 10 hot posts for a subreddit"""
import requests


def top_ten(subreddit):
    """prints titles of the first 10 hot posts listed for a given subreddit."""
    sub = subreddit
    tf = "all"
    lim = 10

    base_url = f'https://www.reddit.com/r/{sub}/hot.json?limit={lim}&t={tf}'
    request = requests.get(
        base_url,
        headers={'User-agent': 'MyBot'},
        allow_redirects=False
    )
    if request.status_code == 404:
        print("None")
        return
    r = request.json()
    [print(p.get('data').get('title')) for p in r.get('data').get('children')]
