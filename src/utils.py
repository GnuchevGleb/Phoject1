import json
import random
import logging
from src.external_api import currency_exchange_rate
import os
from dotenv import load_dotenv


list_tr = []
logger = logging.getLogger("utils.py")
file_handler = logging.FileHandler("../logs/utils.log", "w")
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def list_transactions(way) -> list:
    """функция считывает данные из файла operations.json в директории data в формате json
    и преобразует в формат python"""
    logger.info("начало работы функции list_transactions")

    try:

        with open(way, "r", encoding="utf-8") as file:  # Открываем файл
            text = file.read()  # Читаем содержимое в переменную text
            logger.info("читаем содержимое файла в переменную text")
            elements = len(json.loads(text))
            random_number = random.randint(1, elements)
        logger.info("возвращаем случайно выбранную транзакцию")
        logger.info(json.loads(text)[random_number])
        return json.loads(text)[random_number]  # возвращаем случайно выбранную транзакцию
    except FileNotFoundError:
        logger.error("FileNotFoundError")
        print("ошибка FileNotFoundError")
        return []
    except Exception as e:
        logger.error("ошибка Exception")
        print("Exception")
        return []


# определяем путь к файлу с транзакциями
load_dotenv()
way = os.getenv("WAY_TRANSACTION")
list_tr = list_transactions(way)


def transactions_sum(list_transaction: dict) -> float or str:

    """функция вычисляет сумму транзакций в рублях. Валюту пересчитывает по курсу"""

    logger.info("начало работы функции transactions_sum")
    logger.info("рассматриваем транзакцию: ")
    logger.info(list_transaction)

    print(f" рассматриваем транзакцию: {list_transaction}")
    transactions_sum_list = []

    if len(list_transaction) < 1:
        logger.error("ошибка - файл пуст")
        print("ошибка данных")
        return "ошибка данных"
    else:
        logger.info("отправляем запрос курса EUR")
        currency_eur = currency_exchange_rate("EUR")
        if isinstance(currency_eur, (int, float)) == bool(True):
            print(currency_eur, "курс EUR")
        else:
            logger.error("ошибка - курс не определён")
            print("курс не определён")
            return transactions_sum_list

        logger.info("отправляем запрос курса USD")
        currency_usd = currency_exchange_rate("USD")
        if isinstance(currency_usd, (int, float)) == bool(True):
            print(currency_usd, "курс USD")
        else:
            logger.error("ошибка - курс не определён")
            print("курс не определён")
            return transactions_sum_list

        for operationAmount in list_transaction:

            if operationAmount == "operationAmount":

                if list_transaction[operationAmount].get("currency").get("code") == "RUB":
                    logger.info("расчёт курса RUB")
                    transaction_sum = float(list_transaction[operationAmount].get("amount"))
                    transaction_sum_f = float(f"{transaction_sum:.2f}")
                    print(f"{transaction_sum_f}:   {list_transaction[operationAmount].get('currency').get('code')}")

                if list_transaction[operationAmount].get("currency").get("code") == "USD":
                    logger.info("расчёт курса USD")
                    transaction_sum = float(list_transaction[operationAmount].get("amount")) * float(currency_usd)
                    transaction_sum_f = float(f"{transaction_sum:.2f}")
                    print(f"{transaction_sum_f}:   RUB по курсу USD")

                if list_transaction[operationAmount].get("currency").get("code") == "EUR":
                    logger.info("расчёт курса EUR")
                    transaction_sum = float(list_transaction[operationAmount].get("amount")) * float(currency_eur)
                    transaction_sum_f = float(f"{transaction_sum:.2f}")
                    print(f"{transaction_sum_f}:   RUB по курсу EUR")
    logger.info("сумма транзакции:")
    logger.info(transaction_sum_f)
    return transaction_sum_f


print("Сумма транзакции  ", transactions_sum(list_tr))
