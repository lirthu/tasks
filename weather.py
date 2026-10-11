import logging
import requests

def config_logger():
    logging.basicConfig(level=logging.INFO,
                        filemode='w',
                        format='[%(asctime)s.%(msecs)03d] %(module)10s:%(lineno)-3d %(levelname)-7s - %(message)s',
                        encoding='utf-8'
                        )
    return None

def get_weather_in_moscow(url):
    try:
        response = requests.get(url)
        if response:
            return response.text
    except Exception as error:
        logging.error(f'Ошибка получения данных: {error}')

if __name__ == '__main__':
    link = 'https://wttr.in/Москва?M?T?&lang=ru'
    print(get_weather_in_moscow(link))