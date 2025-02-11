import pytest
import datetime

@pytest.fixture
def list_number_1():
    return [
        {"id": 414288291, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2017-09-12T21:27:25.241689"},
        {"id": 939719571, "state": "EXECUTED", "date": "2016-06-30T02:08:58.425572"},
   ]


@pytest.fixture
def account_card():
    return [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Maestro ", "ошибка ввода"),
        ("Maestro 1 96837868705199", "ошибка ввода"),
        ("MasterCard 71ыв300734726758", "ошибка ввода"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Счет  73654108430135874305", "Счет **4305"),
        ("Счет7365410430135874305", "ошибка ввода"),
        ("Счет", "ошибка ввода"),
        ("Счет 7 65410430135874305", "ошибка ввода"),
        ("Счет 7sd -410430135874305", "ошибка ввода"),
    ]








@pytest.fixture
def executed():
    return [
        {"id": 414288291, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 939719571, "state": "EXECUTED", "date": "2016-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def canceled():
    return [

        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 594226727, "state": "CANCELED", "date": "2017-09-12T21:27:25.241689"},
    ]


@pytest.fixture
def zero():
    return []
#
#
@pytest.fixture
def sort():
    return [
        {"id": 414288291, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2017-09-12T21:27:25.241689"},
        {"id": 939719571, "state": "EXECUTED", "date": "2016-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def revers():
    return [
        {"id": 939719571, "state": "EXECUTED", "date": "2016-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2017-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 414288291, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]

@pytest.fixture
def list_error():
    return [
        {"id": 414288291, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018/10/14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018.09.12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2017-09-12T21:27:25.241689"},
        {"id": 939719571, "state": "EXECUTED", "date": "2016-06-30T02:08:58.425572"},
   ]

