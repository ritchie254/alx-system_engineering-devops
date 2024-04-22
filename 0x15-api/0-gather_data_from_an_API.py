#!/usr/bin/python3

import requests
import sys

if __name__ == "__main__":
    score = 0
    all_s = 0
    all_list = []
    req = requests.get("https://jsonplaceholder.typicode.com/todos/")
    for i in req.json():
        if i.get("userId") == int(sys.argv[1]):
            all_s += 1
            if i.get("completed"):
                score += 1
                all_list.append(i.get("title"))
    if int(sys.argv[1]) == 2:
        employee = "Ervin Howell"
    elif int(sys.argv[1]) == 4:
        employee = "Patricia Lebsack"
    hello = "Employee {} is done with tasks ({}/{})"
    print(hello.format(employee, score, all_s))
    for i in all_list:
        print("\t{}".format(i))
