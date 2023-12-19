#!/usr/bin/python3
"""
Model to make a request to an
API and retrieve data
"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    URL = "https://jsonplaceholder.typicode.com/"
    user_id = int(argv[1])

    user_req = requests.get(f"{URL}/users/{user_id}")
    data = user_req.json()
    user_name = data.get("name")

    todos = requests.get(f"{URL}/todos/")
    todos_data = todos.json()

    completed_todos = []
    total_todos = 0
    for todo in todos_data:
        if todo.get("userId") == user_id:
            total_todos += 1
            if todo.get("completed") is True:
                completed_todos.append(todo)

    print(f"Employee {user_name} is done", end="")
    print(f" with tasks({len(completed_todos)}/{total_todos}):")
    for todo in completed_todos:
        print(f"\t {todo['title']}")
