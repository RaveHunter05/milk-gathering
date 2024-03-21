from faker import Faker

from app.src import models

from app.dependencies import get_db, Session

import logging

logger = logging.getLogger(__name__)

fake = Faker()


class CollectedMilkSeed:
    def __init__(self):
        self.collected_milk = {
            "driver_id": fake.random_int(min=1, max=10),
            "route_id": fake.random_int(min=1, max=10),
            "producer_id": fake.random_int(min=1, max=10),
            "quantity": fake.random_int(),
            "type": "Galon",
            "date": fake.date()
        }

    def generate_collected_milk_data():
        return {
            "driver_id": fake.random_int(min=1, max=10),
            "route_id": fake.random_int(min=1, max=10),
            "producer_id": fake.random_int(min=1, max=10),
            "quantity": fake.random_int(),
            "type": "Galon",
            "date": fake.date()
        }

    @staticmethod
    def seed_collected_milk_seed(num_routes):
        db: Session = next(get_db())
        try:
            for _ in range(num_routes):
                collected_milk = models.CollectedMilk(**CollectedMilkSeed.generate_collected_milk_data())
                print(collected_milk)
                db.add(collected_milk)
            db.commit()
            logger.info(f"Collected Milk table seeded with {num_routes} records")
        except Exception as e:
            logger.error(f"""Error seeding collected milk table: {e}""")
            raise


if __name__ == "__main__":
    CollectedMilkSeed.seed_collected_milk_seed(10)
