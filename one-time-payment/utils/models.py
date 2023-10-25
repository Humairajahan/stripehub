from typing import List
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