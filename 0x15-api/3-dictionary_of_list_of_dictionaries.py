#!/usr/bin/python3
"""
script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress
exports data to dictionary
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    users = requests.get(url + "users").json()
    file_name = "todo_all_employees.json"

    with open(file_name, "w") as json_file:
        json.dump({
            user["id"]: [{
                "username": user["username"],
                "task": todo["title"],
                "completed": todo["completed"]
            } for todo in requests.get(url + "todos",
                                       params={"userId": user["id"]}).json()]
            for user in users}, json_file)
