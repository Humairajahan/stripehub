from typing import List, Optional
from pydantic import BaseModel, constr


class Product(BaseModel):
    name: str
    description: str


class PricingModel(BaseModel):
    name: str
    unit_amount: float
    currency: constr(regex="^usd$")


class ProductPriceCreation(BaseModel):
    product: Product
    price_data: List[PricingModel]
    
    
class ProductsForCheckout(BaseModel):
    price: str
    quantity: int
    
    
class Checkout(BaseModel):
    line_items: List[ProductsForCheckout]
    coupon_id: Optional[str] = None
    
    
class CouponRedeemByYr(BaseModel):
    year: int
    
    
class CouponRedeemByMonth(BaseModel):
    month: int
    
    
class CouponRedeemByDay(BaseModel):
    day: int
    
    
class CreateCoupon(BaseModel):
    name: str
    duration: constr(regex="^once|repeating|forever$")
    currency: constr(regex="^usd$")
    applies_to_products: List[str] 
    percent_off: Optional[float]
    amount_off: Optional[int]
    duration_in_months: Optional[int]
    max_redemptions: Optional[int]
    redeem_by: Optional[List[CouponRedeemByYr, CouponRedeemByMonth, CouponRedeemByDay]]
