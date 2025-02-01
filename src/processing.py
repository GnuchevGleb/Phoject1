def filter_by_state (dictionaries, states = 'EXECUTED' ):
    """
    функция filter_by_state принимает список словарей и опционально значение для ключа
state (по умолчанию EXECUTED). Функция возвращает новый список словарей, содержащий только те словари, у которых ключ
state соответствует указанному значению.

Выход функции со статусом по умолчанию 'EXECUTED'
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

# Выход функции, если вторым аргументов передано 'CANCELED'
[{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
    """

    dictionaries_sort_executed = []
    dictionaries_sort_canceled = []

    if states == 'EXECUTED':
        for i in dictionaries:
            if i.get('state') == 'EXECUTED':
                dictionaries_sort_executed.append(i)
        return dictionaries_sort_executed
    elif states == 'CANCELED':
        for i in dictionaries:
            if i.get('state') == 'CANCELED':
                dictionaries_sort_canceled.append(i)
        return dictionaries_sort_canceled



