import pytest
import datetime 

from app.shopping_cart import to_usd, total, total_price, tax, get_datetime, now

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


def test_human_friendly_timestamp():
    # display formatted date and time 
    result = get_datetime()
    assert result == now.strftime("%Y-%m-%d, %I:%M %p").center(75, " ")


