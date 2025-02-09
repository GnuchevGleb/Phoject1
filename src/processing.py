from typing import Any
import datetime
from datetime import datetime


def filter_by_state(dictionaries: list[dict[str, Any]], states: str = "EXECUTED") -> list[dict[str, Any]]:
    """
    функция filter_by_state принимает список словарей и опционально значение для ключа
    state (по умолчанию EXECUTED). Функция возвращает новый список словарей,
    содержащий только те словари, у которых ключ
    state соответствует указанному значению.

    Выход функции со статусом по умолчанию 'EXECUTED'
    [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
     {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

    # Выход функции, если вторым аргументов передано 'CANCELED'
    [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
     {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
    """

    dictionaries_sort = []

    if states == "EXECUTED":
        for step in dictionaries:
            if step.get("state") == "EXECUTED":
                dictionaries_sort.append(step)

    elif states == "CANCELED":
        for step in dictionaries:
            if step.get("state") == "CANCELED":
                dictionaries_sort.append(step)

    return dictionaries_sort


def sort_by_date(dictionaries: list[dict[str, Any]], reverse: bool = True) -> Any:
    """
    функция sort_by_date принимает список словарей и необязательный параметр,
     задающий порядок сортировки (по умолчанию — убывание). Функция должна возвращать
    новый список, отсортированный по дате (date)

    Выход функции (сортировка по убыванию, т. е. сначала самые последние операции)
    [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
     {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
      {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
       {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
    """

    global date_object

    try:
        for step in dictionaries:
            date_object = step.get("date")[:10]
            # print(date_object)
            datetime.strptime(date_object, "%Y-%m-%d").date()

    except:

        return "ошибка формата даты"

    return sorted(dictionaries, key=lambda x: str(x["date"]), reverse=reverse)


# dictionaries = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
#       {'id': 615064591, 'state': 'CANCELED', 'date': '2018/10/14T08:21:33.419441'},
#       {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
#        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
# print(sort_by_date(dictionaries,True))
