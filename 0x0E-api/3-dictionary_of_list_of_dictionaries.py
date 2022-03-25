#!/usr/bin/python3
""" This module saves information about all
employees' TODO list progress to a CSV file. """

import requests
import json


if __name__ == '__main__':

    users = requests.get(
        "https://jsonplaceholder.typicode.com/users").json()
    todos = requests.get(
        "https://jsonplaceholder.typicode.com/todos").json()

    # save info to a json file
    with open("todo_all_employees.json", 'w') as file:
        todos_dict = {user.get('id'): [{
                'task': x.get('title'),
                'username': user.get('username'),
                'completed': x.get('completed')
            } for x in todos if user.get('id') == x.get('userID')
            ] for user in users}
        json.dump(todos_dict, file)
