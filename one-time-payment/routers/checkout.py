import os
import sys
import json
import stripe
from fastapi import APIRouter, HTTPException
from fastapi.responses import RedirectResponse

sys.path.insert(0, "../utils")
from utils.models import Checkout
from dotenv import load_dotenv

load_dotenv("../.env")

stripe.api_key = os.getenv("SK_KEY")
DOMAIN_NAME = os.getenv("DOMAIN_NAME")


router = APIRouter()


@router.post(
    "/user/create-checkout-session"
)  # , response_class=RedirectResponse, status_code=303)
async def create_checkout_session(request: Checkout):

    # Once customer adds a product to their cart and confirms the cart (hit this endpoint),
    # the backend then checks for the products' price ids against the database
    # and redirects them to a stripe hosted page for payment.

    # Once you attach this url to frontend, you would want to comment the response_class methods back in.

    try:
        line_items = [
            {"price": product.price, "quantity": product.quantity}
            for product in request.line_items
        ]

        checkout_session = stripe.checkout.Session.create(
            line_items=line_items,
            discounts=[{"coupon": request.coupon_id}],
            mode="payment",
            success_url=f"{DOMAIN_NAME}/success.html",
            cancel_url=f"{DOMAIN_NAME}/cancel.html",
        )
    except Exception as e:
        raise HTTPException(status_code=503, detail=str(e))

    return checkout_session.url
