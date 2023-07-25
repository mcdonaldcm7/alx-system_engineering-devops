#!/usr/bin/python3
"""Returns information about the TODO list progress for a given employee ID"""
import json
import requests
import sys


if __name__ == "__main__":
    param = sys.argv[1] if len(sys.argv) == 2 else ""
    todo_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
            param)
    users_url = "https://jsonplaceholder.typicode.com/users"
    users = requests.get(users_url)
    todos = requests.get(todo_url)

    username = ""
    tasks = []
    todo_all = todos.json()

    for user in users.json():
        if user["id"] == (int)(param):
            username = user["username"]
    for task in todo_all:
        tmp_task = {}
        tmp_task["task"] = task["title"]
        tmp_task["completed"] = task["completed"]
        tmp_task["username"] = username
        tasks.append(tmp_task)

    file_name = "{}.json".format(param)

    with open(file_name, 'w') as file:
        json.dump({"{}".format(param): tasks}, file)
