import os
import sys
import stripe
from fastapi import APIRouter, Header, HTTPException, status
from fastapi.responses import JSONResponse
from typing import Optional

sys.path.insert(0, "../utils")
from utils.models import WebHookData
from dotenv import load_dotenv

load_dotenv("../.env")

stripe.api_key = os.getenv("SK_KEY")
WEBHOOK_SECRET = os.getenv("WHSEC")

router = APIRouter()


@router.post("/webhook")
async def webhook_received(
    request: WebHookData, stripe_signature: Optional[str] = Header(None)
):
    # https://stripe.com/docs/webhooks/quickstart

    try:
        event = stripe.Webhook.construct_event(
            payload=request, sig_header=stripe_signature, secret=WEBHOOK_SECRET
        )
    except Exception as e:
        raise HTTPException(status_code=503, detail=str(e))

    # https://stripe.com/docs/payments/accept-a-payment?platform=web&ui=elements#web-post-payment

    if event and event["type"] == "payment_intent.succeeded":
        payment_intent = event["data"]["object"]
        print("Payment for {} succeeded".format(payment_intent["amount"]))
        return JSONResponse(status_code=200, content={"payment intent succeeded"})

    elif event["type"] == "payment_method.attached":
        payment_method = event["data"]["object"]
        return JSONResponse(status_code=200, content={f"payment intent attached: {payment_method}"})
    else:
        print("Unhandled event type {}".format(event["type"]))
        raise HTTPException(status_code=503, detail="Unhandled event type ")
