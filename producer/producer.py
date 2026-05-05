import time
import json
import random
from kafka import KafkaProducer

# Step A: create connection (with retry)
def create_producer():
    while True:
        try:
            producer = KafkaProducer(
                bootstrap_servers='kafka:9092',
                value_serializer=lambda v: json.dumps(v).encode('utf-8')
            )
            print("Connected to Kafka ✅")
            return producer
        except:
            print("Kafka not ready, retrying in 5 seconds...")
            time.sleep(5)

# Step B: connect
producer = create_producer()

# Step C: send data continuously
while True:
    data = {
        "product": random.choice(["phone", "laptop", "tablet"]),
        "price": random.randint(100, 1000),
        "quantity": random.randint(1, 5),
        "category": random.choice(["electronics", "fashion"])
    }

    producer.send("ecommerce_topic", data)
    print("Sent:", data)

    time.sleep(2)  # wait 2 seconds