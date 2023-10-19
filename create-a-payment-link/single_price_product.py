import os
import stripe
from dotenv import load_dotenv

load_dotenv()

stripe.api_key = os.getenv("SK_KEY")


class createProduct:
    def __init__(
        self,
        name: str,
        description: str,
        currency: str,
        unit_amount: float,
        active: bool,
    ) -> None:
        self.name = name
        self.description = description
        self.currency = currency
        self.unit_amount = unit_amount
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
            default_price_data={
                "unit_amount": int(self.unit_amount * 100),
                "currency": self.currency,
                "recurring": {"interval": "month"},
            },
            expand=["default_price"],
        )
        return product

    def main(self):
        product_exists = self.search_product()["data"]
        if product_exists:
            product_id = product_exists[0]["id"]
            price_id = product_exists[0]["default_price"]
            return {"product_id": product_id, "price_id": price_id}

        new_product = self.create_product()
        product_id = new_product["id"]
        price_id = new_product["default_price"]["id"]
        return {"product_id": product_id, "price_id": price_id}


class paymentLink:
    def __init__(self, price_id) -> None:
        self.price_id = price_id

    def create(self):
        payment_link = stripe.PaymentLink.create(
            line_items=[
                {
                    "price": f"{self.price_id}",
                    "quantity": 1,
                    "adjustable_quantity": {"enabled": True},
                }
            ],
            after_completion={
                "type": "redirect",
                "redirect": {"url": "https://example.com"},
            },
        )
        return payment_link

    def deactivate(self, payment_link_id):
        payment_link = stripe.PaymentLink.modify(payment_link_id, active=False)
        return payment_link


product = createProduct(
    name="Basic subscription",
    description="",
    currency="usd",
    unit_amount=199.99,
    active=True,
).main()


payment_link = paymentLink(price_id=product["price_id"]).create()
print(payment_link.url, payment_link.id)


######## Deactivate the payment URL ########

# Ideally you would want to store the payment URL in the database against the URL_ID, PRICE_ID, PRODUCT_ID
# and pass the URL_ID from database to the following function.

# deactivate = paymentLink(price_id=product["price_id"]).deactivate("plink_1O2vtmC5gbIrncpGgA2zYXLs")
