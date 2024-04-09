from faker import Faker

from app.src import models

from app.dependencies import get_db, Session

import logging

logger = logging.getLogger(__name__)

fake = Faker()


class DeductionSeed:
    def __init__(self):
        self.deduction = {
            "name": fake.name(),
            "description": fake.text(),
            "price": fake.random_int(),
            "paid": fake.boolean(),
            "date": fake.date()
        }

    def generate_deduction_data():
        return {
            "name": fake.name(),
            "description": fake.text(),
            "price": fake.random_int(),
            "paid": fake.boolean(),
            "date": fake.date()
        }

    @staticmethod
    def seed_deduction_seed(num_routes):
        db: Session = next(get_db())
        try:
            for _ in range(num_routes):
                deduction = models.Deduction(**DeductionSeed.generate_deduction_data())
                print(deduction)
                db.add(deduction)
            db.commit()
            logger.info(f"Deduction table seeded with {num_routes} records")
        except Exception as e:
            logger.error(f"""Error seeding deduction route table: {e}""")
            raise


if __name__ == "__main__":
    DeductionSeed.seed_deduction_seed(10)
