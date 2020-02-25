"""Module to showcase sample usage of how to adjust price for discounts and
   tax rates.

   - Sample usage:
   python3 main.py 100 .15 -.10
"""

import sys

from price_adjustment.adjust_price import price_adjustment

if __name__ == '__main__':
    # --- Read-in items from command line;
    #     Note: sys.argv[0] stores name of file.
    ITEM_PRICE = float(sys.argv[1])
    TAX_RATE = float(sys.argv[2])
    DISCOUNT = float(sys.argv[3])
    #
    # --- Print them out, for validation:
    print(f"Price of item: {ITEM_PRICE}")
    print(f"Tax rate: {TAX_RATE}")
    print(f"Discount percentage: {DISCOUNT}")
    #
    # --- Compute final cost and print for validation:
    final_price = price_adjustment(
        price_adjustment(ITEM_PRICE, DISCOUNT),
        TAX_RATE)
    print(f"Price after discount and taxes: {round(final_price, 2)}")
