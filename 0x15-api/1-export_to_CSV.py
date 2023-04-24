#!/usr/bin/python3
"""
script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress
exports data in the CSV format
"""
import csv
import requests
from sys import argv


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    user_id = argv[1]
    user = requests.get(url + "users/{}".format(user_id)).json()
    todos = requests.get(url + "todos", params={"userId": user_id}).json()
    file_name = user_id + ".csv"

    with open(file_name, 'w') as csvfile:
        for todo in todos:
            csvfile.write('"{}","{}","{}","{}"\n'.format(
                user_id, user["username"], todo["completed"], todo["title"]))
