from sqlalchemy.orm import Session

from sqlalchemy.sql import func

from . import models, schemas


# Milk Price
def get_milk_price(db: Session, milk_price_id: int):
    return (
            db.query(models.MilkPrice).filter(models.MilkPrice.id == milk_price_id).first()
            )


def get_milk_prices(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.MilkPrice).offset(skip).limit(limit).all()


def create_milk_price(db: Session, milk_price: schemas.MilkPriceCreate):
    db_milk_price = models.MilkPrice(price=milk_price.price, name=milk_price.name, date=milk_price.date)
    db.add(db_milk_price)
    db.commit()
    db.refresh(db_milk_price)
    return db_milk_price


def update_milk_price(db: Session, milk_price: schemas.MilkPriceUpdate):
    milk_price = db.query(models.MilkPrice).filter_by(id=milk_price.id).first()
    milk_price.price = milk_price.price
    db.commit()
    return milk_price


# Deduction
def get_deduction(db: Session, deduction_id: int):
    return (
            db.query(models.Deduction).filter(models.Deduction.id == deduction_id).first()
            )


def get_deductions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Deduction).offset(skip).limit(limit).all()


def create_deduction(db: Session, deduction: schemas.DeductionCreate):
    db_deduction = models.Deduction(
            name=deduction.name,
            description=deduction.description,
            price=deduction.price,
            date=deduction.date,
            )
    db.add(db_deduction)
    db.commit()
    db.refresh(db_deduction)
    return db_deduction


def update_deduction(db: Session, deduction: schemas.DeductionUpdate):
    deduction = db.query(models.Deduction).filter_by(id=deduction.id).first()
    deduction.name = deduction.name
    deduction.description = deduction.description
    deduction.price = deduction.price
    db.commit()
    return deduction


# Milk Route
def get_route(db: Session, route_id: int):
    return db.query(models.MilkRoute).filter(models.MilkRoute.id == route_id).first()


def get_routes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.MilkRoute).offset(skip).limit(limit).all()


def create_route(db: Session, route: schemas.MilkRouteCreate):
    route = models.MilkRoute(
            name=route.name, description=route.description, date=route.date
            )
    db.add(route)
    db.commit()
    db.refresh(route)
    return route


def update_route(db: Session, item_id: str, route: schemas.MilkRouteUpdate):
    item = db.query(models.MilkRoute).filter_by(id=item_id).first()
    item.name = route.name
    item.description = route.description
    db.commit()
    return item


def delete_route(db: Session, route_id: int):
    db_route = (
            db.query(models.MilkRoute).filter(models.MilkRoute.id == route_id).first()
            )
    db.delete(db_route)
    db.commit()
    return db_route

# Driver
def get_driver(db: Session, driver_id: int):
    return db.query(models.Driver).filter(models.Driver.id == driver_id).first()


def get_drivers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Driver).offset(skip).limit(limit).all()


def create_driver(db: Session, driver: schemas.DriverCreate):
    db_driver = models.Driver(name=driver.name, phone=driver.phone, date=driver.date)
    db.add(db_driver)
    db.commit()
    db.refresh(db_driver)
    return db_driver


def update_driver(db: Session, driver: schemas.DriverUpdate):
    driver = db.query(models.Driver).filter_by(id=driver.id).first()
    driver.name = driver.name
    driver.phone = driver.phone
    db.commit()
    return driver


# Transport Cost
def get_transport_cost(db: Session, transport_cost_id: int):
    return (
            db.query(models.TransportCost)
            .filter(models.TransportCost.id == transport_cost_id)
            .first()
            )


def get_transport_costs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.TransportCost).offset(skip).limit(limit).all()


def create_transport_cost(db: Session, transport_cost: schemas.TransportCostCreate):
    db_transport_cost = models.TransportCost(
            name=transport_cost.name, description=transport_cost.description,
            cost=transport_cost.cost, date=transport_cost.date
            )
    db.add(db_transport_cost)
    db.commit()
    db.refresh(db_transport_cost)
    return db_transport_cost


def update_transport_cost(db: Session, transport_cost: schemas.TransportCostUpdate):
    transport_cost = (
            db.query(models.TransportCost).filter_by(id=transport_cost.id).first()
            )
    transport_cost.cost = transport_cost.Cost
    transport_cost.name = transport_cost.name
    transport_cost.description = transport_cost.description
    db.commit()
    db.commit()
    return transport_cost


# Producer
def get_producer(db: Session, producer_id: int):
    return db.query(models.Producer).filter(models.Producer.id == producer_id).first()


def get_producers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Producer).offset(skip).limit(limit).all()


def create_producer(db: Session, producer: schemas.ProducerCreate):
    db_producer = models.Producer(name=producer.name, description=producer.description, phone=producer.phone, date=producer.date)
    db.add(db_producer)
    db.commit()
    db.refresh(db_producer)
    return db_producer


def update_producer(db: Session, producer: schemas.ProducerUpdate):
    producer = db.query(models.Producer).filter_by(id=producer.id).first()
    producer.name = producer.name
    producer.description = producer.description
    db.commit()
    return producer


# Payment
def get_payment(db: Session, payment_id: int):
    return db.query(models.Payment).filter(models.Payment.id == payment_id).first()


def get_payments(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Payment).offset(skip).limit(limit).all()


def create_payment(db: Session, payment: schemas.PaymentCreate):
    db_payment = models.Payment(amount=payment.amount, date=payment.date, deduction_id=payment.deduction_id, transport_cost_id=payment.transport_cost_id, collected_milk_id=payment.collected_milk_id, milk_price_id=payment.milk_price_id)
    db.add(db_payment)
    db.commit()
    db.refresh(db_payment)
    return db_payment

# Collected Milk
def get_collected_milk(db: Session, collected_milk_id: int):
    return (
            db.query(models.CollectedMilk)
            .filter(models.CollectedMilk.id == collected_milk_id)
            .first()
            )


def get_collected_milks(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.CollectedMilk).offset(skip).limit(limit).all()


def create_collected_milk(db: Session, collected_milk: schemas.CollectedMilkCreate):
    db_collected_milk = models.CollectedMilk(
            quantity=collected_milk.quantity, date=collected_milk.date, type=collected_milk.type,
            route_id=collected_milk.route_id, driver_id=collected_milk.driver_id, producer_id=collected_milk.producer_id
            )
    db.add(db_collected_milk)
    db.commit()
    db.refresh(db_collected_milk)
    return db_collected_milk


def update_collected_milk(db: Session, collected_milk: schemas.CollectedMilkUpdate):
    db_collected_milk = models.CollectedMilk(
            quantity=collected_milk.quantity, date=collected_milk.date
            )
    db.add(db_collected_milk)
    db.commit()
    db.refresh(db_collected_milk)
    return db_collected_milk

# Reports

def get_collected_milk_report_by_date(
        db: Session, start_date: str, end_date: str
        ):
    return (
            db.query(models.CollectedMilk)
            .filter(models.CollectedMilk.date >= start_date)
            .filter(models.CollectedMilk.date <= end_date)
            .group_by(models.CollectedMilk.route_id)
            .all()
            )

def get_payments_report_by_date(
        db: Session, start_date: str, end_date: str
        ):
    return (
            db.query(models.Payment)
            .join(models.CollectedMilk, models.Payment.collected_milk_id == models.CollectedMilk.id)
            .filter(models.Payment.date >= start_date)
            .filter(models.Payment.date <= end_date)
            .all()
            )

def get_collected_report_by_producer_and_date(
        db: Session, start_date: str, end_date: str
        ):
    result = db.query(models.CollectedMilk.producer_id, func.max(models.CollectedMilk.quantity).label("max_quantity"),
                      func.sum(models.CollectedMilk.quantity).label("total_quantity")) .group_by(models.CollectedMilk.producer_id) .all()
    return (
            result
            )
