#!/usr/bin/python3
""" This module returns information about
an employee's TODO list progress. """

import requests, sys


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

        # print employee info
        print("Employee {} is done with tasks({}/{}):".format(
            user.get("name"), len(completed), len(todo)))
        for title in completed:
            print("\t {}".format(title))
