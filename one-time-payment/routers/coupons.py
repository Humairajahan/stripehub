import os
import sys
import stripe
from fastapi import APIRouter

sys.path.insert(0, "../utils")
from utils.models import CreateCoupon, DeleteCoupon
from utils.coupons import Coupon
from dotenv import load_dotenv

load_dotenv("../.env")

stripe.api_key = os.getenv("SK_KEY")


router = APIRouter()


@router.post("/admin/create-coupon")
async def create_coupon(request: CreateCoupon):
    coupon = Coupon(
        name=request.name,
        redeem_by=request.redeem_by,
        applies_to_products=request.applies_to_products,
        percent_off=request.percent_off,
        amount_off=request.amount_off,
        max_redemptions=request.max_redemptions,
        duration=request.duration,
        duration_in_months=request.duration_in_months,
        currency=request.currency,
    ).create_coupon()
    return coupon


@router.delete("/admin/delete-coupon")
async def delete_a_coupon(coupon_id: str):
    coupon = Coupon.delete_coupon(coupon_id=coupon_id)
    return coupon
