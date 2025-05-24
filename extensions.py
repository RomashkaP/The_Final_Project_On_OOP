import requests
import json
from config import curr_dict

class APIException(Exception):
    pass

class CurrancyConverter():
    @staticmethod
    def get_price(base, quote, amount):
        if base == quote:
            raise APIException(f'Невозможно перевести одинаковые валюты - {base}.')
        try:
            base_ticker = curr_dict[base]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту - {base}.')
        try:
            quote_ticker = curr_dict[quote]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту - {quote}.')
        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество - {amount}.')
        if amount <= 0:
            raise APIException('Количество должно быть больше нуля.')
        r = requests.get(f'https://v6.exchangerate-api.com/v6/b6bba2ca8863521061779a7e/latest/{base_ticker}').json()
        result_amount = r['conversion_rates'][quote_ticker] * amount
        return result_amount