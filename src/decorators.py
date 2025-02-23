import datetime
import logging

account_card = "Maestro 1596837868705199"


def log(filename=None):
    logging.basicConfig(
        filename=filename,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(module)s - %(message)s",
        filemode="w",
    )
    print(f"\n куда выводим:  {filename}")

    def wrapper(func):
        def inner(args):
            start_time = datetime.datetime.now()
            logging.info(f"Функция  {func.__name__}")
            logging.info(f"Время начала выполнения функции  {start_time}")
            result = func(args)
            end_time = datetime.datetime.now()
            logging.info(f"Функция {func.__name__} выполнялась {end_time - start_time} секунд")
            logging.info(f"my_function ok")
            return result

        return inner

    return wrapper


@log("mylog.txt")
def mask_account_cards(card_number_account: str) -> str:
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

    logging.info(f"Входные данные: {card_number_account}  ")
    print(f" Входные данные: {card_number_account}")
    if "Счет" in card_number_account:
        if card_number_account[-20:].isdigit():
            from src.masks import get_mask_account  # type: ignore

            logging.info(f"Результат выполнения функции    Счет {(get_mask_account(str(card_number_account[-20:])))}")
            return str(f"Счет {(get_mask_account(str(card_number_account[-20:])))}")
        logging.info(f" ошибка ввода")
        return str("ошибка ввода")

    if "Maestro" or "MasterCard" in card_number_account:
        if card_number_account[-16:].isdigit():
            from src.masks import get_mask_card_number  # type: ignore

            logging.info(
                f" Результат выполнения функции  {card_number_account[:-16]}{(get_mask_card_number(str(card_number_account[-16:])))}"
            )
            return str(f"{card_number_account[:-16]}{(get_mask_card_number(str(card_number_account[-16:])))}")
        logging.info(f"ошибка ввода")
        return str("ошибка ввода")


print(mask_account_cards(account_card))
