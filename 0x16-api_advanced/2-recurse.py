#!/usr/bin/python3
"""import requests"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(
        subreddit, after)
    header = {'User-Agent': 'my-app/0.0.1'}
    request = requests.get(url, allow_redirects=False, headers=header)
    if request.status_code != 200:
        return None
    else:
        data = request.json()['data']
        after = data['after']
        for child in data['children']:
            hot_list.append(child['data']['title'])
        if after is None:
            return hot_list
        return recurse(subreddit, hot_list, after)
