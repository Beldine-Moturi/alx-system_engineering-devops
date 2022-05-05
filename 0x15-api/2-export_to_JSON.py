#!/usr/bin/python3
"""
uses a REST API and for a given employee ID and
stores information abou them in a json file
"""

if __name__ == "__main__":
    import json
    import requests
    import sys

    API = "https://jsonplaceholder.typicode.com"
    """REST API url"""

    id = sys.argv[1]
    user = requests.get('{}/users/{}'.format(API, id)).json()
    tasks = requests.get('{}/users/{}/todos'.format(API, id)).json()

    task_list = []
    for task in tasks:
        t = {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": user.get("username")
        }
        task_list.append(t)

    json_list = {id: task_list}
    with open("{}.json".format(id), "w") as f:
        json.dump(json_list, f)
