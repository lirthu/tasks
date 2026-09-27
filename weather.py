import requests

def get_weather(url):
    try:
        response = requests.get(url)
        if response:
            return response.text
    except Exception as error:
        return error

if __name__ == '__main__':
    link = 'https://wttr.in/Москва?M?T?&lang=ru'
    get_weather(link)