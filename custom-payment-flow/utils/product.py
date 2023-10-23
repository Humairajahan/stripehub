import os
import stripe
from dotenv import load_dotenv

load_dotenv("../.env")

stripe.api_key = os.getenv("SK_KEY")


class createProduct:
    def __init__(
        self,
        name: str,
        description: str,
        active: bool = True,
    ) -> None:
        self.name = name
        self.description = description
        self.active = active

    def search_product(self):
        # https://stripe.com/docs/api/products/search
        # https://stripe.com/docs/search#query-fields-for-products

        product = stripe.Product.search(
            query=f"name:'{self.name}'",
        )
        return product

    def create_product(self):
        # https://stripe.com/docs/products-prices/manage-prices?dashboard-or-api=api

        product = stripe.Product.create(
            name=self.name,
        )
        return product

    def main(self):
        product_exists = self.search_product()["data"]
        if product_exists:
            product_id = product_exists[0]["id"]
            return {"product_id": product_id}

        new_product = self.create_product()
        product_id = new_product["id"]
        return {"product_id": product_id}
