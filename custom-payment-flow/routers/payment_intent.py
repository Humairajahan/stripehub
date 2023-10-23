import os
import stripe
from fastapi import APIRouter, Request, HTTPException
from dotenv import load_dotenv

load_dotenv("../.env")

stripe.api_key = os.getenv("SK_KEY")

router = APIRouter()


@router.post("/user/create-payment-intent")
async def create_payment_intent(request: Request):
    try:
        payment_intent = stripe.PaymentIntent.create(
            amount=int(request.items * 100),
            currency=request.currency,
            automatic_payment_methods={"enabled": True},
        )
        return {"client_secret": payment_intent["client_secret"]}
    except Exception as e:
        raise HTTPException(status_code=503, detail=str(e))
