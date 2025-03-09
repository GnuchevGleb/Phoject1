import logging


logger = logging.getLogger("masks.py")
file_handler = logging.FileHandler("../logs/masks.log", "w")
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_numbers_str: str) -> str:
    """
    Функция маскировки номера банковской карты
    Пример работы функции:
    7000792289606361 входной аргумент
    7000 79** **** 6361 выход функции
    """

    logger.info("начало работы функции get_mask_card_number")
    logger.info("обработка входящего значения номера банковской карты")
    logger.info(card_numbers_str)
    if card_numbers_str.isdigit():

        if len(card_numbers_str) == 16:
            logger.info("замаскированное значение")
            logger.info(str(f"{card_numbers_str[0:4]} {card_numbers_str[4:6]}** **** {card_numbers_str[12:]}"))
            return str(f"{card_numbers_str[0:4]} {card_numbers_str[4:6]}** **** {card_numbers_str[12:]}")
        else:

            return str("ошибка ввода")
    logger.error("ошибка ввода")
    return str("ошибка ввода")


def get_mask_account(bank_accounts_str: str) -> str:
    """
    Функция маскировки номера банковского счета
    Пример работы функции:
    73654108430135874305 входной аргумент
    **4305 выход функции
    """
    logger.info("начало работы функции get_mask_account")
    logger.info("обработка входящего значения номера банковского счета")
    logger.info(bank_accounts_str)

    if bank_accounts_str.isdigit():
        if len(bank_accounts_str) == 20:
            logger.info("замаскированное значение")
            logger.info(str(f"**{bank_accounts_str[-4:]}"))
            return str(f"**{bank_accounts_str[-4:]}")
        else:

            return str("ошибка ввода")
    logger.error("ошибка ввода")
    return str("ошибка ввода")
