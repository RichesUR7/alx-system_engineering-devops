#!/usr/bin/python3
"""
For all employees, returns information about
their TODO list progress and exports it to a JSON file.
"""

import json
import requests


def all_employees_todo_progress():
    """Fetches TODO progress for all employees and writes it to a JSON file."""
    users = requests.get(
        "https://jsonplaceholder.typicode.com/users"
    ).json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()

    user_tasks = {}

    for user in users:
        tasks = [task for task in todos if task["userId"] == user["id"]]
        task_list = []
        for task in tasks:
            task_dict = {}
            task_dict["username"] = user['username']
            task_dict["task"] = task['title']
            task_dict["completed"] = task['completed']
            task_list.append(task_dict)
        user_tasks[user["id"]] = task_list

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(user_tasks, jsonfile, indent=2)


if _name_ == "_main_":
    all_employees_todo_progress()
