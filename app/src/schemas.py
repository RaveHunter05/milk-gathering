from datetime import date
from pydantic import BaseModel
from typing import Optional

from decimal import Decimal


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


class Deduction(BaseModel):
    id: int
    name: str
    description: str
    price: Decimal
    date: date

    class Config:
        from_attributes = True


class DeductionCreate(BaseModel):
    name: str
    description: str
    price: Decimal
    date: date


class DeductionUpdate(BaseModel):
    name: str
    description: str
    price: Decimal
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


class Producer(BaseModel):
    id: int
    name: str
    description: str
    phone: str
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

#Cheese Maker

class CheeseMaker(BaseModel):
    id: int
    name: str
    description: str
    phone: str
    date: date

    class Config:
        from_attributes = True


class CheeseMakerUpdate(BaseModel):
    name: str
    description: str
    phone: str
    date: date


class CheeseMakerCreate(BaseModel):
    name: str
    description: str
    phone: str
    date: date


class MilkSelled(BaseModel):
    id: int
    date: date
    quantity: Decimal
    price: Decimal
    cheese_maker_id: int


class MilkSelledCreate(BaseModel):
    date: date
    quantity: Decimal
    price: Decimal
    cheese_maker_id: int


class MilkSelledUpdate(BaseModel):
    id: int
    date: date
    quantity: Decimal
    price: Decimal
    cheese_maker_id: int


class CollectedMilk(BaseModel):
    id: int
    date: date
    quantity: Decimal
    name: str
    price: Decimal
    paid: bool
    route_id: int
    driver_id: int
    producer_id: int

    class Config:
        from_attributes = True


class CollectedMilkCreate(BaseModel):
    date: date
    quantity: Decimal
    name: str
    price: Decimal
    route_id: int
    driver_id: int
    producer_id: int


class CollectedMilkUpdate(BaseModel):
    date: date
    quantity: Decimal
    name: str
    price: Decimal
    route_id: int
    driver_id: int
    producer_id: int


class Payment(BaseModel):
    id: int
    date: date
    total_amount: Decimal
    deduction_id: Optional[int]
    collected_milk_id: int

    class Config:
        from_attributes = True


class PaymentCreate(BaseModel):
    date: date
    total_amount: Decimal
    deduction_id: Optional[int] = None
    collected_milk_id: int


class PaymentUpdate(BaseModel):
    date: date
    total_amount: Decimal
    deduction_id: Optional[int]
    collected_milk_id: int


class LastPaymentsReport(BaseModel):
    producer_id: int
    producer_name: str
    total_collected: int
    total_payment: int
    date: date


class PaymentsByProducer(BaseModel):
    producer_id: int
    producer_name: str
    total_collected: int
    total_payment: int
    date: date


class CollectedMilkReport(BaseModel):
    producer_id: int
    producer_name: str
    total_collected: Decimal


class CollectedMilkReportByRoute(BaseModel):
    route_id: int
    route_name: str
    milk_quantity: Decimal


class CollectedMilkReportByRouteAndDriver(BaseModel):
    route_id: int
    route_name: str
    driver_name: str
    milk_quantity: Decimal


class SelledVsCollectedMilk(BaseModel):
    date: date
    day_of_week: str
    milk_collected: Decimal
    total_price_collected: Decimal
    avg_milk_collected_price: Decimal
    milk_selled: Decimal
    total_price_selled: Decimal
    avg_milk_selled_price: Decimal


class SelledMilkByDate(BaseModel):
    date: date
    day_of_week: str
    milk_price: Decimal
    milk_selled: Decimal
    total_price: Decimal


class CollectedMilkByDate(BaseModel):
    date: date
    day_of_week: str
    milk_price: Decimal
    milk_collected: Decimal
    total_price: Decimal


class CollectedMilkByDateAndRoute(BaseModel):
    date: date
    day_of_week: str
    route_name: str
    milk_collected: Decimal
    total_price_collected: Decimal


class MilkSellsReportByCheeseMaker(BaseModel):
    date: date
    day_of_week: str
    cheese_maker_name: str
    total_milk_selled: Decimal
    total_price_selled: Decimal


class PaymentReportByProducer(BaseModel):
    date: date
    day_of_week: str
    producer_name: str
    total_milk_collected: Decimal
    total_price_collected: Decimal
    total_deduction: Decimal
    total_payment: Decimal
