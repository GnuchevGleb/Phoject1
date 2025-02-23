from src.decorators import get_mask_card_numbers
from tests.conftest import account_card


def test_mask_carts(account_card):

    for key in account_card:
        if "Maestro" in key[0]:

            assert str(get_mask_card_numbers((key[0][-16:])) == str(key[1][-16:]))

        if "MasterCard" in key[0]:

            assert str(get_mask_card_numbers((key[0][-16:])) == str(key[1][-19:]))


def my_function(x: int, y: int) -> int:
    print(f"Result: {x + y}")
    return x + y
