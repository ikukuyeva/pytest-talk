"""Module containing helper function(s) to find price after discount and/or
   taxes.
"""
import math

def price_after_discount(price, discount_percent):
	"""Function to compute price after discount is applied."""
	if discount_percent > 1:
		raise ValueError("Error: Discount is more than 100%.")
	else:	
		return price * (1 - discount_percent)


def price_after_tax(price, tax_percent):
	"""Function to compute price after taxes are included."""
	return price * (1 + tax_percent)


def price_adjustment(price, adjustment):
	if math.fabs(adjustment) > 1:
		raise ValueError("Error: Adjustment is more than 100% of price.")
	else:
		return price * (1 + adjustment)
