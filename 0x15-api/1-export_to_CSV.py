#!/usr/bin/python3

"""Export API data to csv"""

import csv
import requests
import sys


def fetch_user_data(user_id):
    """Fetch user data from API"""
    url_user = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    response = requests.get(url_user)
    return response.json()


def fetch_tasks(user_id):
    """Fetch task data from API"""
    base_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'
    url_tasks = base_url.format(user_id)
    response = requests.get(url_tasks)
    return response.json()


def write_to_csv(user_id, username, tasks):
    """Write the task data to csv file"""
    filename = '{}.csv'.format(user_id)
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in tasks:
            row = [user_id, username, task['completed'], task['title']]
            writer.writerow(row)


def main():
    if len(sys.argv) != 2:
        print("Usage python script.py <userId>")
        return
    user_id = sys.argv[1]
    user_data = fetch_user_data(user_id)
    tasks = fetch_tasks(user_id)

    username = user_data.get('username')
    write_to_csv(user_id, username, tasks)


if __name__ == '__main__':
    main()
