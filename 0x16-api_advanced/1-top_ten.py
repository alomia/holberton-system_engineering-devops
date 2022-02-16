#!/usr/bin/python3
"""import requests"""
import requests


def top_ten(subreddit):
    """prints the titles of the 10 hottest posts on a given subreddit"""
    limit = 10
    try:
        url = 'https://www.reddit.com/r/{subreddit}/hot.json?limit={l}'.format(
            subreddit=subreddit, l=limit)
        request = requests.get(
            url, headers={'User-agent': 'MyHolbertonAPI/0.0.1'})
        r = request.json()['data']
        [print(value['data']['title']) for value in r['children']]
    except(Exception):
        print('None')

