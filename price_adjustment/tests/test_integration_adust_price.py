import pytest
from price_adjustment.adjust_price import price_after_discount, price_after_tax

def test_price_adjustment_integration_discount_taxes():
    expected_output_price = 82.5
    price_discounted = price_after_discount(100.0, 0.25)
    output_price = price_after_tax(price_discounted, 0.1)
    assert output_price == expected_output_price, \
        """Should show that the price is reduced by less than 25%, after taxes
           are applied to the discounted price.
        """
