import sys

import requests
from pprint import pprint
import inspect

url = 'https://script.google.com/macros/s/AKfycbyuXjpd6D0hI_J4IriLANECbA_5PUPDxi2g0vux72pmjxvaI4mj9OOIidswGfzuvUhC/exec'


data = requests.get(url)

data_dict = data.json()

# pprint(data_dict)

money = 0

# names = []
# for person in data_dict['trip']:
#     if person['money']:
#         print(f'{person["name"]} -->> {person["money"]}')
#         money += person['money']
#
#     names.append(person["name"])
#
# print(money)
# print(names)

# money = [person['money'] for person in data_dict['trip']]
# money = sum([person['money'] for person in data_dict['trip'] if person['money']])
# print(money)
#
names = [person["name"] for person in data_dict['trip']]
print(names)
print(sys.getsizeof(names))

names = (person["name"] for person in data_dict['trip'])
print(names)
print(sys.getsizeof(names))

print(next(names))
print(next(names))
print(next(names))

print(9999999999999999999999)

print(next(names))
print(next(names))

#
# names = {person["name"] for person in data_dict['trip']}
# print(names)
#
# names = {person["name"]: person["money"] for person in data_dict['trip']}
# print(names)
