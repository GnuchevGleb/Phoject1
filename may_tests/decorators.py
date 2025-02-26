import datetime
import logging


def log(filename=None):
    """
    декоратор log автоматически логирует начало и конец выполнения функции, а также ее результаты или возникшие ошибки.
    """
    logging.basicConfig(
        filename=filename,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(module)s - %(message)s",
        filemode="w",
    )
    print(f"\n куда выводим:  {filename}")

    def wrapper(func):

        try:

            def inner(args):

                start_time = datetime.datetime.now()
                logging.info(f"Функция  {func.__name__} ")
                print((f"Функция  {func.__name__}  {args}"))
                logging.info(f"Время начала выполнения функции  {start_time}")
                result = func(args)  # запуск выполнения функции
                print(result)
                end_time = datetime.datetime.now()
                logging.info(f"Функция {func.__name__} выполнялась {end_time - start_time} секунд")
                logging.info("my_function ok")

                return result

            return inner
        except FileNotFoundError:
            logging.info(f"Файл '{filename}' не найден!")  # Если файл не найден, выводим сообщение об ошибке
        except IOError:
            logging.info(
                "Произошла ошибка ввода-вывода при чтении файла!"
            )  # Если возникает ошибка ввода-вывода, выводим сообщение об ошибке

    return wrapper


card_number_account = "Maestro 1596837868705199"


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
    print(f" Входные данные:::: {card_number_account}")
    if "Счет" in card_number_account:
        if card_number_account[-20:].isdigit():
            from src.masks import get_mask_account  # type: ignore

            logging.info(f"Результат выполнения функции    Счет {(get_mask_account(str(card_number_account[-20:])))}")
            return str(f"Счет {(get_mask_account(str(card_number_account[-20:])))}")
        logging.info(" ошибка ввода")
        return str("ошибка ввода")

    if "Maestro" or "MasterCard" in card_number_account:
        if card_number_account[-16:].isdigit():
            from src.masks import get_mask_card_number  # type: ignore

            logging.info(
                f" Результат выполнения функции  {card_number_account[:-16]}{(get_mask_card_number(str(card_number_account[-16:])))}"
            )
            return str(f"{card_number_account[:-16]} {(get_mask_card_number(str(card_number_account[-16:])))}")
        logging.info(f"ошибка ввода")
        return str("ошибка ввода")


print(f" результат {mask_account_cards(card_number_account)}")
