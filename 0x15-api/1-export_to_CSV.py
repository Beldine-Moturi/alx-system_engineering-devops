#!/usr/bin/python3
"""
uses a REST API and for a given employee ID, returns information
about his/her TODO list progress.
"""


if __name__ == "__main__":
    import csv
    import requests
    import sys

    API = 'https://jsonplaceholder.typicode.com'
    id = sys.argv[1]
    user = requests.get('{}/users/{}'.format(API, id)).json()
    tasks = requests.get('{}/users/{}/todos'.format(API, id)).json()

    with open(f'{id}.csv', 'w', newline='') as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["userId", "username", "completed", "title"],
            quoting=csv.QUOTE_ALL
        )
        for task in tasks:
            writer.writerow({
                "userId": id,
                "username": user.get('name'),
                "completed": task.get('completed'),
                "title": task.get('title')
            })
