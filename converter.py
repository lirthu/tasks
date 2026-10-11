import logging
import argparse
import requests

def config_logger():
    logging.basicConfig(level=logging.INFO,
                        filemode='w',
                        format='[%(asctime)s.%(msecs)03d] %(module)10s:%(lineno)-3d %(levelname)-7s - %(message)s',
                        encoding='utf-8'
                        )
    return None

def parser_creator():
    parser = argparse.ArgumentParser(description='Valute to RUB')
    parser.add_argument('amount', type=int, help='amount of valute to convert')
    parser.add_argument('valute', type=str, help='type of valute to convert into rubles')
    return parser

def get_json_data(url):
    try:
        response = requests.get(url)
        if response:
            data_json = response.json()
            return data_json
    except Exception as error:
        logging.error(f'Ошибка получения данных: {error}')

def converter_valute(amount, valute_name, json_data):
    try:
        get_value = json_data['Valute'][valute_name]['Value']
        total = amount * get_value
        return logging.info(round(total, 2))
    except Exception as e:
        logging.error(f'Валюта {e} не найдена!')

if __name__ == '__main__':
    link = 'https://www.cbr-xml-daily.ru/daily_json.js'
    args = parser_creator().parse_args()
    print(converter_valute(args.amount, args.valute, get_json_data(link)))
