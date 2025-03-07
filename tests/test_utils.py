from src.utils import transactions_sum, list_transactions
import pytest



def test_transactions_sum(zero):
    print(transactions_sum)
    assert transactions_sum([]) == 'ошибка данных'


def test_transactions_sum_1(test_transactions_1):

    assert transactions_sum(test_transactions_1) == 60888.63


def test_list_transactions(we):
    print(we)
    assert  list_transactions(we) == []