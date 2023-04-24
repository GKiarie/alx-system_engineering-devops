#!/usr/bin/python3
"""
script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress
exports data to JSON format
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    user_id = argv[1]
    user = requests.get(url + "users/{}".format(user_id)).json()
    todos = requests.get(url + "todos", params={"userId": user_id}).json()
    file_name = user_id + ".json"
    task_list = []
    for todo in todos:
        j_dict = {
                "task": todo["title"],
                "completed": todo["completed"],
                "username": user["username"]}
        task_list.append(j_dict)

    with open(file_name, 'w') as json_file:
        json.dump({user_id: task_list}, json_file)
