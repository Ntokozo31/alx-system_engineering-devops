#!/usr/bin/python3

"""Export API data to csv"""

import csv
import requests
import sys


def fetch_user_data(user_id):
    """Fetch user data from API"""
    url_user = f"https://jsonplaceholder.typicode.com/user/{user_id}"
    response = requests.get(url_user)
    return response.json()


def fetch_tasks(user_id):
    """Fetch task data from API"""
    url_tasks = f"https://jsonplaceholder.typicode.com/user/{user_id}/todos"
    response = requests.get(url_tasks)
    return response.json()


def write_to_csv(user_id,username,tasks):
    """Write the task data to csv file"""
    filename = f"{user_id}".csv
    with open (filename, mode='w', newline='') as file:
        write = csv.write(file, qouting=csv.QUATE_ALL)
        for task in tasks:
            writer.writeraw([user_id, username, task.get('completed'), task.get('title')])


def main():
    if len(sys.argv) != 2:
        print("Usage python script.py <userId>")
        return
    user_id = sys.argv[1]
    user_data = fetch_user_data(user_id)
    tasks = fatch_tasks(user_id)

    username = user_data.get('username')
    write_to_csv =(user_id, username, tasks)


if __name__ == '__main__':
    main()
