#!/usr/bin/python3

import requests
import sys

api = "https://jsonplaceholder.typicode.com"
if __name__ == "__main__":
    score = 0
    id = int(sys.argv[1])
    all_s = 0
    all_list = []
    req = requests.get("{}/todos/".format(api))
    user = requests.get("{}/users/{}".format(api, id)).json()
    if len(sys.argv) > 1:
        for i in req.json():
            if i.get("userId") == id:
                all_s += 1
                if i.get("completed"):
                    score += 1
                    all_list.append(i.get("title"))
    hello = "Employee {} is done with tasks ({}/{})"
    print(hello.format(user.get("name"), score, all_s))
    for i in all_list:
        print("\t{}".format(i))
