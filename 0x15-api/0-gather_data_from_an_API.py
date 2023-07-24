#!/usr/bin/python3
"""Returns information about the TODO list progress for a given employee ID"""
import requests
import sys


if __name__ == "__main__":
    param = sys.argv[1] if len(sys.argv) == 2 else ""
    todo_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
            param)
    users_url = "https://jsonplaceholder.typicode.com/users"
    users = requests.get(users_url)
    todos = requests.get(todo_url)

    name = ""
    tasks_done = []
    todo_all = todos.json()

    for user in users.json():
        if user["id"] == (int)(param):
            name = user["name"]
    for task in todo_all:
        if task["completed"]:
            tasks_done.append(task["title"])
    print("Employee {} is done with tasks({}/{}):".format(
        name, len(tasks_done), len(todo_all)))
    for task in tasks_done:
        print("\t {}".format(task))
