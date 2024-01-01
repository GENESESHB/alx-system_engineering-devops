#!/usr/bin/python3
"""  this an extended version of Python script #0
    to export data in the CSV format.
    Requirements:
        - Records all tasks that are owned by this employee.
        - Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS",
        "TASK_TITLE".
        - File name must be: USER_ID.csv.
"""

import csv
from os import sys
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]
    usrname = (requests.get(f"{url}users/{user_id}").json().get("username"))
    todos = (requests.get(f"{url}user/{user_id}/todos").json())
    tasks = list(todos)

    csv_filename = f"{user_id}.csv"
    with open(csv_filename, "w") as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in tasks:
            csv_writer.writerow([user_id, usrname,
                                task['completed'],
                                task['title']])
