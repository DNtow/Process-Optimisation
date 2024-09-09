# kafka_consumer.py
from kafka import KafkaConsumer
import json

class KafkaDataConsumer:
    def __init__(self, topic, bootstrap_servers):
        self.consumer = KafkaConsumer(topic, bootstrap_servers=bootstrap_servers, value_deserializer=lambda m: json.loads(m.decode('utf-8')))

    def consume_data(self):
        for message in self.consumer:
            print(f"Consumed message: {message.value}")
