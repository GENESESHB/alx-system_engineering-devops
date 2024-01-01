#!/usr/bin/python3
"""
python script that can use REST API 
for give ass the id return information about progress
"""

from os import sys
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    name = (requests.get(f"{url}users/{sys.argv[1]}").json().get("name"))
    todos = (requests.get(f"{url}user/{sys.argv[1]}/todos").json())
    total_tasks = len(todos)
    done_tasks = []
    done = 0
    for tasks in todos:
        if tasks.get("completed"):
            done += 1
            done_tasks.append(tasks)
    print(f"Employee {name} is done with tasks({done}/{total_tasks}):")
    for item in done_tasks:
        print(f"\t {item['title']}")
