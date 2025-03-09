import csv
import os

import pandas as pd
from dotenv import load_dotenv

# определяем путь к файлу с транзакциями
load_dotenv()
way = os.getenv("WAY_TRANSACTION_CSV")
print(way)


def list_transactions_csv(way):
    with open(way, "r", encoding="utf-8") as file:  # Открываем файл
        text = file.read()  # Читаем содержимое в переменную text
        # print(text)
    with open(way) as file:
        reader = csv.reader(file)
        for row in reader:
            print("**", row)
    wine_reviews = pd.read_csv(way)
    print(wine_reviews)
    pass


list_tr_csv = list_transactions_csv(way)
