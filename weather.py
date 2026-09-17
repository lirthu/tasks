import requests

response = requests.get(f'https://wttr.in/Москва?M?T?&lang=ru')
print(response.text)