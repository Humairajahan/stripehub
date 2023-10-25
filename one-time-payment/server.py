from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import prices, checkout, coupons

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(prices.router)
app.include_router(checkout.router)
app.include_router(coupons.router)


################################################################
# [
#   {
#     "product_id": "prod_OsoL8PfUPfJTlY",
#     "price_id": "price_1O52iYC5gbIrncpGWiz0UguL",
#     "pricing_model_name": "monthly",
#     "unit_amount": 20,
#     "currency": "usd"
#   },
#   {
#     "product_id": "prod_OsoL8PfUPfJTlY",
#     "price_id": "price_1O52iZC5gbIrncpGA0S6srns",
#     "pricing_model_name": "yearly",
#     "unit_amount": 220,
#     "currency": "usd"
#   }
# ]
################################################################