import logging
from confluent_kafka import Producer, KafkaException
import json 

class KafkaPublisher():
    def __init__(self, logger: logging.Logger, bootstrap_servers : str, topic_name : str):
        self.producer = Producer(bootstrap_servers)
        self.topic = topic_name
        self.logger = logger

    def publish(self, event: dict|str):
        data = json.dumps(event).encode()
        key = "RAW".encode()    
        try:
            self.producer.produce(self.topic, value=data, key=key)
        except KafkaException as e:
            raise f"kafka error. {e}"
    