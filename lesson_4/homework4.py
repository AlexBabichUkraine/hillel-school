from pywebio.input import input as pw_input
from pywebio.output import put_success, put_warning

cat_emoji = '\U0001F431'
dog_emoji = '\U0001F436'
fish_emoji = '\U0001F41F'
hamster_emoji = '\U0001F439'
turtle_emoji = '\U0001F422'
can_swim = False
excluded_symbols = " )(*/.!@#$%^&*,;:'1234567890"

pet_type = str(pw_input('What pet do you have: ', required=True)).strip(excluded_symbols).lower()
pet_name = str(pw_input('What is name of your pet: ', required=True)).strip(excluded_symbols).title()

if pet_type == 'fish' or pet_type == 'turtle':
    can_swim = True

if can_swim is True:
    put_warning(f'You need aquarium for {pet_type}')

if pet_type == 'dog':
    put_success(f"I'm scared of dog barking  {dog_emoji}, including dog for name {pet_name}")
elif pet_type == 'cat':
    put_success(f"The cats are catching the mice {cat_emoji}, including cat for name {pet_name}")
elif pet_type == 'hamster':
    put_success(f"The hamsters are small{hamster_emoji}, including hamster for name {pet_name}")
elif pet_type == 'fish':
    put_success(f"Don't cook fish {fish_emoji}, including fish for name {pet_name}")
elif pet_type == 'turtle':
    put_success(f"The turtle has heavy shell{turtle_emoji}, including turtle for name {pet_name}")
else:
    put_warning("sorry i don't know this animal")
