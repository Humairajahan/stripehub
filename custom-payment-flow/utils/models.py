from typing import List
from pydantic import BaseModel, constr


class PricingModel(BaseModel):
    unit_amount: float
    currency: constr(regex="^(usd|eur|inr)$")
    recurring: constr(regex="^(monthly|half-yearly|yearly)$")


class PriceCreation(BaseModel):
    product_id: str
    price_data: List[PricingModel]
