#!/usr/bin/python3
"""
2. Export to JSON
"""

import json
import requests as reqs
from sys import argv


def run():
    """ Export to Json"""
    u_id = argv[1]
    url = 'https://jsonplaceholder.typicode.com/'
    tasks = reqs.get(url + 'todos?userId={}'.format(u_id)).json()
    user = reqs.get(url + 'users/{}'.format(u_id)).json()

    tasks_list = [{"task": task.get('title'),
                   "completed": task.get('completed'),
                   "username": user.get('username')} for task in tasks]

    filename = u_id + '.json'
    with open(filename, 'w', newline='') as jsonfile:
        json.dump({u_id: tasks_list}, jsonfile)


if __name__ == "__main__":
    run()
