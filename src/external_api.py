import os

import requests
from dotenv import load_dotenv


def currency_exchange_rate(currencys: str) -> float:

    """Функция конвертации валюты"""

    # Загрузка переменных из .env-файла
    load_dotenv()
    ###############################################################################
    # Получение значения переменной API_KEY из .env-файла
    kei_api = os.getenv("API_KEY")

    ###############################################################################
    # Отправка GET-запроса к API
    url_rub_currencys = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currencys}&amount=5"
    headers = {"apikey": kei_api}
    response_rub_currencys = requests.get(url_rub_currencys, headers=headers)
    print(response_rub_currencys.json())  # вывод ответа от сервера курса валют
    response_rub_currencys = response_rub_currencys.json()
    print(response_rub_currencys)
    #################################################################################
    # результат для проверки функциональности
    # response_rub_currencys = {'success': True,
    # 'query': {'from': 'USD', 'to': 'RUB', 'amount': 5},
    # 'info': {'timestamp': 1741486023, 'rate': 89.050893},
    # 'date': '2025-03-09', 'result': 445.254465}

    ##################################################################################
    for response_rub_currencys_key, response_rub_currencys_value in response_rub_currencys.items():

        if response_rub_currencys_key == "info":
            currency_currencys = round(response_rub_currencys_value.get("rate"), 2)
            print(f" курс {currencys} =  {currency_currencys}")
            return currency_currencys


print(currency_exchange_rate("USD"))
