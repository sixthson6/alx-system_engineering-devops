#!/usr/bin/python3
"""Exports todo list information of all employees
    to JSON format
"""

if __name__ == "__main__":
    import json
    import requests
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()

    with open("todo_all_employees.json", "w", encoding="utf-8") as jsonfile:
        json.dump({
            u.get("id"): [{
                "username": u.get("username"),
                "task": t.get("title"),
                "completed": t.get("completed")
            } for t in requests.get(url + "todos",
                                    params={"userId": u.get("id")}).json()]
            for u in users}, jsonfile)
