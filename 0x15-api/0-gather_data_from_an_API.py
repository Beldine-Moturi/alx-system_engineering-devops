#!/usr/bin/python3
"""uses a REST API and for a given employee ID, returns information
about his/her TODO list progress."""
import requests
import sys


API = 'https://jsonplaceholder.typicode.com'


if __name__ == "__main__":
    id = sys.argv[1]
    user = requests.get('{}/users/{}'.format(API, id)).json()
    tasks = requests.get('{}/users/{}/todos'.format(API, id)).json()
    completed = list(filter(lambda x: x.get('completed'), tasks))

    print(
        "Employee {} is done with tasks {}/{}:".format(
            user.get('name'),
            len(completed),
            len(tasks)
        )
    )
    for task in completed:
        print("\t {}".format(task.get('title')))
