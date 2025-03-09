import pytest

from src.widget import get_date, mask_account_card


def test_mask_account_card(account_card):

    # print(account_card)
    for key in account_card:
        # print(key)
        assert mask_account_card(str(key[0])) == key[1]


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
