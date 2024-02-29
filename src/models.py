from sqlalchemy import Column, Integer, String, ForeignKey, Date, Boolean
from sqlalchemy.orm import relationship

from .database import Base

# body. These models are used in the path operation function parameters
# and return values
# Path: models.py


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    email = Column(String, index=True)
    disabled = Column(Boolean, index=True)
    hashed_password = Column(String, index=True)


class Token(Base):
    __tablename__ = "token"

    id = Column(Integer, primary_key=True, index=True)
    access_token = Column(String, index=True)
    token_type = Column(String, index=True)


class TokenData(Base):
    __tablename__ = "token_data"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)


class MilkPrice(Base):
    __tablename__ = "milk_price"

    id = Column(Integer, primary_key=True, index=True)
    price = Column(Integer, index=True)
    date = Column(Date, index=True)


class Deduction(Base):
    __tablename__ = "deduction"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    price = Column(Integer, index=True)
    date = Column(Date, index=True)

    # Dependent Relationships
    payment = relationship("Payment", back_populates="deduction")


class MilkRoute(Base):
    __tablename__ = "milk_route"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    date = Column(Date, index=True)

    # Foreign Keys
    collected_milk = relationship("CollectedMilk", back_populates="route")


class Driver(Base):
    __tablename__ = "driver"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    phone = Column(String, index=True)
    date = Column(Date, index=True)

    # Dependent Relationships
    collected_milk = relationship("CollectedMilk", back_populates="driver")


class TransportCost(Base):
    __tablename__ = "transport_cost"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    cost = Column(Integer, index=True)
    date = Column(Date, index=True)

    # Dependent Relationships
    payment = relationship("Payment", back_populates="transport_cost")


class Producer(Base):
    __tablename__ = "producer"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    phone = Column(String, index=True)
    date = Column(Date, index=True)

    # Foreign Keys
    collected_milk = relationship("CollectedMilk", back_populates="producer")


class CollectedMilk(Base):
    __tablename__ = "collected_milk"

    id = Column(Integer, primary_key=True, index=True)
    # Foreign Keys
    driver_id = Column(ForeignKey("driver.id"), index=True)
    route_id = Column(ForeignKey("milk_route.id"), index=True)
    producer_id = Column(ForeignKey("producer.id"), index=True)

    quantity = Column(Integer, ForeignKey("collected_milk.id"), index=True)
    date = Column(Date, index=True)

    # Foreign Key Relationships
    driver = relationship("Driver", back_populates="collected_milk")
    route = relationship("MilkRoute", back_populates="collected_milk")
    producer = relationship("Producer", back_populates="collected_milk")

    # Dependent Relationships
    payment = relationship("Payment", back_populates="collected_milk")


class Payment(Base):
    __tablename__ = "payment"

    id = Column(Integer, primary_key=True, index=True)
    # Foreign Keys
    collected_milk_id = Column(ForeignKey("collected_milk.id"), index=True)
    deduction_id = Column(ForeignKey("deduction.id"), index=True)
    transport_cost_id = Column(ForeignKey("transport_cost.id"), index=True)

    amount = Column(Integer, index=True)
    date = Column(Date, index=True)

    # Foreign Key Relationships
    collected_milk = relationship("CollectedMilk", back_populates="payment")
    transport_cost = relationship("TransportCost", back_populates="payment")
    deduction = relationship("Deduction", back_populates="payment")
