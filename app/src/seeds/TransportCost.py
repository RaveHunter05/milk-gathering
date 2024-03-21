from faker import Faker

from app.src import models

from app.dependencies import get_db, Session

import logging

logger = logging.getLogger(__name__)

fake = Faker()


class TransportCost:
    def __init__(self):
        self.transport_cost = {
            "name": fake.name(),
            "description": fake.text(),
            "cost": fake.random_int(),
            "date": fake.date()
        }

    def generate_transport_cost():
        return {
            "name": fake.name(),
            "description": fake.text(),
            "cost": fake.random_int(),
            "date": fake.date()
        }

    @staticmethod
    def seed_transport_cost(num_routes):
        db: Session = next(get_db())
        try:
            for _ in range(num_routes):
                transport_cost = models.TransportCost(**TransportCost.generate_transport_cost())
                print(transport_cost)
                db.add(transport_cost)
            db.commit()
            logger.info(f"Transport Cost table seeded with {num_routes} records")
        except Exception as e:
            logger.error(f"""Error seeding transport cost table: {e}""")
            raise


if __name__ == "__main__":
    TransportCost.seed_transport_cost(10)
