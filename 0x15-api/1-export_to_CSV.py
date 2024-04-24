#!/usr/bin/python3
"""
For a given employee ID, returns information about
their TODO list progress and exports it to a CSV file.
"""

import csv
import requests
import sys


def employee_todo_progress(employee_id):
    """Fetches TODO progress for a given employee ID & writes it to CSV file"""
    user = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    ).json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()

    tasks = [task for task in todos if task["userId"] == int(employee_id)]

    with open(f"{employee_id}.csv", "w", newline="") as csvfile:
        taskwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in tasks:
            taskwriter.writerow(
                [
                    employee_id,
                    user["username"],
                    task["completed"],
                    task["title"]
                    ]
            )


if _name_ == "_main_":
    employee_todo_progress(sys.argv[1])
