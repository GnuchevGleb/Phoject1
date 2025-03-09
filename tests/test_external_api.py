from unittest.mock import patch

from src.external_api import currency_exchange_rate


@patch("requests.get")
def test_currency_exchange_rate(mock_get_usd):
    """
    функция Mock для API обращение к серверу обмена валют для USD
    """
    mock_get_usd.return_value.json.return_value = {
        "base": "USD",
        "date": "2025-03-04",
        "rates": {"RUB": 89.693521},
        "success": True,
        "timestamp": 1741115232,
    }

    assert currency_exchange_rate("USD") == 89.693521
    mock_get_usd.assert_called()


@patch("requests.get")
def test_currency_exchange_rate_1(mock_get_eur):
    """
    функция Mock для API обращение к серверу обмена валют для EUR
    """
    mock_get_eur.return_value.json.return_value = {
        "base": "EUR",
        "date": "2025-03-04",
        "rates": {"RUB": 89.693521},
        "success": True,
        "timestamp": 1741115464,
    }
    assert currency_exchange_rate("EUR") == 89.693521
    mock_get_eur.assert_called()
