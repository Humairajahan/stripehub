import os
import stripe
from dotenv import load_dotenv

load_dotenv()

stripe.api_key = os.getenv("SK_KEY")


class createPricingModel:
    def __init__(
        self, product_id, pricing_model_name, unit_amount, currency, recurring
    ):
        self.product_id = product_id
        self.pricing_model_name = pricing_model_name
        self.unit_amount = unit_amount
        self.currency = currency
        self.recurring = recurring

    # def search_pricing_model(self):
    #     # Search through database to check if pricing model exists already.

    def create_pricing_model(self):
        # https://stripe.com/docs/products-prices/manage-prices?dashboard-or-api=api

        price = stripe.Price.create(
            product=self.product_id,
            nickname=self.pricing_model_name,
            unit_amount=int(self.unit_amount * 100),
            currency=self.currency,
            recurring={"interval": self.recurring},
        )
        return {"price_id": price["id"]}

    # def main(self):
    #     # Implement after database has been integrated.
    #     price_exists = ...
    #     if price_exists:
    #         price_id = ...
    #         return {"price_id": price_id}
    #     new_price = self.create_pricing_model()
    #     price_id = ...
    #     return {"price_id": price_id}
