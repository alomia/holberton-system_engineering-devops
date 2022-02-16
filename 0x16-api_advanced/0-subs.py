#!/usr/bin/python3
"""import requests"""
import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers  for a given subreddit"""
    try:
        url = 'https://www.reddit.com/r/{subreddit}/about.json'.format(
            subreddit=subreddit)
        request = requests.get(
            url, headers={'User-agent': 'MyHolbertonAPI/0.0.1'})
        r = request.json()['data']['subscribers']
        return r
    except(Exception):
        return(0)
