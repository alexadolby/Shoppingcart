import pytest

from app.shopping_cart import to_usd, total, total_price, tax

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
    result = to_usd(111222333.45)
    assert result == "$111,222,333.45"


#def test_human_friendly_timestamp():

#def test find_product():

#def test_calculate_total():
   # total = total_price(100) + tax
    #assert result == 106