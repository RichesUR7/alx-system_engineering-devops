#!/usr/bin/python3
"""
For a given employee ID, returns information about
their TODO list progress.
"""

import requests
import sys


def employee_todo_progress(employee_id):
    """Fetches TODO progress for a given employee ID."""
    user = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    ).json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()

    tasks = [task for task in todos if task["userId"] == int(employee_id)]
    completed_tasks = [task for task in tasks if task["completed"]]

    print(
        f"Employee {user['name']} is done "
        f"with tasks({len(completed_tasks)}/{len(tasks)}):"
    )
    for task in completed_tasks:
        print(f"\t {task['title']}")


if _name_ == "_main_":
    employee_todo_progress(sys.argv[1])
