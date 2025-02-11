from src.widget import mask_account_card, get_date

#
# def test_mask_account_card():
#     assert mask_account_card('Maestro 1596837868705199') == 'Maestro 1596 83** **** 5199'
#     assert mask_account_card('MasterCard 7158300734726758') == 'MasterCard 7158 30** **** 6758'
#     assert mask_account_card('Maestro 1 96837868705199') == "ошибка ввода"
#     assert mask_account_card('MasterCard 71ыв300734726758') == "ошибка ввода"
#
#     assert mask_account_card('Счет 73654108430135874305') == 'Счет **4305'
#     assert mask_account_card('Счет  73654108430135874305') == 'Счет **4305'
#     assert mask_account_card('Счет7365410430135874305') == "ошибка ввода"
#     assert mask_account_card('Счет 7 65410430135874305') == "ошибка ввода"
#     assert mask_account_card('Счет 7sd -410430135874305') == "ошибка ввода"

import pytest


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Maestro 1 96837868705199", "ошибка ввода"),
        ("MasterCard 71ыв300734726758", "ошибка ввода"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Счет  73654108430135874305", "Счет **4305"),
        ("Счет7365410430135874305", "ошибка ввода"),
        ("Счет 7 65410430135874305", "ошибка ввода"),
        ("Счет 7sd -410430135874305", "ошибка ввода"),
    ],
)
def test_mask_account_card(test_input, expected):
    assert mask_account_card(test_input) == expected


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2024/03/11T02:26:18.671407", "11.03.2024"),
        ("", "ошибка формата даты"),
    ],
)
def test_get_date(test_input, expected):
    assert get_date(test_input) == expected
