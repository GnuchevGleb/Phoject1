import time
import datetime

# card_numbers = "1596837868705198"


def log(filename=None):

    """Функция вычисляет время выполнения передаваемой ей функции"""

    def timing_decorator(func):
        def wrapper(*args, **kwargs):
            # print(filename, args)
            if filename == "mylog.txt":
                f = open("mylog.txt", "a")
                f.write(f"\n Функция {func.__name__}  начала работу  {datetime.datetime.now()}")
                f.write(f" \n   Запись в файл {filename} \n Входные данные {args} ")
                start_time = time.time()
                func(*args, **kwargs)
                f.write(f"\n        Результат работы {func(*args, **kwargs)}")
                end_time = time.time()
                f.write(f"\n            Функция {func.__name__}  завершила работу  {datetime.datetime.now()}")
                # print(f" \n Функция  {func.__name__}  выполнялась {end_time - start_time:.2f} секунд")
                f.write(f" \n               Функция  {func.__name__}  выполнялась {end_time - start_time:.2f} секунд")
                f.close()

            if filename is None:
                print(f" \n Функция {func.__name__}  начала работу")
                print(f" \n     Запись в файл {filename} \n Входные данные {args} ")
                start_time = time.time()
                func(*args, **kwargs)
                print(f"\n          Функция {func.__name__}  завершила работу  {datetime.datetime.now()}")
                print(f"\n              Результат работы {func(*args, **kwargs)}")
                end_time = time.time()
                print(f" \n                 Функция  {func.__name__}  выполнялась {end_time - start_time:.2f} секунд")

        return wrapper

    return timing_decorator


@log("mylog.txt")
def get_mask_card_numbers(card_numbers_str: str) -> str:
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
            return str("ошибка ввода")
    return str("ошибка ввода")


# get_mask_card_numbers(card_numbers)
