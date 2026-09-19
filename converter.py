import argparse
import requests

response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
response_json = response.json()

def convert(amount, in_valute):
    value_in_valute = response_json['Valute'][in_valute]['Value']
    total = amount * value_in_valute
    return total

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Valute to RUB')
    parser.add_argument('amount', type=int, help='amount of valute to convert')
    parser.add_argument('valute', type=str, help='type of valute to convert into rubles')
    args = parser.parse_args()
    print(convert(args.amount, args.valute))