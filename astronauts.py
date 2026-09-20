import requests
import time
from datetime import datetime
import json

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
                print('Превышено число попыток')
                raise

def get_current_date():
    today = datetime.today()
    time_format = "%Y-%m-%d"
    today = f"{today:{time_format}}"
    return today

def getting_people(json_data):
    print('Общее количество людей: ', json_data['number'])
    for i in json_data['people']:
        print(i['name'], i['craft'])

def data_writing_json(current_date, json_data):
    with open(f"astros_{current_date}.json", 'w', encoding='utf-8') as file:
        for i in json_data['people']:
            dictionary = {i['name']: i['craft']}
            json.dump(dictionary, file, indent=4, ensure_ascii=False)

if __name__ == '__main__':
    link = 'http://api.open-notify.org/astros.json'
    data = retry_request(link)
    getting_people(data)
    data_writing_json(get_current_date(), data)
