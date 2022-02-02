#!/usr/bin/python3
"""
Dictionary of list of dictionaries
"""
import json
import requests as reqs
from sys import argv


def run():
    """ Dics into dic to Json"""
    url = 'https://jsonplaceholder.typicode.com/'
    tasks = reqs.get(url + 'todos/').json()
    users = reqs.get(url + 'users/').json()

    new_dict = {}
    for user in users:
        u_id = user.get('id')
        task_list = [{"username": user.get('username'),
                      "task": task.get('title'),
                      "completed": task.get('completed')
                      } for task in tasks if u_id == task.get('userId')]
        new_dict[u_id] = task_list

    filename = 'todo_all_employees.json'
    with open(filename, 'w', newline='') as jsonfile:
        json.dump(new_dict, jsonfile)


if __name__ == "__main__":
    run()
