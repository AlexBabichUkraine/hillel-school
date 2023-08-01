from pywebio.input import input as pw_input
from pywebio.output import put_success

favourite_food = pw_input('Enter your favourite food >>>').title()
favourite_food = favourite_food.lower()
emoji = '\U0001F604'
result = f'oh this food: {favourite_food}, its my  favourite too {emoji}'
put_success(result)
