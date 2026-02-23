import logging
from confluent_kafka import Message ,Producer, KafkaException
import json 

class KafkaPublisher():
    def __init__(self, logger: logging.Logger, bootstrap_servers : str, topic_name : str):
        self.producer = Producer(bootstrap_servers)
        self.topic = topic_name
        self.logger = logger

    def delivery(self, err : Message, msg : Message):
        if err is not None:
            self.logger.error("Delivery failed for Message: {} : {}".format(msg.value(), err))
            return
        self.logger.info('Message: {} successfully produced to Topic: {} Partition: [{}] at offset {}'.format(
         msg.value(), msg.topic(), msg.partition(), msg.offset()))


    def publish(self, event: dict|str):
        data = json.dumps(event).encode()
        try:
            self.producer.produce(self.topic, value=data,callback=self.delivery)
            self.producer.poll(0)
        except KafkaException as e:
            raise f"kafka error. {e}"
    