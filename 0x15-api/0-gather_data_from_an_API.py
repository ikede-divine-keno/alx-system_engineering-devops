#!/usr/bin/python3
"""Write a Python script that, using this REST API, for a given
employee ID, returns information about his/her TODO list progress."""
import requests
from sys import argv


if __name__ == "__main__":
    num = 0
    comt = []
    tasks = requests.get(
        "https://jsonplaceholder.typicode.com/todos",
        params={"userId": "{}".format(argv[1])},
    )
    todos = tasks.json()
    for to in todos:
        if to.get("completed"):
            comt.append(to.get("title"))
            num += 1
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])
    )
    user_data = dict(response.json())
    print(
        "Employee {} is done with tasks({}/{}):".format(
            user_data.get("name"), num, len(todos)
        )
    )
    [print("\t {}".format(com)) for com in comt]
