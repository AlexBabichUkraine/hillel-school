import requests
from pprint import pprint

url = 'https://dummyjson.com/todos'

parameters = {
    'limit': 150
}

response = requests.get(url, params=parameters)
uncompleted_works = []

if response.status_code == 200:
    works_list = response.json()['todos']
    for work in works_list:
        if work['completed'] is False:
            uncompleted_works.append(f"Uncompleted task: '{work['todo']}' for user with ID: {work['userId']}")

print(*uncompleted_works, sep='\n')
