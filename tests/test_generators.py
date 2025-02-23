import pytest
from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_card_number_generator_min():

    assert card_number_generator(1, 5) == [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005",
    ]
    # assert next(generator) == "0000 0000 0000 0002"
    # assert next(generator) == "0000 0000 0000 0003"


@pytest.mark.parametrize(
    "start_s, stop_s, result",
    [
        (2, 1, "ошибка"),
        (1, "a", "ошибка"),
        (0, 5, "ошибка"),
        (1, 99999999999999999, "ошибка"),
    ],
)
def test_card_number_generator(start_s, stop_s, result):
    assert card_number_generator(start_s, stop_s) == result


def test_filter_by_currency_default(test_transactions):
    generator = filter_by_currency(test_transactions)
    assert next(generator) == test_transactions[0]
    assert next(generator) == test_transactions[1]
    assert next(generator) == test_transactions[3]


def test_filter_by_currency_manual_currency(test_transactions):
    generator = filter_by_currency(test_transactions, "RUB")
    assert next(generator) == test_transactions[2]
    assert next(generator) == test_transactions[4]


def test_filter_by_currency_not_currency(test_transactions):
    generator = filter_by_currency(test_transactions, "EUR")
    with pytest.raises(StopIteration):
        next(generator) == StopIteration


def test_filter_by_currency_not_list():
    generator = filter_by_currency([])
    with pytest.raises(StopIteration):
        next(generator) == StopIteration


def test_transaction_descriptions(test_transactions):
    generator = transaction_descriptions(test_transactions)
    assert next(generator) == "Перевод организации"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод со счета на счет"


def test_transaction_descriptions():
    generator = filter_by_currency([])
    with pytest.raises(StopIteration):
        next(generator) == StopIteration
