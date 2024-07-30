#!/usr/bin/python3

'''
Request employee data from API
'''
import requests
import sys

REST_API = "https://jsonplaceholder.typicode.com"

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <userId>")
        return
    user_id = sys.argv[1]
    if not user_id.isdigit():
        print("Error: The user ID must be an integer")
        return
    user_id = int(user_id)

    users_url = f"{REST_API}/users/{user_id}"
    user_response = requests.get(users_url)
    user_data = user_response.json()

    todos_url = f"{REST_API}/todos"
    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    employee_name = user_data.get('name')
    user_task = [todo for todo in todos if todo['userId'] == user_id]
    completed_tasks = [task for task in user_task if task['completed']]

    print(f"Employee {employee_name} is done with tasks({len(completed_tasks)}/{len(user_tasks)}):")
    for task in completed_tasks:
        print(f"\t {task[title]}")

if __name__ == '__main__':
    main()
