import pytest

from app.shopping_cart import to_usd, total_price, selected_id

def test_to_usd():
    # apply to USD formatting
    result = to_usd(3.50)
    assert result == "$3.50"

    # display two decimal places
    result = to_usd(3.5)
    assert result == "$3.50"

    # round to two decimal places
    result = to_usd(3.666)
    assert result == "$3.67"

    # display thousand separators
    result = to_usd(111222333.445)
    assert result == "$111,222,333.45"


#def test_human_friendly_timestamp():

def test_find_product():
    result = selected_id(2)
    assert result == "Name: All-Seasons Salt | Price: $4.99"

def test_calculate_total_price():
    result = total_price(100)
    assert result == 106