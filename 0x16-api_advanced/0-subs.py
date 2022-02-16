import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers  for a given subreddit"""
    try:
        url = 'https://www.reddit.com/r/{subreddit}/about.json'.format(subreddit = subreddit)
        response = requests.get(url, headers={'User-agent':
                                'MyHOlbertonAPI/0.0.1'})
        data = response.json()['data']['subscribers']
        return data
    except(Exception):
        return 0
