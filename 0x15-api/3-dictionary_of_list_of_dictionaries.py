#!/usr/bin/python3
""" This is an extended version of Python script #0
    to export data in the JSON format.
    Requirements:
        - Records all tasks from all employees.
        - Format must be: { "USER_ID": [ {"username": "USERNAME",
          "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS},
          {"username": "USERNAME", "task": "TASK_TITLE",
          "completed": TASK_COMPLETED_STATUS}, ... ],
          "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE",
          "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME",
          "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ]}.
        - File name must be: todo_all_employees.json  .
"""

import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = (requests.get(f"{url}users").json())
    all_data = {}
    user_data = []

    for user in users:
        user_id = user["id"]
        todos = list(requests.get(f"{url}user/{user['id']}/todos").json())
        for task in todos:
            task_data = {"username": user["username"], "task": task['title'],
                         "completed": task['completed']}
            user_data.append(task_data)
        all_data[user_id] = user_data
        user_data = []
    json_filename = "todo_all_employees.json"
    with open(json_filename, 'w') as f:
        json.dump(all_data, f)
