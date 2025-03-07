import json

import random

from src.external_api import currency_exchange_rate
import os
from dotenv import load_dotenv


list_tr = []


def list_transactions(way) -> list:
    """функция считывает данные из файла operations.json в директории data в формате json
    и преобразует в формат python"""

    print(type(way), way)
    try:

        with open(way, "r", encoding="utf-8") as file:  # Открываем файл
            text = file.read()  # Читаем содержимое в переменную text

            elements = len(json.loads(text))
            random_number = random.randint(1, elements)

        return json.loads(text)[random_number]  # возвращаем случайно выбранную транзакцию
    except FileNotFoundError:
        print("FileNotFoundError")
        return []
    except Exception as e:
        print("Exception")
        return []


# определяем путь к файлу с транзакциями
load_dotenv()
way = os.getenv("WAY_TRANSACTION")

list_tr = list_transactions(way)


def transactions_sum(list_transaction: dict) -> float:

    """функция вычисляет сумму транзакций в рублях. Валюту пересчитывает по курсу"""

    print(f" рассматриваем транзакцию {list_transaction}")
    transactions_sum_list = []

    if len(list_transaction) < 1:
        print("ошибка данных")
        return "ошибка данных"
    else:
        currency_eur = currency_exchange_rate("EUR")
        if isinstance(currency_eur, (int, float)) == True:
            print(currency_eur, "курс EUR")
        else:
            print("курс не определён")
            return transactions_sum_list

        currency_usd = currency_exchange_rate("USD")
        if isinstance(currency_usd, (int, float)) == True:
            print(currency_usd, "курс USD")
        else:
            print("курс не определён")
            return transactions_sum_list

        for operationAmount in list_transaction:

            if operationAmount == "operationAmount":

                if list_transaction[operationAmount].get("currency").get("code") == "RUB":

                    transaction_sum = float(list_transaction[operationAmount].get("amount"))
                    transaction_sum_f = float(f"{transaction_sum:.2f}")
                    print(f"{transaction_sum_f}:   {list_transaction[operationAmount].get('currency').get('code')}")

                if list_transaction[operationAmount].get("currency").get("code") == "USD":
                    transaction_sum = float(list_transaction[operationAmount].get("amount")) * float(currency_usd)
                    transaction_sum_f = float(f"{transaction_sum:.2f}")

                    print(f"{transaction_sum_f}:   RUB по курсу USD")
                if list_transaction[operationAmount].get("currency").get("code") == "EUR":
                    transaction_sum = float(list_transaction[operationAmount].get("amount")) * float(currency_eur)
                    transaction_sum_f = float(f"{transaction_sum:.2f}")

                    print(f"{transaction_sum_f}:   RUB по курсу EUR")

    return transaction_sum_f


print("Сумма транзакции  ", transactions_sum(list_tr))
