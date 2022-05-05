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
        base_url = f'https://www.reddit.com/r/{subreddit}/about.json?t={timeframe}'
        request = requests.get(
            base_url,
            headers={'User-agent': 'MyBot'},
            allow_redirects=False
        )
    except Exception as e:
        print("An error occured!:")
        print(e)
    return request.json()['data']['subscribers']

if len(sys.argv) < 2:
    print("Please pass an argument for the subreddit to search.")
else:
    print("{:d}".format(number_of_subscribers(sys.argv[1])))
