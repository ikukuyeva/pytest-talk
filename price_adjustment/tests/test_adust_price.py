from price_adjustment.adjust_price import price_after_discount, price_after_tax

def test_price_adjustment_discount():
	expected_output_price = 75.0
	output_price = price_after_discount(100.0, 0.25)
	assert output_price == expected_output_price, \
		"""Should show that the price is now reduced by 25%."""

def test_price_adjustment_discount_throws_error_price_below_zero():
	with pytest.raises(ValueError):
		price_after_discount(100.0, 1.25)
