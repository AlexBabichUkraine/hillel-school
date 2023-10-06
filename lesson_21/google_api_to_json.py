import json
import requests
from pprint import pprint

url = 'https://script.google.com/macros/s/AKfycby7h0ZUecCiTB5hspKQHs5VQnv4lqf9vjx8P2LERZGt1hTKRpqttT0EWBTogqh4dmw/exec'

data = requests.get(url)
data_dict = data.json()

with open('data_from_google_api.json', mode='w', encoding='utf-8') as json_file:
    json.dump(data_dict, json_file, indent=4)

with open('data_from_google_api.json') as file:
    data_json = json.load(file)
    pprint(data_json)
