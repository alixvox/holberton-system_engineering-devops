#!/usr/bin/python3
""" This module saves information about
an employee's TODO list progress to a CSV file. """

import requests
import sys
import csv


if __name__ == '__main__':

    # check that arg passed is an int #
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
                    user.get("name"), len(completed), len(todo)))
                for title in completed:
                    print("\t {}".format(title))

        # save info to a csv file #
        with open("{}.csv".format(id), 'w') as file:
            csv = csv.writer(file, quoting=csv.QUOTE_ALL)
            for x in todo:
                csv.writerow([
                    id, user.get("username"),
                    x.get("completed"), x.get("title")])
