import pytest

from app.shopping_cart import to_usd, total_price

def test_to_usd():
    # apply to USD formatting
    assert to_usd(3.50) == "$3.50"

    # display two decimal places
    assert to_usd(3.5) == "$3.50"

    # round to two decimal places
    assert to_usd(3.666) == "$3.67"

    # display thousand separators
    assert to_usd(111222333.445) == "$111,222,333.45"


def test_human_friendly_timestamp():

def test_find_product():

def test_calculate_total_price():
    assert total_price