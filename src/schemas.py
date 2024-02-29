from datetime import date
from pydantic import BaseModel


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
    price: int
    date: date

    class Config:
        orm_mode = True


class MilkPriceCreate(BaseModel):
    price: int
    date: date


class MilkPriceUpdate(BaseModel):
    price: int
    date: date


class Deduction(BaseModel):
    id: int
    name: str
    description: str
    price: int
    date: date

    class Config:
        orm_mode = True


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
        orm_mode = True


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
        orm_mode = True


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

    class Config:
        orm_mode = True


class ProducerCreate(BaseModel):
    name: str
    description: str


class ProducerUpdate(BaseModel):
    name: str
    description: str


class CollectedMilk(BaseModel):
    id: int
    date: date
    amount: int
    fat: int
    snf: int
    rate: int
    total: int
    route_id: int
    driver_id: int

    class Config:
        orm_mode = True


class CollectedMilkCreate(BaseModel):
    date: date
    amount: int
    fat: int
    snf: int
    rate: int
    total: int
    route_id: int
    driver_id: int


class CollectedMilkUpdate(BaseModel):
    date: date
    amount: int
    fat: int
    snf: int
    rate: int
    total: int
    route_id: int
    driver_id: int


class Payment(BaseModel):
    id: int
    date: date
    amount: int
    deduction_id: int
    transport_cost_id: int
    collected_milk_id: int

    class Config:
        orm_mode = True


class PaymentCreate(BaseModel):
    date: date
    amount: int
    deduction_id: int
    transport_cost_id: int
    collected_milk_id: int


class PaymentUpdate(BaseModel):
    date: date
    amount: int
    deduction_id: int
    transport_cost_id: int
    collected_milk_id: int
