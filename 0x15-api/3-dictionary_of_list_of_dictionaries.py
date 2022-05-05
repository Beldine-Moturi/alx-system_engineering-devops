#!/usr/bin/python3
"""
uses a REST API to fetch data and
stores information in a json file
"""

if __name__ == "__main__":
    import json
    import requests
    import sys

    API = "https://jsonplaceholder.typicode.com"
    """REST API url"""

    users = requests.get('{}/users'.format(API)).json()
    json_list = {}
    for user in users:
        tasks = requests.get(
            '{}/users/{}/todos'.format(API, user.get('id'))).json()
        task_list = []
        for task in tasks:
            t = {
                "username": user.get("username"),
                "task": task.get("title"),
                "completed": task.get("completed")
            }
            task_list.append(t)
        json_list[user.get("id")] = task_list
    with open("todo_all_employees.json", "w") as f:
        json.dump(json_list, f)
