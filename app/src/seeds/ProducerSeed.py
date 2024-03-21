from faker import Faker

from app.src import models

from app.dependencies import get_db, Session

import logging

logger = logging.getLogger(__name__)

fake = Faker()


class ProducerSeed:
    def __init__(self):
        self.producer = {
            "name": fake.name(),
            "description": fake.text(),
            "phone": fake.phone_number(),
            "date": fake.date()
        }

    def generate_producer_data():
        return {
            "name": fake.name(),
            "description": fake.text(),
            "phone": fake.phone_number(),
            "date": fake.date()
        }

    @staticmethod
    def seed_producer_table(num_producers):
        db: Session = next(get_db())
        try:
            for _ in range(num_producers):
                producer = models.Producer(**ProducerSeed.generate_producer_data())
                print(producer)
                db.add(producer)
            db.commit()
            logger.info(f"Producer table seeded with {num_producers} records")
        except Exception as e:
            logger.error(f"""Error seeding producer table: {e}""")
            raise


if __name__ == "__main__":
    ProducerSeed.seed_producer_table(10)
