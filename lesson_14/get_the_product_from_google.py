import requests
from pprint import pprint

url = 'https://script.google.com/macros/s/AKfycby7h0ZUecCiTB5hspKQHs5VQnv4lqf9vjx8P2LERZGt1hTKRpqttT0EWBTogqh4dmw/exec'

data = requests.get(url)
data_dict = data.json()

all_prices = sum([element['price'] for element in data_dict['food']])
all_prices_without_gluten = sum([element['price'] for element in data_dict['food'] if element['gluten']])
zero_amount = len([element['name'] for element in data_dict['food'] if element['amount'] == 0])

pprint(f'Ціна усіх товарів: {all_prices}')
pprint(f'Ціна усіх товарів без глютену: {all_prices_without_gluten}')
pprint(f'Скількох товарів немає: {zero_amount}')
