#!/usr/bin/python3
""" Defines a function that fetches a list containing the titles
    of all hot articles for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """ Returns a list of all hot articles
    Args:
        subreddit (str): The subreddit to query
        hot_list (list): the list to append to
    Returns:
        - The number of hot articles in a subreddit
        - 0 if the 'subreddit' is invalid.
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=100&t=all'
    if after:
        url += f'&after={after}'
    result = requests.get(
        url,
        headers={'User-agent': 'MyBot'},
        allow_redirects=False
    )
    if result.status_code != 200:
        return None
    result = result.json()
    posts = result.get('data').get('children')
    for post in posts:
        hot_list.append(post.get('data').get('title'))
    after_param = result.get('data').get('after')
    if after_param:
        return recurse(
            subreddit,
            hot_list=hot_list,
            after=after_param
        )
    return hot_list
