from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from mangum import Mangum

from app.src import models

from app.src.routers import payment, milk_routes, drivers, transport_costs, producers, auth, deductions, milk_prices, reports, collected_milks

from app.src.database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(drivers.router)
app.include_router(milk_routes.router)
app.include_router(milk_prices.router)
app.include_router(collected_milks.router)
app.include_router(payment.router)
app.include_router(producers.router)
app.include_router(transport_costs.router)
app.include_router(deductions.router)
app.include_router(reports.router)
app.include_router(auth.router)


@app.get("/")
async def root():
    return {"message": "Hallo Welt!"}

handler = Mangum(app)
