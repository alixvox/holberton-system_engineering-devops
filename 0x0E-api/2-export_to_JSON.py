#!/usr/bin/python3
""" This module saves information about
an employee's TODO list progress to a CSV file. """

import requests
import sys
import json


if __name__ == '__main__':

    # check that arg passed is an int
    if sys.argv[1].isdigit:
        id = sys.argv[1]
        user = requests.get(
            "https://jsonplaceholder.typicode.com/users/{}"
            .format(id)).json()
        todo = requests.get(
            "https://jsonplaceholder.typicode.com/todos/?userId={}"
            .format(id)).json()
        completed = []
        for x in todo:
            if x.get("completed") is True:
                completed.append(x.get("title"))

        # print information to output #
        print("Employee {} is done with tasks ({}/{}):".format(
            user.get("name"), len(completed), len(to_do)))
        for title in completed:
            print("\t {}".format(title))

        # save info to a json file
        with open("{}.json".format(id), 'w') as file:
            tasks = {id: [{
                'task': x.get('title'),
                'username': user.get('username'),
                'completed': x.get('completed')}
                for x in todo]}
            json.dump(tasks, file)
