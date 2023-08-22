import requests

url = 'http://api.open-notify.org/astros.json'
response = requests.get(url)
astros_on_orbit = []

if response.status_code == 200:
    astro_json = response.json()['people']
    for astronaut in astro_json:
        if astronaut['craft'] == 'ISS':
            astros_on_orbit.append(f'{astronaut["name"]}: currently on ISS (orbital )')

print(*astros_on_orbit, sep='\n')
