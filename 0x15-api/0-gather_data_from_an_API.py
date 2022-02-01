#!/usr/bin/python3
"""
Gather data from an API
"""
import requests as reqs
from sys import argv


def run():
        """ Return users by tasks completed successfully"""
        u_id = argv[1]
        url = 'https://jsonplaceholder.typicode.com/'
        tasks = reqs.get(url + 'todos?userId={}'.format(u_id)).json()
        user = reqs.get(url + 'users/{}'.format(u_id)).json()

        tasks_completed = []
        for iter in tasks:
                if iter.get('completed') is True:
                        tasks_completed.append(iter.get('title'))
        print('Employee {} is done with tasks({}/{}): '.format(user.get('name'),
                len(tasks_completed), len(tasks)))

        for iter in tasks_completed:
                print('\t {}'.format(iter))

if __name__ == "__main__":
    run()
