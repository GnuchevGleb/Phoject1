from src.decorators import mask_account_cards
import pytest


def test_mask_account_cards(account_card):

    for key in account_card:
        assert mask_account_cards(str(key[0])) == key[1]
