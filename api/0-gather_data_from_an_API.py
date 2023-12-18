#!/usr/bin/python3
""" my first api """
import sys
import requests
import json
if __name__ == "__main__":
    todos_api = requests.get(
        'https://jsonplaceholder.typicode.com/todos/')
    user_api = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(sys.argv[1]))
    todo_data = todos_api.text
    user_data = user_api.text
    user = json.loads(user_data)
    todo = json.loads(todo_data)
    count = 0
    completed_tasks = []
    for i in todo:
        if i['userId'] == user['id']:
            if i['completed']:
                completed_tasks.append(i)
            count += 1
    print(
        'Employee {} is done with tasks({}/{}):'
        .format(user['name'], len(completed_tasks), count))
    for i in completed_tasks:
        print('\t {}'.format(i['title']))
