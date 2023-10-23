from fastapi import FastAPI
from routers import prices, payment_intent, webhook

app = FastAPI()

app.include_router(prices.router)
app.include_router(payment_intent.router)
app.include_router(webhook.router)
