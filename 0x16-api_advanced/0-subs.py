#!/usr/bin/python3
"""Defines a function that queries the Reddit API and returns
the number of subscribers for a given subreddit."""
import requests
import sys


def number_of_subscribers(subreddit):
    """Queries the Reddit API"""
    try:
        timeframe = 'all'
        limit = ''
        base_url = f'https://www.reddit.com/r/{subreddit}/about.json?\
t={timeframe}'
        request = requests.get(
            base_url,
            headers={'User-agent': 'MyBot'},
            allow_redirects=False
        )
    if 'error' in request.json().keys():
        return 0
    return request.json()['data']['subscribers']
