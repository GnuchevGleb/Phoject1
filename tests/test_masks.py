from src.masks import get_mask_account, get_mask_card_number


def test_mask_cart(account_card):

    for key in account_card:
        if "Maestro" in key[0]:

            assert str(get_mask_card_number((key[0][-16:])) == str(key[1][-16:]))

        if "MasterCard" in key[0]:

            assert str(get_mask_card_number((key[0][-16:])) == str(key[1][-19:]))


def test_get_mask_account(account_card):

    for key in account_card:

        if "Счет" in key[0]:

            assert str(get_mask_account((key[0][-20:])) == str(key[1][-6:]))
