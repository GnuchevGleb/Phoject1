from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number() -> str:
    assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361"
    assert get_mask_card_number("78787787000792289606") == "ошибка длины номера карты"
    assert get_mask_card_number("54289606") == "ошибка длины номера карты"
    assert get_mask_card_number("7dfdf000792289606") == "ошибка ввода номера карты"
    assert get_mask_card_number("") == "ошибка ввода номера карты"
    assert get_mask_card_number("-7000792289 606361.1") == "ошибка ввода номера карты"


def test_get_mask_account() -> str:
    assert get_mask_account("73654108430135874305") == "**4305"
    assert get_mask_account("73654108430135874") == "ошибка длины номера банковского счета"
    assert get_mask_account("736541084302222222135874") == "ошибка длины номера банковского счета"
    assert get_mask_account("73sds654108430135874") == "ошибка ввода номера банковского счета"
    assert get_mask_account("") == "ошибка ввода номера банковского счета"
    assert get_mask_account("-73sds654108 430135874.4") == "ошибка ввода номера банковского счета"
