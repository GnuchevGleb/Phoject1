from src.ftr import list_transactions_csv


def test_list_transactions_csv(file_not):
    assert list_transactions_csv(file_not) == "Path does not exist"


def test_list_transactions_csv_2(tst_sv):
    assert type(list_transactions_csv(tst_sv)) == dict


def test_list_transactions_ex(file_not):
    assert list_transactions_csv(file_not) == "Path does not exist"


def test_llist_transactions_ex_2(tst_sv):
    assert type(list_transactions_csv(tst_sv)) == dict
