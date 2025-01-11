def get_mask_card_number(card_numbers: str) -> str:
    """
    Функция маскировки номера банковской карты
    Пример работы функции:
    7000792289606361 входной аргумент
    7000 79** **** 6361 выход функции
    """

    card_numbers_str = str(card_numbers)
    return str(f"{card_numbers_str[0:4]} {card_numbers_str[4:6]}** **** {card_numbers_str[12:]}")


def get_mask_account(bank_accounts: str) -> str:
    """
    Функция маскировки номера банковского счета
    Пример работы функции:
    73654108430135874305 входной аргумент
    **4305 выход функции
    """

    bank_accounts_str = str(bank_accounts)
    return str(f"**{bank_accounts_str[-4:]}")
