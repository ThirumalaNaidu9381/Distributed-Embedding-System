import random
import time


class EmbeddingService:

    @staticmethod
    def generate_embedding(text: str):

        # Simulate expensive embedding generation
        time.sleep(3)

        return [round(random.random(), 3) for _ in range(10)]