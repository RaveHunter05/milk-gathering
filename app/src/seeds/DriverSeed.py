from faker import Faker

from app.src import models

from app.dependencies import get_db, Session

import logging

logger = logging.getLogger(__name__)

fake = Faker()


class DriverSeed:
    def __init__(self):
        self.driver = {
            "name": fake.name(),
            "phone": fake.phone_number(),
            "date": fake.date()
        }

    def generate_driver_data():
        return {
            "name": fake.name(),
            "phone": fake.phone_number(),
            "date": fake.date()
        }

    @staticmethod
    def seed_driver_seed(num_routes):
        db: Session = next(get_db())
        try:
            for _ in range(num_routes):
                driver = models.Driver(**DriverSeed.generate_driver_data())
                print(driver)
                db.add(driver)
            db.commit()
            logger.info(f"Driver table seeded with {num_routes} records")
        except Exception as e:
            logger.error(f"""Error seeding driver route table: {e}""")
            raise


if __name__ == "__main__":
    DriverSeed.seed_driver_seed(10)
