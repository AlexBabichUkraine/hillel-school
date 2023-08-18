camry_elegance = {
    'type': 'sedan',
    'engine': '2,5 hybrid',
    'color': 'red',
    'power': 218,
    'max speed': 180,
    'length': 4.885,
    'width': 1.840,
    'height': 1.445,
    'guarantee in years': 5,
    'multimedia': [
        'Інформаційно-розважальна система Toyota Touch 2',
        '6 динаміків',
        'Багатофункціональний сенсорний дисплей 9',
        'Система безпровідного зв"язку за протоколом Bluetooth',
        'Підтримка систем Apple CarPlay та Android Auto',
    ]
}

for key, value in camry_elegance.items():
    if type(value) == list:
        print(key, end=': ')
        print(*value, sep=', ')
    else:
        print(f'{key}: {value}')
