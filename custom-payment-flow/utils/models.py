from typing import List
from pydantic import BaseModel, constr


class Product(BaseModel):
    name: str
    description: str


class PricingModel(BaseModel):
    name: str
    unit_amount: float
    currency: constr(regex="^(usd|eur|inr)$")
    recurring: constr(regex="^(month|year)$")


class ProductPriceCreation(BaseModel):
    product: Product
    price_data: List[PricingModel]


class WebHookData(BaseModel):
    data: dict
    type: str
    