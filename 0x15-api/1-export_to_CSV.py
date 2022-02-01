#!/usr/bin/python3
"""
1. Export to CSV
"""
import csv
import requests as reqs
from sys import argv


def run():
    """ Export data to CSV """
    u_id = argv[1]

    url = 'https://jsonplaceholder.typicode.com/'
    tasks = reqs.get(url + 'todos?userId={}'.format(u_id)).json()
    user = reqs.get(url + 'users/{}'.format(u_id)).json()

    csv_inf = []
    for iter in tasks:
        csv_inf.append([u_id,
                        user.get('username'),
                        iter.get('completed'),
                        iter.get('title')])

    filename = u_id + '.csv'
    with open(filename, 'w', newline='') as csv_file:
        r = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_ALL)
        r.writerows(csv_inf)


if __name__ == "__main__":
    run()
