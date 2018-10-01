"""Module containing helper function(s) to find price after discount and/or
   taxes.
"""

def price_after_discount(price, discount_percent):
	"""Function to compute price after discount is applied."""
	return price*(1-discount_percent)
