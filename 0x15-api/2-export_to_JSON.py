#!/usr/bin/python3
"""
For a given employee ID, returns information about
their TODO list progress and exports it to a JSON file.
"""

import json
import requests
import sys


def employee_todo_progress(employee_id):
    """Fetches TODO progress for a given employee ID & write it to JSON file"""
    user = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    ).json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()

    tasks = [task for task in todos if task["userId"] == int(employee_id)]

    task_list = []
    for task in tasks:
        task_dict = {}
        task_dict["task"] = task["title"]
        task_dict["completed"] = task["completed"]
        task_dict["username"] = user["username"]
        task_list.append(task_dict)

    with open(f"{employee_id}.json", "w") as jsonfile:
        json.dump({employee_id: task_list}, jsonfile, indent=2)


if _name_ == "_main_":
    employee_todo_progress(sys.argv[1])
