import os
import sys
import stripe
from fastapi import APIRouter

sys.path.insert(0, "../utils")
from utils.models import ProductPriceCreation
from utils.product import createProduct
from utils.price import createPricingModel
from dotenv import load_dotenv

load_dotenv("../.env")

stripe.api_key = os.getenv("SK_KEY")


router = APIRouter()


@router.post("/admin/subscription-package")
async def create_subscription_package(request: ProductPriceCreation):
    product = createProduct(
        name=request.product.name, description=request.product.description
    ).main()

    response = []
    package_list = request.price_data
    for package in package_list:
        price = createPricingModel(
            product_id=product["product_id"],
            pricing_model_name=package.name,
            unit_amount=package.unit_amount,
            currency=package.currency,
            recurring=package.recurring,
        ).create_pricing_model()

        resp = {
            "product_id": product["product_id"],
            "price_id": price["price_id"],
            "pricing_model_name": package.name,
            "unit_amount": package.unit_amount,
            "currency": package.currency,
            "recurring": package.recurring,
        }
        response.append(resp)
    return response
