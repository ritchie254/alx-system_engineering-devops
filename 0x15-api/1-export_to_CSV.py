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
        todos = list(filter(lambda x: x.get('userId') == id, req.json()))
        file_name = "{}.csv".format(id)
        with open(file_name, "w") as file:
            for i in todos:
                file.write(
                        '"{}","{}","{}","{}"\n'.format(
                            id,
                            user.get("username"),
                            i.get("completed"),
                            i.get("title")
                            )
                        )
