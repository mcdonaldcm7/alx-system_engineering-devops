#!/usr/bin/python3
"""Returns information about the TODO list progress for a given employee ID"""
import json
import requests
import sys


if __name__ == "__main__":
    todo_url = "https://jsonplaceholder.typicode.com/todos"
    users_url = "https://jsonplaceholder.typicode.com/users"
    users = requests.get(users_url)
    todos = requests.get(todo_url)

    users_stats = {}

    for user in users.json():
        tasks = []
        for task in todos.json():
            if task["userId"] == user["id"]:
                tmp_task = {}
                tmp_task["username"] = user["username"]
                tmp_task["task"] = task["title"]
                tmp_task["completed"] = task["completed"]
                tasks.append(tmp_task)
        users_stats[user["id"]] = tasks

    file_name = "todo_all_employees.json"

    with open(file_name, 'w') as file:
        json.dump(users_stats, file)
