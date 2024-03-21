from faker import Faker

from app.src import models

from app.dependencies import get_db, Session

import logging

logger = logging.getLogger(__name__)

fake = Faker()


class MilkPriceSeed:
    def __init__(self):
        self.driver = {
            "name": fake.name(),
            "price": fake.random_int(),
            "date": fake.date()
        }

    def generate_milk_price_data():
        return {
            "name": fake.name(),
            "price": fake.random_int(),
            "date": fake.date()
        }

    @staticmethod
    def seed_milk_price_seed(num_routes):
        db: Session = next(get_db())
        try:
            for _ in range(num_routes):
                milk_price = models.MilkPrice(**MilkPriceSeed.generate_milk_price_data())
                print(milk_price)
                db.add(milk_price)
            db.commit()
            logger.info(f"Milk Price table seeded with {num_routes} records")
        except Exception as e:
            logger.error(f"""Error seeding milk price route table: {e}""")
            raise


if __name__ == "__main__":
    MilkPriceSeed.seed_milk_price_seed(10)
