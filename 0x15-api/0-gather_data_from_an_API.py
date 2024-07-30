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

    # Fech user details
    users_url = "{}/users/{}".format(REST_API, user_id)
    user_response = requests.get(users_url)
    user_data = user_response.json()

    # Fetch todos
    todos_url = "{}/todos".format(REST_API)
    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    # Extract employee name
    employee_name = user_data.get('name')

    # Filter task for the user
    user_tasks = [todo for todo in todos if todo['userId'] == user_id]
    completed_tasks = [task for task in user_tasks if task['completed']]

    # Output the results
    print(
        "Employee {} is done with tasks({}/{}):".format(
            employee_name,
            len(completed_tasks),
            len(user_tasks)
        )
    )
    for task in completed_tasks:
        print("\t {}".format(task['title']))


if __name__ == '__main__':
    main()
