from faker import Faker

from app.src import models

from app.dependencies import get_db, Session

import logging

logger = logging.getLogger(__name__)

fake = Faker()


class CheeseMakerSeed:
    def __init__(self):
        self.cheese_maker = {
            "name": fake.name(),
            "description": fake.text(),
            "phone": fake.phone_number(),
            "date": fake.date()
        }

    def generate_cheese_maker_data():
        return {
            "name": fake.name(),
            "description": fake.text(),
            "phone": fake.phone_number(),
            "date": fake.date()
        }

    @staticmethod
    def seed_cheese_maker_table(num_cheese_makers):
        db: Session = next(get_db())
        try:
            for _ in range(num_cheese_makers):
                cheese_maker = models.CheeseMaker(**CheeseMakerSeed.generate_cheese_maker_data())
                print(cheese_maker)
                db.add(cheese_maker)
            db.commit()
            logger.info(f"CheeseMaker table seeded with {num_cheese_makers} records")
        except Exception as e:
            logger.error(f"""Error seeding cheese_maker table: {e}""")
            raise


if __name__ == "__main__":
    CheeseMakerSeed.seed_cheese_maker_table(10)
