from faker import Faker

from app.src import models

from app.dependencies import get_db, Session

import logging

logger = logging.getLogger(__name__)

fake = Faker()


class MilkRouteSeed:
    def __init__(self):
        self.milkroute = {
            "name": fake.name(),
            "description": fake.text(),
            "date": fake.date()
        }

    def generate_milk_route_data():
        return {
            "name": fake.name(),
            "description": fake.text(),
            "date": fake.date()
        }

    @staticmethod
    def seed_milk_route_seed(num_routes):
        db: Session = next(get_db())
        try:
            for _ in range(num_routes):
                milk_route = models.MilkRoute(**MilkRouteSeed.generate_milk_route_data())
                print(milk_route)
                db.add(milk_route)
            db.commit()
            logger.info(f"Milk Route table seeded with {num_routes} records")
        except Exception as e:
            logger.error(f"""Error seeding milk route table: {e}""")
            raise


if __name__ == "__main__":
    MilkRouteSeed.seed_milk_route_seed(10)
