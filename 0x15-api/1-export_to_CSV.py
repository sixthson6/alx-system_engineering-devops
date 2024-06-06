#!/usr/bin/python3
""" Contains script to return employee
todo list progress from an api
"""
if __name__ == "__main__":
    import requests
    import sys
    import csv

    # Get ID
    i = int(sys.argv[1])
    id = "{}.csv".format(i)

    # Create new csv file
    f = open(id, 'w', newline='', encoding='utf-8')

    # Create writer object
    c = csv.writer(f, quoting=csv.QUOTE_ALL)

    # Define the rows
    # c.writerow( ["USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"] )

    # Write to csv file
    r = requests.get('https://jsonplaceholder.typicode.com/todos/')
    em_name = requests.get('https://jsonplaceholder.typicode.com/users/')
    if r.status_code == 200 and em_name.status_code == 200:
        data = r.json()
        name = em_name.json()
        employee_name = None
        for n in name:
            if n['id'] == i:
                employee_name = n['name']
        for item in data:
            if item['userId'] == i:
                row = [item['userId'], employee_name,
                       item['completed'], item['title']]
                c.writerow(row)
    # Close file
    f.close()
