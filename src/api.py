from fastapi import FastAPI, HTTPException, status
from dependencies import ACCESS_TOKEN_EXPIRE_MINUTES

from datetime import timedelta

from src import schemas, models

from src.authentication import authenticate_user, create_access_token

from src.routers import payment, milk_routes, drivers, transport_costs, producers, auth, deductions, milk_prices

from src.database import engine

models.Base.metadata.create_all(bind=engine)


app = FastAPI()

# Routers
app.include_router(drivers.router)
app.include_router(milk_routes.router)
app.include_router(milk_prices.router)
app.include_router(payment.router)
app.include_router(producers.router)
app.include_router(transport_costs.router)
app.include_router(deductions.router)
app.include_router(auth.router)


@app.get("/")
async def root():
    return {"message": "Hallo Welt!"}
