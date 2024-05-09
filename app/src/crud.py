from sqlalchemy.orm import Session

from sqlalchemy.sql import func, extract

from sqlalchemy import desc

from datetime import datetime, timedelta

from . import models, schemas


# Deduction
def get_deduction(db: Session, deduction_id: int):
    return (
        db.query(models.Deduction).filter(models.Deduction.id == deduction_id).first()
    )


def get_deductions(db: Session, skip: int = 0, limit: int = 100):
    return (
        db.query(models.Deduction)
        .filter(models.Deduction.paid == False)
        .order_by(desc(models.Deduction.date))
        .offset(skip)
        .limit(limit)
        .all()
    )


def create_deduction(db: Session, deduction: schemas.DeductionCreate):
    db_deduction = models.Deduction(
        name=deduction.name,
        description=deduction.description,
        price=deduction.price,
        date=deduction.date,
        paid=False,
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
    return (
        db.query(models.MilkRoute)
        .order_by(desc(models.MilkRoute.date))
        .offset(skip)
        .limit(limit)
        .all()
    )


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
    return (
        db.query(models.Driver)
        .order_by(desc(models.Driver.date))
        .offset(skip)
        .limit(limit)
        .all()
    )


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


# Producer
def get_producer(db: Session, producer_id: int):
    return db.query(models.Producer).filter(models.Producer.id == producer_id).first()


def get_producers(db: Session, skip: int = 0, limit: int = 100):
    return (
        db.query(models.Producer)
        .order_by(desc(models.Producer.date))
        .offset(skip)
        .limit(limit)
        .all()
    )


def create_producer(db: Session, producer: schemas.ProducerCreate):
    db_producer = models.Producer(
        name=producer.name,
        description=producer.description,
        phone=producer.phone,
        date=producer.date,
    )
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


# CheeeseMaker


def get_cheese_maker(db: Session, cheese_maker_id: int):
    return (
        db.query(models.CheeseMaker)
        .filter(models.CheeseMaker.id == cheese_maker_id)
        .first()
    )


def get_cheese_makers(db: Session, skip: int = 0, limit: int = 100):
    return (
        db.query(models.CheeseMaker)
        .order_by(desc(models.CheeseMaker.date))
        .offset(skip)
        .limit(limit)
        .all()
    )


def create_cheese_maker(db: Session, cheese_maker: schemas.CheeseMakerCreate):
    db_cheese_maker = models.CheeseMaker(
        name=cheese_maker.name,
        description=cheese_maker.description,
        phone=cheese_maker.phone,
        date=cheese_maker.date,
    )
    db.add(db_cheese_maker)
    db.commit()
    db.refresh(db_cheese_maker)
    return db_cheese_maker


def update_cheese_maker(db: Session, updated_cheese_maker: schemas.CheeseMakerUpdate):
    updated_cheese_maker = (
        db.query(models.CheeseMaker).filter_by(id=updated_cheese_maker.id).first()
    )
    updated_cheese_maker.name = updated_cheese_maker.name
    updated_cheese_maker.description = updated_cheese_maker.description
    updated_cheese_maker.phone = updated_cheese_maker.phone
    db.commit()
    return updated_cheese_maker


# Milk Selled


def get_milk_selled(db: Session, milk_selled_id: int):
    return (
        db.query(models.MilkSelled)
        .filter(models.MilkSelled.id == milk_selled_id)
        .first()
    )


def get_milk_selleds(db: Session, skip: int = 0, limit: int = 100):
    return (
        db.query(models.MilkSelled)
        .order_by(desc(models.MilkSelled.date))
        .offset(skip)
        .limit(limit)
        .all()
    )


def create_milk_selled(db: Session, milk_selled: schemas.MilkSelledCreate):
    db_milk_selled = models.MilkSelled(
        quantity=milk_selled.quantity,
        date=milk_selled.date,
        price=milk_selled.price,
        cheese_maker_id=milk_selled.cheese_maker_id,
    )
    db.add(db_milk_selled)
    db.commit()
    db.refresh(db_milk_selled)
    return db_milk_selled


def update_milk_selled(db: Session, milk_selled: schemas.MilkSelledUpdate):
    db_milk_selled = db.query(models.MilkSelled).filter_by(id=milk_selled.id).first()
    db_milk_selled.date = milk_selled.date
    db_milk_selled.quantity = milk_selled.quantity
    db_milk_selled.price = milk_selled.price
    db_milk_selled.cheese_maker_id = milk_selled.cheese_maker_id

    db.commit()
    return db_milk_selled


# Payment
def get_payment(db: Session, payment_id: int):
    return db.query(models.Payment).filter(models.Payment.id == payment_id).first()


def get_payments(db: Session, skip: int = 0, limit: int = 100):
    return (
        db.query(models.Payment)
        .order_by(desc(models.Payment.date))
        .offset(skip)
        .limit(limit)
        .all()
    )


def create_payment(db: Session, payment: schemas.PaymentCreate):
    db_payment = models.Payment(
        total_amount=payment.total_amount,
        date=payment.date,
        deduction_id=payment.deduction_id,
        collected_milk_id=payment.collected_milk_id,
    )

    current_collected = db.query(models.CollectedMilk).filter_by(id=payment.collected_milk_id).first()
    if current_collected:
        current_collected.paid = True

    current_deduction = db.query(models.Deduction).filter_by(id=payment.deduction_id).first()
    if current_deduction:
        current_deduction.paid = True

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
    return (
        db.query(models.CollectedMilk)
        .filter(models.CollectedMilk.paid == False)
        .order_by(desc(models.CollectedMilk.date))
        .offset(skip)
        .limit(limit)
        .all()
    )


def create_collected_milk(db: Session, collected_milk: schemas.CollectedMilkCreate):
    db_collected_milk = models.CollectedMilk(
        quantity=collected_milk.quantity,
        name=collected_milk.name,
        price=collected_milk.price,
        date=collected_milk.date,
        route_id=collected_milk.route_id,
        driver_id=collected_milk.driver_id,
        producer_id=collected_milk.producer_id,
        paid=False,
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


def get_last_payments_report(db: Session):
    return (
        db.query(
            models.Payment,
            models.CollectedMilk.producer_id,
            models.Producer.name.label("producer_name"),
            func.sum(models.CollectedMilk.quantity).label("total_collected"),
            func.sum(models.Payment.total_amount).label("total_payment"),
            models.Payment.date,
        )
        .join(
            models.CollectedMilk,
            models.Payment.collected_milk_id == models.CollectedMilk.id,
        )
        .join(models.Producer, models.CollectedMilk.producer_id == models.Producer.id)
        .group_by(
            models.Payment.collected_milk_id,
            models.Producer.name,
            models.Payment.id,
            models.Payment.date,
            models.CollectedMilk.producer_id,
        )
        .order_by(desc(models.Payment.date))
        .limit(10)
        .all()
    )


def get_payments_report_by_date(db: Session, start_date: str, end_date: str):
    return (
        db.query(
            models.Payment,
            models.CollectedMilk.producer_id,
            models.Producer.name.label("producer_name"),
            func.sum(models.CollectedMilk.quantity).label("total_collected"),
            func.sum(models.Payment.amount).label("total_payment"),
            models.Payment.date,
        )
        .join(
            models.CollectedMilk,
            models.Payment.collected_milk_id == models.CollectedMilk.id,
        )
        .join(models.Producer, models.CollectedMilk.producer_id == models.Producer.id)
        .filter(models.Payment.date >= start_date)
        .filter(models.Payment.date <= end_date)
        .filter(models.Payment.amount > 0)
        .group_by(
            models.Payment.collected_milk_id,
            models.Producer.name,
            models.Payment.id,
            models.Payment.date,
            models.CollectedMilk.producer_id,
        )
        .all()
    )


def get_collected_report_by_producer_and_date(
    db: Session, start_date: str, end_date: str
):
    return (
        db.query(
            models.CollectedMilk.producer_id,
            models.Producer.name.label("producer_name"),
            func.sum(models.CollectedMilk.quantity).label("total_collected"),
        )
        .join(models.CollectedMilk.producer)
        .filter(models.CollectedMilk.date >= start_date)
        .filter(models.CollectedMilk.date <= end_date)
        .filter(models.CollectedMilk.quantity > 0)
        .group_by(models.CollectedMilk.producer_id, models.Producer.name)
        .all()
    )


def get_collected_milk_by_route_driver_and_date(
    db: Session, start_date: str, end_date: str
):
    return (
        db.query(
            models.CollectedMilk.route_id,
            models.MilkRoute.name.label("route_name"),
            func.sum(models.CollectedMilk.quantity).label("milk_quantity"),
            models.Driver.name.label("driver_name"),
        )
        .join(models.CollectedMilk.route)
        .join(models.CollectedMilk.driver)
        .filter(models.CollectedMilk.date >= start_date)
        .filter(models.CollectedMilk.date <= end_date)
        .group_by(
            models.CollectedMilk.route_id, models.MilkRoute.name, models.Driver.name
        )
        .all()
    )


def get_collected_milk_by_route_and_date(db: Session, start_date: str, end_date: str):
    return (
        db.query(
            models.CollectedMilk.route_id,
            models.MilkRoute.name.label("route_name"),
            func.sum(models.CollectedMilk.quantity).label("milk_quantity"),
        )
        .join(models.CollectedMilk.route)
        .filter(models.CollectedMilk.date >= start_date)
        .filter(models.CollectedMilk.date <= end_date)
        .filter(models.CollectedMilk.quantity > 0)
        .group_by(models.CollectedMilk.route_id, models.MilkRoute.name)
        .all()
    )

def get_collected_milk_report_by_date(db: Session, start_date: str, end_date: str):
    start_datetime = datetime.strptime(start_date, "%Y-%m-%d")
    end_datetime = datetime.strptime(end_date, "%Y-%m-%d")

    if (end_datetime - start_datetime).days > 7:
        return []

    daily_reports = []

    current_datetime = start_datetime

    while current_datetime <= end_datetime:
        current_date_str = current_datetime.strftime("%Y-%m-%d")

        daily_report = (
            db.query(
                models.CollectedMilk.date,
                func.round(func.avg(models.CollectedMilk.price), 2).label("milk_price"),
                func.sum(models.CollectedMilk.quantity).label("milk_collected"),
                func.sum(models.CollectedMilk.price * models.CollectedMilk.quantity).label(
                    "total_price"
                ),
            )
            .filter(models.CollectedMilk.date == current_date_str)
            .group_by(models.CollectedMilk.date)
            .all()
        )

        if daily_report == []:
            daily_report = {
                "date": current_date_str,
                "day_of_week": current_datetime.strftime("%A"),
                "milk_price": 0,
                "milk_collected": 0,
                "total_price": 0,
            }
        else:
            daily_report = {
                "date": current_date_str,
                "day_of_week": current_datetime.strftime("%A"),
                "milk_price": daily_report[0][1],
                "milk_collected": daily_report[0][2],
                "total_price": daily_report[0][3],
            }

        daily_reports.append(daily_report)

        current_datetime += timedelta(days=1)

    return daily_reports


def get_selled_milk_report_by_date(db: Session, start_date: str, end_date: str):
    # Convert start_date and end_date strings to datetime objects
    start_datetime = datetime.strptime(start_date, "%Y-%m-%d")
    end_datetime = datetime.strptime(end_date, "%Y-%m-%d")

    if (end_datetime - start_datetime).days > 7:
        return []

    # Initialize empty list to store daily reports
    daily_reports = []

    # Loop through each day in the date range
    current_datetime = start_datetime
    while current_datetime <= end_datetime:
        # Convert current date to string
        current_date_str = current_datetime.strftime("%Y-%m-%d")

        # Query for milk sold on current day
        daily_report = (
            db.query(
                models.MilkSelled.date,
                func.round(func.avg(models.MilkSelled.price), 2).label("milk_price"),
                func.sum(models.MilkSelled.quantity).label("milk_selled"),
                func.sum(models.MilkSelled.price * models.MilkSelled.quantity).label(
                    "total_price"
                ),
            )
            .filter(models.MilkSelled.date == current_date_str)
            .group_by(models.MilkSelled.date)
            .all()
        )


        if daily_report == []:
            daily_report = {
                "date": current_date_str,
                "day_of_week": current_datetime.strftime("%A"),
                "milk_price": 0,
                "milk_selled": 0,
                "total_price": 0,
            }
        else:
            daily_report = {
                "date": current_date_str,
                "day_of_week": current_datetime.strftime("%A"),
                "milk_price": daily_report[0][1],
                "milk_selled": daily_report[0][2], "total_price": daily_report[0][3],
                }

        # Append daily report to the list of daily reports
        daily_reports.append(daily_report)

        # Move to the next day
        current_datetime += timedelta(days=1)

    return daily_reports


def compare_milk_selled_and_collected_milk_by_date(
    db: Session, start_date: str, end_date: str
):
    start_datetime = datetime.strptime(start_date, "%Y-%m-%d")
    end_datetime = datetime.strptime(end_date, "%Y-%m-%d")

    if (end_datetime - start_datetime).days > 7:
        return []

    daily_reports = []

    current_datetime = start_datetime
    
    while current_datetime <= end_datetime:
        current_date_str = current_datetime.strftime("%Y-%m-%d")

        daily_report = (
            db.query(
                models.CollectedMilk.date,
                func.sum(models.CollectedMilk.quantity).label("milk_collected"),
                func.sum(models.CollectedMilk.price * models.CollectedMilk.quantity).label(
                    "total_price_collected"
                ),
                func.round(func.avg(models.CollectedMilk.price), 2).label("avg_milk_collected_price"),
                func.sum(models.MilkSelled.quantity).label("milk_selled"),
                func.sum(models.MilkSelled.price * models.MilkSelled.quantity).label(
                    "total_price_selled"
                ),
                func.round(func.avg(models.MilkSelled.price), 2).label("avg_milk_selled_price"),
            )
            .outerjoin(models.MilkSelled, extract('day', models.CollectedMilk.date) == extract('day', models.MilkSelled.date))
            .filter(models.CollectedMilk.date == current_date_str)
            .group_by(models.CollectedMilk.date)
            .all()
        )


        if daily_report == []:
            daily_report = {
                "date": current_date_str,
                "day_of_week": current_datetime.strftime("%A"),
                "milk_collected": 0,
                "total_price_collected": 0,
                "avg_milk_collected_price": 0,
                "milk_selled": 0,
                "total_price_selled": 0,
                "avg_milk_selled_price": 0,
            }
        else:
            milk_collected = daily_report[0][1] if daily_report[0][1] else 0
            total_price_collected = daily_report[0][2] if daily_report[0][2] else 0
            avg_milk_collected_price = daily_report[0][3] if daily_report[0][3] else 0
            milk_selled = daily_report[0][4] if daily_report[0][4] else 0
            total_price_selled = daily_report[0][5] if daily_report[0][5] else 0
            avg_milk_selled_price = daily_report[0][6] if daily_report[0][6] else 0

            daily_report = {
                "date": current_date_str,
                "day_of_week": current_datetime.strftime("%A"),
                "milk_collected": milk_collected,
                "total_price_collected": total_price_collected,
                "avg_milk_collected_price": avg_milk_collected_price,
                "milk_selled": milk_selled,
                "total_price_selled": total_price_selled,
                "avg_milk_selled_price": avg_milk_selled_price,
            }

        daily_reports.append(daily_report)

        current_datetime += timedelta(days=1)

    return daily_reports





# Payment report by producer and by date
def get_payment_report_by_producer_and_date(db: Session, start_date: str, end_date: str):
    start_datetime = datetime.strptime(start_date, "%Y-%m-%d")
    end_datetime = datetime.strptime(end_date, "%Y-%m-%d")

    if (end_datetime - start_datetime).days > 7:
        return []

    daily_reports = []

    current_datetime = start_datetime

    while current_datetime <= end_datetime:
        current_date_str = current_datetime.strftime("%Y-%m-%d")
        
        # bring only producers with collected milk
        producersWithCollected = db.query(models.Producer).join(models.CollectedMilk).filter(models.CollectedMilk.quantity > 0).all()
        for producer in producersWithCollected:
            daily_report = (
                db.query(
                    models.Payment.date,
                    models.Producer.name.label("producer_name"),
                    func.sum(models.CollectedMilk.quantity).label("total_milk_collected"),
                    func.sum(models.CollectedMilk.price * models.CollectedMilk.quantity).label("total_price_collected"),
                    func.coalesce(func.sum(models.Deduction.price), 0).label("total_deduction"),
                    func.sum(models.Payment.total_amount).label("total_payment"),
                    models.Producer.id.label("producer_id"),
                )
                .outerjoin(models.Deduction)
                .join(models.CollectedMilk, models.Payment.collected_milk_id == models.CollectedMilk.id)
                .join(models.Producer, models.CollectedMilk.producer_id == models.Producer.id)
                .filter(models.Payment.date == current_date_str)
                .filter(models.Producer.id == producer.id)
                .group_by(models.Payment.date, models.Producer.name, models.Producer.id)
                .all()
            )

            if daily_report == []:
                daily_report = {
                    "date": current_date_str,
                    "day_of_week": current_datetime.strftime("%A"),
                    "producer_name": producer.name,
                    "total_milk_collected": 0,
                    "total_price_collected": 0,
                    "total_deduction": 0,
                    "total_payment": 0,
                    "producer_id": producer.id,
                }
            else:
                daily_report = {
                    "date": current_date_str,
                    "day_of_week": current_datetime.strftime("%A"),
                    "producer_name": daily_report[0][1],
                    "total_milk_collected": daily_report[0][2],
                    "total_price_collected": daily_report[0][3],
                    "total_deduction": daily_report[0][4],
                    "total_payment": daily_report[0][5],
                    "producer_id": daily_report[0][6],
                }

            daily_reports.append(daily_report)
        current_datetime += timedelta(days=1)

    ordered_report = []
    report_ids = []

    for report in daily_reports:
        if report["producer_id"] not in report_ids:
            report_ids.append(report["producer_id"])
            report_id = report["producer_id"]
            report_report = list(filter(lambda x: x["producer_id"] == report_id, daily_reports))
            ordered_report.append(report_report)

    return ordered_report


# Milk sells report by cheese_maker and by date
def get_milk_sells_report_by_cheese_maker_and_date(db: Session, start_date: str, end_date: str):
    start_datetime = datetime.strptime(start_date, "%Y-%m-%d")
    end_datetime = datetime.strptime(end_date, "%Y-%m-%d")

    if (end_datetime - start_datetime).days > 7:
        return []

    daily_reports = []

    current_datetime = start_datetime

    while current_datetime <= end_datetime:
        current_date_str = current_datetime.strftime("%Y-%m-%d")

        for report in db.query(models.CheeseMaker).all():
            daily_report = (
                db.query(
                    models.MilkSelled.date,
                    models.CheeseMaker.name.label("cheese_maker_name"),
                    func.sum(models.MilkSelled.quantity).label("total_milk_selled"),
                    func.sum(models.MilkSelled.price * models.MilkSelled.quantity).label("total_price_selled"),
                    models.CheeseMaker.id.label("cheese_maker_id"),
                )
                .join(models.CheeseMaker)
                .filter(models.MilkSelled.date == current_date_str)
                .filter(models.CheeseMaker.id == report.id)
                .group_by(models.MilkSelled.date, models.CheeseMaker.name, models.CheeseMaker.id)
                .all()
            )

            if daily_report == []:
                daily_report = {
                    "date": current_date_str,
                    "day_of_week": current_datetime.strftime("%A"),
                    "cheese_maker_name": report.name,
                    "total_milk_selled": 0,
                    "total_price_selled": 0,
                    "cheese_maker_id": report.id,
                }
            else:
                daily_report = {
                    "date": current_date_str,
                    "day_of_week": current_datetime.strftime("%A"),
                    "cheese_maker_name": daily_report[0][1],
                    "total_milk_selled": daily_report[0][2],
                    "total_price_selled": daily_report[0][3],
                    "cheese_maker_id": daily_report[0][4],
                }

            daily_reports.append(daily_report)

        current_datetime += timedelta(days=1)

    ordered_report = []
    report_ids = []

    for report in daily_reports:
        if report["cheese_maker_id"] not in report_ids:
            report_ids.append(report["cheese_maker_id"])
            report_id = report["cheese_maker_id"]
            report_report = list(filter(lambda x: x["cheese_maker_id"] == report_id, daily_reports))
            ordered_report.append(report_report)

    return ordered_report

# Collected by route by day
def get_collected_milk_report_by_date_and_route(db: Session, start_date: str, end_date: str):
    start_datetime = datetime.strptime(start_date, "%Y-%m-%d")
    end_datetime = datetime.strptime(end_date, "%Y-%m-%d")

    if (end_datetime - start_datetime).days > 7:
        return []

    daily_reports = []

    current_datetime = start_datetime

    while current_datetime <= end_datetime:
        current_date_str = current_datetime.strftime("%Y-%m-%d")

        for route in db.query(models.MilkRoute).all():
            daily_report = (
                db.query(
                    models.CollectedMilk.date,
                    models.MilkRoute.name.label("route_name"),
                    func.sum(models.CollectedMilk.quantity).label("milk_collected"),
                    func.sum(models.CollectedMilk.price * models.CollectedMilk.quantity).label("total_price_collected"),
                    models.MilkRoute.id.label("route_id"),
                )
                .join(models.MilkRoute)
                .filter(models.CollectedMilk.date == current_date_str)
                .filter(models.MilkRoute.id == route.id)
                .group_by(models.CollectedMilk.date, models.MilkRoute.name, models.MilkRoute.id)
                .all()
            )

            if daily_report == []:
                daily_report = {
                    "date": current_date_str,
                    "day_of_week": current_datetime.strftime("%A"),
                    "route_name": route.name,
                    "milk_collected": 0,
                    "total_price_collected": 0,
                    "route_id": route.id,
                }
            else:
                daily_report = {
                    "date": current_date_str,
                    "day_of_week": current_datetime.strftime("%A"),
                    "route_name": daily_report[0][1],
                    "milk_collected": daily_report[0][2],
                    "total_price_collected": daily_report[0][3],
                    "route_id": daily_report[0][4],
                }

            daily_reports.append(daily_report)

        current_datetime += timedelta(days=1)

    # list of lists by route
    ordered_report = []
    report_ids = []
    for report in daily_reports:
        if report["route_id"] not in report_ids:
            report_ids.append(report["route_id"])
            report_id = report["route_id"]
            report_report = list(filter(lambda x: x["route_id"] == report_id, daily_reports))
            ordered_report.append(report_report)

    return ordered_report
