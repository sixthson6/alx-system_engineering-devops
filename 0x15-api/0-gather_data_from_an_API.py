#!/usr/bin/python3
""" Contains script to return employee
todo list progress from an api
"""
if __name__ == "__main__":
    import requests
    import sys


    r = requests.get('https://jsonplaceholder.typicode.com/todos/')
    em_name = requests.get('https://jsonplaceholder.typicode.com/users/')
    if r.status_code == 200 and em_name.status_code == 200:
        data = r.json()
        id = int(sys.argv[1])
        name = em_name.json()
        count = 0
        for item in data:
            if item['userId'] == id and item['completed'] == True:
                count += 1
        for n in name:
            if n['id'] == id:
                employee_name = n['name']
       
        print("Employee {} is done with tasks({}/20)".format(employee_name, count))
        for item in data:
            if item['userId'] == id and item['completed'] == True:   
                print("\t{}".format(item['title']))
