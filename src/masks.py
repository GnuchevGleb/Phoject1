def get_mask_card_number(card_numbers_str: str) -> str:
    """
    Функция маскировки номера банковской карты
    Пример работы функции:
    7000792289606361 входной аргумент
    7000 79** **** 6361 выход функции
    """

    if card_numbers_str.isdigit():

        if len(card_numbers_str) == 16:

            return str(f"{card_numbers_str[0:4]} {card_numbers_str[4:6]}** **** {card_numbers_str[12:]}")
        else:
            return str("ошибка длины номера карты")

    return str("ошибка ввода номера карты")


def get_mask_account(bank_accounts_str: str) -> str:
    """
    Функция маскировки номера банковского счета
    Пример работы функции:
    73654108430135874305 входной аргумент
    **4305 выход функции
    """

    if bank_accounts_str.isdigit():
        if len(bank_accounts_str) == 20:
            return str(f"**{bank_accounts_str[-4:]}")
        else:
            return str("ошибка длины номера банковского счета")

    return str("ошибка ввода номера банковского счета")
