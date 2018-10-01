"""Module for unit, regression and paramterized testing of 'adjust_price'
   functions.
"""
from price_adjustment.adjust_price import price_after_discount, price_after_tax
import math
ROUND_OFF_ERROR = 0.001

def test_price_adjustment_discount():
    """Unit test to showcase functionality of applying a discount to an item's
       price.
    """
    expected_output_price = 75.0
    output_price = price_after_discount(100.0, 0.25)
    assert math.fabs(output_price - expected_output_price) < ROUND_OFF_ERROR, \
        """Should show that the price is now reduced by 25%."""


def test_price_adjustment_tax():
    """Unit test to showcase functionality of applying a tax rate to an item's
       price.
    """
    expected_output_price = 110.0
    output_price = price_after_tax(100.0, 0.10)
    assert math.fabs(output_price - expected_output_price) < ROUND_OFF_ERROR, \
        """Should show that the price is now increased by 10%."""


def test_price_adjustment_discount_throws_error_price_below_zero():
    """Unit test to showcase edge case behavior of throwing an error when
       the final price of the item after discount is less than 0.
    """
    with pytest.raises(ValueError):
        price_after_discount(100.0, 1.25)
