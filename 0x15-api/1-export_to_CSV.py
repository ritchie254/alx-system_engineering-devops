#!/usr/bin/python3
"""
script to fetch api information
"""

import requests
import sys

api = "https://jsonplaceholder.typicode.com"
"""api url"""


if __name__ == "__main__":
    all_list = []
    if len(sys.argv) > 1:
        id = int(sys.argv[1])
        req = requests.get("{}/todos/".format(api))
        user = requests.get("{}/users/{}".format(api, id)).json()
        file_name = "{}.csv".format(id)
        for i in req.json():
            if i.get("userId") == id:
                name = user.get("name")
                task = i.get("completed")
                title = i.get("title")
                new = '"{}","{}","{}","{}"\n'
                with open(file_name, "a") as file:
                    file.write(new.format(id, name, task, title))
