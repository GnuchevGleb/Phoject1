def mask_account_card(card_number_account: str) -> str:
    """
Функция, которая умеет обрабатывать информацию как о картах, так и о счетах
Примеры работы функции
 Пример для карты
Visa Platinum 7000792289606361 - входной аргумент
Visa Platinum 7000 79** **** 6361 - выход функции

 Пример для счета
Счет 73654108430135874305 - входной аргумент
Счет **4305 - выход функции
    """


    if 'Счет' in card_number_account:

        from  masks import get_mask_account

        return f'Счет {(get_mask_account(int(card_number_account[-20:])))}'
    else:

        from masks import get_mask_card_number

        return f'{card_number_account[:-16]}{(get_mask_card_number(int(card_number_account[-16:])))}'

#card_number_account = 'Visa Platinum 8990922113665229'
#print(mask_account_card(card_number_account))



def get_date (date_time: str) -> str:
    """Функция, которая принимает на вход строку с датой в формате
"2024-03-11T02:26:18.671407"
 и возвращает строку с датой в формате
"ДД.ММ.ГГГГ" ("11.03.2024")
    """

    return f'{date_time[0:4]}.{date_time[5:7]}.{date_time[8:10]}'

#date_time = '2024-03-11T02:26:18.671407'
#print(get_date(date_time))