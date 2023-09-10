import requests
from pprint import pprint

url = 'https://script.google.com/macros/s/AKfycby7h0ZUecCiTB5hspKQHs5VQnv4lqf9vjx8P2LERZGt1hTKRpqttT0EWBTogqh4dmw/exec'

data = requests.get(url)
data_dict = data.json()
products_with_gluten = []
products_without_gluten = []
price = 0
price_1 = 0
price_without_gluten = 0

names = []
# for product in data_dict['food']:
#     if product['gluten']:
#         price += product['price']
#         products_with_gluten.append(product["name"])
#     else:
#         products_without_gluten.append(product['name'])
#         price_without_gluten += product['price']
#         names.append(product["name"])
#
# print(f'products with gluten: {products_with_gluten}')
# print(f'products without gluten: {products_without_gluten}')

all_prices = sum([element['price'] for element in data_dict['food']])
all_prices_without_gluten = sum([element['price'] for element in data_dict['food'] if element['gluten']])
no_left = len([element['name'] for element in data_dict['food'] if element['amount'] == 0])


pprint(f'Ціна усіх товарів: {all_prices}')
pprint(f'Ціна усіх товарів без глютену: {all_prices_without_gluten}')
print(f'Скількох товарів немає: {no_left}')
