import json
import os
import os.path
import sys

import requests
from dotenv import load_dotenv

from src.external_api import currency_exchange_rate

list_tr = []
load_dotenv()
way = os.getenv("WAY_TRANSACTION")

def list_transactions(way) -> list:
    """функция считывает данные из файла operations.json в директории data в формате json
    и преобразует в формат python"""
    print(way,'************************************')
    try:
        with open(way, "r", encoding="utf-8") as file:  # Открываем файл
            text = file.read()  # Читаем содержимое в переменную text
            #print(text)  # выводим содержимое файла

        return json.loads(text)
    except FileNotFoundError:
        list_transaction = []
        return list_transaction
    except Exception as e:
        list_transaction = []
        return list_transaction



#print(list_transactions(way))
# list_tr = list_transactions()


def transactions_sum(list_transaction: list) -> list:

    """функция вычисляет сумму транзакций в рублях. Валюту пересчитывает по курсу"""

    transactions_sum_list = []
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



    for transaction in list_transactions():
        for operationAmount in transaction:
            if operationAmount == "operationAmount":

                if transaction[operationAmount].get("currency").get("code") == "RUB":
                    transaction_sum = float(transaction[operationAmount].get("amount"))
                    transaction_sum_f = float(f"{transaction_sum:.2f}")
                    print(f"{transaction_sum_f}:{transaction[operationAmount].get('currency').get('code')}")
                    transactions_sum_list.append(
                        f"{transaction_sum_f}:{transaction[operationAmount].get('currency').get('code')}"
                    )
                if transaction[operationAmount].get("currency").get("code") == "USD":
                    transaction_sum = float(transaction[operationAmount].get("amount")) * float(currency_usd)
                    transaction_sum_f = float(f"{transaction_sum:.2f}")
                    transactions_sum_list.append(f"{transaction_sum_f}:RUB по курсу USD")
                    print(f"{transaction_sum_f}:RUB по курсу USD")
                if transaction[operationAmount].get("currency").get("code") == "EUR":
                    transaction_sum = float(transaction[operationAmount].get("amount")) * float(currency_eur)
                    transaction_sum_f = float(f"{transaction_sum:.2f}")
                    transactions_sum_list.append(f"{transaction_sum_f}:RUB по курсу EUR")
                    print(f"{transaction_sum_f}:RUB по курсу EUR")

        # print(transaction)

    return transactions_sum_list


print(transactions_sum(list_tr))
