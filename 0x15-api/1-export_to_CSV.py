#!/usr/bin/python3
"""
Returns information about the TODO list progress for a given employee ID
and exports data in the CSV format
"""
import csv
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
    tasks = []
    todo_all = todos.json()

    for user in users.json():
        if user["id"] == (int)(param):
            name = user["username"]
    for task in todo_all:
        tmp_list = [param, name, task["completed"], task["title"]]
        tasks.append(tmp_list)

    file_name = "{}.csv".format(param)

    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        writer.writerows(tasks)
