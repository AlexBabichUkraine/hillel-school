from pywebio.input import input as pw_input
from pywebio.output import put_success

visited_cities = pw_input('Please enter cities that you visited last 10 years: ', required=True)
wanted_to_visit_cities = pw_input('Please enter cities that you want visit in next 10 years: ', required=True)

visited_cities_cleared = ''

for letter in visited_cities:
    if letter.isalpha() or letter == '-':
        visited_cities_cleared += letter
    else:
        visited_cities_cleared += ' '

visited_cities_set = set(visited_cities_cleared.title().split())

wanted_to_visit_cities_cleared = ''

for letter in wanted_to_visit_cities:
    if letter.isalpha() or letter == '-':
        wanted_to_visit_cities_cleared += letter
    else:
        wanted_to_visit_cities_cleared += ' '

wanted_to_visit_cities_set = set(wanted_to_visit_cities_cleared.title().split())

liked_cities = visited_cities_set & wanted_to_visit_cities_set

if liked_cities:
    put_success(f"You maybe very like these city/cities: {', '.join(liked_cities)}")
else:
    put_success(f'You are ready to see something new')

