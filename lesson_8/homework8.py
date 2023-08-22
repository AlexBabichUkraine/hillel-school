from pywebio.input import input as pw_input, input_group, NUMBER, FLOAT

students = {
    'Іван Петров': {
        'Пошта': 'Ivan@gmail.com',
        'Вік': 14,
        'Номер телефону': '+380987771221',
        'Середній бал': 95.8
    },
    'Женя Курич': {
        'Пошта': 'Geka@gmail.com',
        'Вік': 16,
        'Номер телефону': None,
        'Середній бал': 64.5
    },
    'Маша Кера': {
        'Пошта': 'Masha@gmail.com',
        'Вік': 18,
        'Номер телефону': '+380986671221',
        'Середній бал': 80
    },
}
# ваш код нижче !!!!!!!! вище нічого не змінюємо


def age_validate(input_value):
    if input_value < 18:
        return 'Too young'
    if input_value > 40:
        return 'Too old'


def score_validate(input_value):
    if input_value > 100 or input_value < 0:
        return 'Enter value in range 0-100'


# Ввід данних студента та занесення в словник
data = input_group('New students data', [
    pw_input('Please enter name of student: ', name='name'),
    pw_input('Please enter email of student: ', name='email'),
    pw_input('Please enter age of student: ', name='age', type=NUMBER, validate=age_validate),
    pw_input('Please enter phone of student: ', name='phone'),
    pw_input('Please enter score of student: ', name='score', type=FLOAT, validate=score_validate),
])

students[data['name']] = {
    'Пошта': data['email'],
    'Вік': data['age'],
    'Номер телефону': data['phone'],
    'Середній бал': data['score'],
}

students_best_score = []
summary_score = 0

# Знаходимо студентів які мають високий балл
for key, value in students.items():
    if value['Середній бал'] > 90:
        students_best_score.append(f"{key}: {value['Середній бал']}")
    if value['Номер телефону'] is None:
        value['Номер телефону'] = '+3800504768089'

    summary_score += value['Середній бал']


average_score = summary_score / len(students)

# виводимо список успішних студентів
for element in students_best_score:
    print(element)
print(f'Average score for group: {round(average_score, 1)}')
