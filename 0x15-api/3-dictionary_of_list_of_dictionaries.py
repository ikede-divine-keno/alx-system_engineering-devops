#!/usr/bin/python3
"""Write a Python script that, using this REST API, for a given
employee ID, returns information about his/her TODO list progress."""
import json
import requests


if __name__ == "__main__":
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    users = response.json()
    all_users = {}
    for user in users:
        tasks = requests.get(
            "https://jsonplaceholder.typicode.com/todos",
            params={"userId": "{}".format(user.get("id"))},
        )
        todos = tasks.json()
        fd = [
            {
                "username": user.get("username"),
                "task": to.get("title"),
                "completed": to.get("completed"),
            }
            for to in todos
        ]
        all_users[user.get("id")] = fd

    with open("todo_all_employees.json", "w", encoding="utf-8") as f:
        json.dump(all_users, f)
