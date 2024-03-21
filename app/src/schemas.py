from datetime import date
from pydantic import BaseModel
from typing import Optional


class Token(BaseModel):
    access_token: str 
    token_type: str


class TokenData(BaseModel):
    username: str


class User(BaseModel):
    username: str
    email: str
    disabled: bool = False
    hasshed_password: str = None


class UserCreate(BaseModel):
    username: str
    email: str
    password: str


class MilkPrice(BaseModel):
    id: int
    name: str
    price: int
    date: date

    class Config:
        from_attributes = True


class MilkPriceCreate(BaseModel):
    name: str
    price: int
    date: date


class MilkPriceUpdate(BaseModel):
    name: str
    price: int
    date: date


class Deduction(BaseModel):
    id: int
    name: str
    description: str
    price: int
    date: date

    class Config:
        from_attributes = True


class DeductionCreate(BaseModel):
    name: str
    description: str
    price: int
    date: date


class DeductionUpdate(BaseModel):
    name: str
    description: str
    price: int
    date: date


class MilkRoute(BaseModel):
    id: int
    name: str
    description: str
    date: date


class MilkRouteCreate(BaseModel):
    name: str
    description: str
    date: date


class MilkRouteUpdate(BaseModel):
    name: str
    description: str
    date: date


class Driver(BaseModel):
    id: int
    name: str
    phone: str
    date: date

    class Config:
        from_attributes = True


class DriverCreate(BaseModel):
    name: str
    phone: str
    date: date


class DriverUpdate(BaseModel):
    name: str
    phone: str
    date: date


class TransportCost(BaseModel):
    id: int
    cost: int
    name: str
    description: str
    date: date

    class Config:
        from_attributes = True


class TransportCostCreate(BaseModel):
    cost: int
    name: str
    description: str
    date: date


class TransportCostUpdate(BaseModel):
    cost: int
    name: str
    description: str
    date: date


class Producer(BaseModel):
    id: int
    name: str
    description: str
    date: date

    class Config:
        from_attributes = True


class ProducerCreate(BaseModel):
    name: str
    description: str
    phone: str
    date: date


class ProducerUpdate(BaseModel):
    name: str
    description: str


class CollectedMilk(BaseModel):
    id: int
    date: date
    type: str
    quantity: int
    route_id: int
    driver_id: int
    producer_id: int

    class Config:
        from_attributes = True


class CollectedMilkCreate(BaseModel):
    date: date
    type: str
    quantity: int
    route_id: int
    driver_id: int
    producer_id: int


class CollectedMilkUpdate(BaseModel):
    date: date
    type: str
    quantity: int
    route_id: int
    driver_id: int
    producer_id: int


class Payment(BaseModel):
    id: int
    date: date
    amount: int
    deduction_id: int
    transport_cost_id: int
    collected_milk_id: int
    milk_price_id: int

    class Config:
        from_attributes = True


class PaymentCreate(BaseModel):
    date: date
    amount: int
    deduction_id: Optional[int]
    transport_cost_id: Optional[int]
    collected_milk_id: int
    milk_price_id: int


class PaymentUpdate(BaseModel):
    date: date
    amount: int
    deduction_id: Optional[int]
    transport_cost_id: Optional[int]
    collected_milk_id: int

class PaymentsByProducer(BaseModel):
    producer_id: int
    producer_name: str
    total_collected: int
    total_payment: int
    date: date

class CollectedMilkReport(BaseModel):
    producer_id: int
    producer_name: str
    total_collected: float


class CollectedMilkReportByRoute(BaseModel):
    route_id: int
    route_name: str
    milk_quantity: float


class CollectedMilkReportByRouteAndDriver(BaseModel):
    route_id: int
    route_name: str
    driver_name: str
    milk_quantity: float
