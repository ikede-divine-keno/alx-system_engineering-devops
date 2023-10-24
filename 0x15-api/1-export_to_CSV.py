#!/usr/bin/python3
"""Write a Python script that, using this REST API, for a given
employee ID, returns information about his/her TODO list progress."""
import csv
import requests
from sys import argv


if __name__ == "__main__":
    tasks = requests.get("https://jsonplaceholder.typicode.com/todos")
    todos = tasks.json()
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])
    )
    user_ = response.json()
    with open("{}.csv".format(user_.get("id")), "w", newline="") as csvfile:
        writer = csv.writer(
            csvfile, quoting=csv.QUOTE_ALL, quotechar='"', lineterminator="\n"
        )
        for to in todos:
            if int(argv[1]) == to.get("userId"):
                writer.writerow(
                    [
                        user_.get("id"),
                        user_.get("username"),
                        str(to.get("completed")),
                        to.get("title"),
                    ]
                )
