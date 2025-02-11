from src.processing import filter_by_state, sort_by_date


def test_filter_by_state (list_number_1, executed):

    assert filter_by_state (list_number_1) == executed

def test_filter_by_state_1 (list_number_1, canceled):

    assert filter_by_state (list_number_1,"CANCELED") == canceled

def test_sort_by_date (list_number_1, sort):
    assert sort_by_date(list_number_1) == sort


def test_sort_by_date_revers (list_number_1, revers):
    assert sort_by_date(list_number_1, False) == revers


def test_sort_by_date_zero():
    assert sort_by_date([]) == []

def test_sort_by_date_error (list_error):


    assert sort_by_date (list_error) == "ошибка формата даты"
