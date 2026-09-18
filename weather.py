import requests

def get_weather():
    response = requests.get(f'https://wttr.in/Москва?M?T?&lang=ru')
    print(response.text)

if __name__ == '__main__':
    get_weather()