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

    def wrapper(function):

        def inner(arg):
            try:
                print(function, arg, filename)
                start_time = datetime.datetime.now()
                logging.info(f"Функция  {function.__name__} ")
                print(f"Функция  {function.__name__}   с входными данными {arg}")
                logging.info(f"Время начала выполнения функции  {start_time}")
                result = function(arg)  # запуск выполнения функции
                end_time = datetime.datetime.now()
                logging.info(f"Функция {function.__name__} выполнялась {end_time - start_time} секунд")
                print(f"Функция {function.__name__} выполнялась {end_time - start_time} секунд")
                logging.info(f"my_function ok")
            except:
                logging.exception("Exception occurred", exc_info=True)

            return

        return inner

    return wrapper


#
@log("mylog.txt")
def mask_account_cards(text):
    return


print(mask_account_cards("Maestro 1596837868705199"))

# @log()
# def mask_account_cards(text):
#     return
# print(mask_account_cards("Maestro 1596837868705199"))
