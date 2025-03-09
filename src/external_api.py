import os
from dotenv import load_dotenv

import requests


def currency_exchange_rate(currencys: str) -> float:

    """Функция конвертации валюты"""

    # Загрузка переменных из .env-файла
    load_dotenv()
    ###############################################################################
    # print(currencys)
    # Получение значения переменной API_KEY из .env-файла
    kei_api = os.getenv("API_KEY")
    # print(kei_api)
    # Создание заголовка с токеном доступа API
    # Отправка GET-запроса к API

    url_rub_currencys = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currencys}&amount=5"
    headers = {"apikey": kei_api}
    response_rub_currencys = requests.get(url_rub_currencys, headers=headers)
    print(response_rub_currencys.json())  # вывод ответа от сервера курса валют
    response_rub_currencys = response_rub_currencys.json()
    #################################################################################
    # response_rub_currencys = {
    #     "base": "USD",
    #     "date": "2025-03-05",
    #     "rates": {"RUB": 31957.58},
    #     "success": True,
    #     "timestamp": 1741191972,
    # }  # результат для проверки функциональности
    ##################################################################################
    for response_rub_currencys_key, response_rub_currencys_value in response_rub_currencys.items():

        if response_rub_currencys_key == "rates":
            currency_currencys = response_rub_currencys_value.get("RUB")
            print(f" курс {currencys} =  {currency_currencys}")
            return currency_currencys


# print(currency_exchange_rate('USD'))
