from fastapi import FastAPI
from routers import prices

app = FastAPI()

app.include_router(prices.router)
