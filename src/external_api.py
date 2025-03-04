import os

from dotenv import load_dotenv
import requests


def currency_exchange_rate(currencys: str) -> float:
    """Функция конвертации валюты"""

    list_currency = (
        "AED",
        "AFN",
        "ALL",
        "AMD",
        "ANG",
        "AOA",
        "ARS",
        "AUD",
        "AWG",
        "AZN",
        "BAM",
        "BBD",
        "BDT",
        "BGN",
        "BHD",
        "BIF",
        "BMD",
        "BND",
        "BOB",
        "BRL",
        "BSD",
        "BTC",
        "BTN",
        "BWP",
        "BYN",
        "BYR",
        "BZD",
        "CAD",
        "CDF",
        "CHF",
        "CLF",
        "CLP",
        "CNH",
        "CNY",
        "COP",
        "CRC",
        "CUC",
        "CUP",
        "CVE",
        "CZK",
        "DJF",
        "DKK",
        "DOP",
        "DZD",
        "EGP",
        "ERN",
        "ETB",
        "EUR",
        "FJD",
        "FKP",
        "GBP",
        "GEL",
        "GGP",
        "GHS",
        "GIP",
        "GMD",
        "GNF",
        "GTQ",
        "GYD",
        "HKD",
        "HNL",
        "HRK",
        "HTG",
        "HUF",
        "IDR",
        "ILS",
        "IMP",
        "INR",
        "IQD",
        "IRR",
        "ISK",
        "JEP",
        "JMD",
        "JOD",
        "JPY",
        "KES",
        "KGS",
        "KHR",
        "KMF",
        "KPW",
        "KRW",
        "KWD",
        "KYD",
        "KZT",
        "LAK",
        "LBP",
        "LKR",
        "LRD",
        "LSL",
        "LTL",
        "LVL",
        "LYD",
        "MAD",
        "MDL",
        "MGA",
        "MKD",
        "MMK",
        "MNT",
        "MOP",
        "MRU",
        "MUR",
        "MVR",
        "MWK",
        "MXN",
        "MYR",
        "MZN",
        "NAD",
        "NGN",
        "NIO",
        "NOK",
        "NPR",
        "NZD",
        "OMR",
        "PAB",
        "PEN",
        "PGK",
        "PHP",
        "PKR",
        "PLN",
        "PYG",
        "QAR",
        "RON",
        "RSD",
        "RUB",
        "RWF",
        "SAR",
        "SBD",
        "SCR",
        "SDG",
        "SEK",
        "SGD",
        "SHP",
        "SLE",
        "SLL",
        "SOS",
        "SRD",
        "STD",
        "SVC",
        "SYP",
        "SZL",
        "THB",
        "TJS",
        "TMT",
        "TND",
        "TOP",
        "TRY",
        "TTD",
        "TWD",
        "TZS",
        "UAH",
        "UGX",
        "USD",
        "UYU",
        "UZS",
        "VEF",
        "VES",
        "VND",
        "VUV",
        "WST",
        "XAF",
        "XAG",
        "XAU",
        "XCD",
        "XDR",
        "XOF",
        "XPF",
        "YER",
        "ZAR",
        "ZMK",
        "ZMW",
        "ZWL",
    )
    if currencys in list_currency:

        # Загрузка переменных из .env-файла
        load_dotenv()
        # print(currencys)
        # Получение значения переменной API_KEY из .env-файла
        kei_api = os.getenv("API_KEY")
        # print(kei_api)

        # Создание заголовка с токеном доступа API
        # Отправка GET-запроса к API

        url_rub_currencys = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currencys}&amount=5"
        headers = {"apikey": kei_api}
        response_rub_currencys = requests.get(url_rub_currencys, headers=headers)

        # # Обработка ответа
        print(response_rub_currencys.json())  # вывод ответа от сервера курса валют
        response_rub_currencys = response_rub_currencys.json()

        for response_rub_currencys_key, response_rub_currencys_value in response_rub_currencys.items():

            if response_rub_currencys_key == "rates":
                currency_currencys = response_rub_currencys_value.get("RUB")

                print(f" курс {currencys} =  {currency_currencys}")
                return currency_currencys
    else:
        print("не верно введена валюта")
        return []
    return


# print(currency_exchange_rate('USD'))
