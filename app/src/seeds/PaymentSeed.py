from faker import Faker

from app.src import models

from app.dependencies import get_db, Session

import logging

logger = logging.getLogger(__name__)

fake = Faker()


class PaymentSeed:
    def __init__(self):
        self.payment = {
            "collected_milk_id": fake.random_int(min=11, max=20),
            "deduction_id": fake.random_int(min=1, max=10),
            "transport_cost_id": fake.random_int(min=1, max=10),
            "milk_price_id": fake.random_int(min=1, max=10),
            "amount": fake.random_int(),
            "date": fake.date()
        }

    def generate_payment():
        return {
            "collected_milk_id": fake.random_int(min=11, max=20),
            "deduction_id": fake.random_int(min=1, max=10),
            "transport_cost_id": fake.random_int(min=1, max=10),
            "milk_price_id": fake.random_int(min=1, max=10),
            "amount": fake.random_int(),
            "date": fake.date()
        }

    @staticmethod
    def seed_payment(num_routes):
        db: Session = next(get_db())
        try:
            for _ in range(num_routes):
                payment = models.Payment(**PaymentSeed.generate_payment())
                print(payment)
                db.add(payment)
            db.commit()
            logger.info(f"Payment Milk table seeded with {num_routes} records")
        except Exception as e:
            logger.error(f"""Error seeding payment milk table: {e}""")
            raise


if __name__ == "__main__":
    PaymentSeed.seed_payment(10)
