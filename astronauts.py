import logging
import requests
import time
from datetime import datetime
import json

def config_logger():
    logging.basicConfig(level=logging.INFO,
                        filemode='w',
                        format='[%(asctime)s.%(msecs)03d] %(module)10s:%(lineno)-3d %(levelname)-7s - %(message)s',
                        encoding='utf-8'
                        )
    return None


def retry_request(url, max_tries=3,delay=2):
    for attempt in range(max_tries):
        try:
            response = requests.get(url)
            if response:
                json_data = response.json()
                return json_data
        except requests.RequestException:
            if attempt < max_tries - 1:
                time.sleep(delay)
            else:
                logging.error('Превышено число попыток')
                raise

def get_current_date():
    try:
        today = datetime.today()
        time_format = "%Y-%m-%d"
        today = f"{today:{time_format}}"
        return today
    except Exception as error:
        logging.debug(f'Ошибка: {error}')

def get_people_in_space(json_data):
    try:
        logging.info(f'Общее количество людей: {json_data['number']}')
        for i in json_data['people']:
            logging.info(f'{i['name']:<20} - {i['craft']}')
    except Exception as error:
        logging.error(f'{error}')

def writing_data_to_json(current_date, json_data):
    try:
        with open(f"astros_{current_date}.json", 'w', encoding='utf-8') as file:
            for i in json_data['people']:
                dictionary = {i['name']: i['craft']}
                json.dump(dictionary, file, indent=4, ensure_ascii=False)
    except Exception as error:
        logging.error(f'Ошибка: {error}')

if __name__ == '__main__':
    config_logger()
    link = 'http://api.open-notify.org/astros.json'
    data = retry_request(link)
    get_people_in_space(data)
    writing_data_to_json(get_current_date(), data)
