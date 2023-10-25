# Coupons specify a fixed value discount.
# You can create customer-facing promotion codes that map to a single underlying coupon.
# This means that the codes `FALLPROMO` and `SPRINGPROMO` can both point to one 25% off coupon.


import os
import stripe
from datetime import datetime
from typing import Optional, List
from dotenv import load_dotenv

load_dotenv()

stripe.api_key = os.getenv("SK_KEY")


class Coupon:
    def __init__(
        self,
        name: str,
        redeem_by: Optional[List[int]],  # taking date input as [year, month, date]
        applies_to_products: List[str],
        percent_off: Optional[float] = None,
        amount_off: Optional[int] = None,
        max_redemptions: int = 100,
        duration: str = "once",
        duration_in_months: Optional[int] = None,
        currency: str = "usd",
    ):
        if percent_off is not None and amount_off is not None:
            raise ValueError(
                "A coupon object has either a percent_off or an amount_off. Not both."
            )

        if duration is "repeating" and duration_in_months is None:
            raise ValueError(
                "duration_in_months needs to be specified for a 'repeating' duration."
            )

        if percent_off is not None and percent_off < 0 or percent_off > 100:
            raise ValueError("Choose a percent_off value in the range(0,100)")

        if redeem_by is not None and len(redeem_by) == 3:
            self.redeem_by = datetime(redeem_by[0], redeem_by[1], redeem_by[2])

        self.name = name
        self.percent_off = percent_off
        self.amount_off = amount_off
        self.duration = duration
        self.duration_in_months = duration_in_months
        self.currency = currency
        self.max_redemptions = max_redemptions
        self.applies_to_products = applies_to_products

    def create_coupon(self):
        try:
            coupon = stripe.Coupon.create(
                name=self.name,
                percent_off=self.percent_off,
                amount_off=self.amount_off,
                duration=self.duration,
                duration_in_months=self.duration_in_months,
                currency=self.currency,
                max_redemtions=self.max_redemptions,
                applies_to=self.applies_to_products,
                redeem_by=self.redeem_by,
            )
            return {"coupon_id": coupon["id"]}
        except Exception:
            raise Exception

    @staticmethod
    def delete_coupon(coupon_id):
        try:
            coupon = stripe.Coupon.delete(coupon_id)
            return coupon
        except Exception:
            raise Exception
