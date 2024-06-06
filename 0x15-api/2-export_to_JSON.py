#!/usr/bin/python3
"""Contains script to export data in JSON
format, retrieved from an api
"""
if __name__ == "__main__":
    import requests
    import json
    import sys

    # Get ID
    id = int(sys.argv[1])
    file = "{}.json".format(id)

    # Get username
    em_name = requests.get('https://jsonplaceholder.typicode.com/users/')
    if em_name.status_code == 200:
        name = em_name.json()
        employee_name = None
        for n in name:
            if n['id'] == id:
                username = n['username']

    # Get Todos
    r = requests.get('https://jsonplaceholder.typicode.com/todos/', params={"userId": id}).json()

    # Write to file as json
    with open(file, 'w', newline='', encoding='utf-8') as f:
        json.dump({id: [{
            "task": t.get("title"),
            "completed": t.get("completed"),
            "username": username
            } for t in r]}, f)
    

