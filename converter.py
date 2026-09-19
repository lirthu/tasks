import argparse
import requests

def get_json_data(link):
    response = requests.get(link)
    data_json = response.json()
    return data_json

def converter_valute(amount, valute_name, json_data):
    get_value = json_data['Valute'][valute_name]['Value']
    total = amount * get_value
    return total

if __name__ == '__main__':

    get_link = 'https://www.cbr-xml-daily.ru/daily_json.js'

    parser = argparse.ArgumentParser(description='Valute to RUB')
    parser.add_argument('amount', type=int, help='amount of valute to convert')
    parser.add_argument('valute', type=str, help='type of valute to convert into rubles')
    args = parser.parse_args()

    print(converter_valute(args.amount, args.valute, get_json_data(get_link)))
