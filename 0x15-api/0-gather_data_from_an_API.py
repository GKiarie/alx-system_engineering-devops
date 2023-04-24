#!/usr/bin/python3
"""
script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""
import requests
from sys import argv


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    user = requests.get(url + "users/{}".format(argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": argv[1]}).json()
    complete = []
    for todo in todos:
        if todo.get('completed') is True:
            complete.append(todo.get('title'))
    print("Employee {} is done with tasks({}/{}):".format(
        user["name"], len(complete), len(todos)))
    for task in complete:
        print("\t {}".format(task))
