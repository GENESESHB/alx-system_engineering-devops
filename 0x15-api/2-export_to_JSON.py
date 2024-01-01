#!/usr/bin/python3
""" This is an extended version of Python script #0
    to export data in the JSON format.
    Requirements:
        - Records all tasks that are owned by this employee.
        - Format must be: { "USER_ID": [{"task": "TASK_TITLE",
          "completed": TASK_COMPLETED_STATUS,
          "username": "USERNAME"},
          {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS,
          "username": "USERNAME"}, ... ]}.
        - File name must be: USER_ID.json.
"""

import json
from os import sys
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]
    usrname = (requests.get(f"{url}users/{user_id}").json().get("username"))
    todos = list(requests.get(f"{url}user/{user_id}/todos").json())
    all_data = {}
    user_data = []

    for task in todos:
        task_data = {"task": task['title'], "completed": task['completed'],
                     "username": usrname}
        user_data.append(task_data)

    all_data[user_id] = user_data
    json_filename = f"{user_id}.json"
    with open(json_filename, 'w') as f:
        json.dump(all_data, f)
