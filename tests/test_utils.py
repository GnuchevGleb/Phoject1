
from src.utils import dictionary_transactions, transactions_sum


def test_transactions_sum(zeroo):
    print(transactions_sum)
    assert transactions_sum({}) == 0


def test_transactions_sum_1(test_transactions_1):

    assert transactions_sum(test_transactions_1) == 60888.63


def test_dictionary_transactions(we):
    print(we)
    assert dictionary_transactions(we) == {}
