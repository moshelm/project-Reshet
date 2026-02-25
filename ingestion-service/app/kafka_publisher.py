import logging
from confluent_kafka import Message ,Producer, KafkaException
import json 

class KafkaPublisher():
    def __init__(self, logger: logging.Logger, kafka_config : str, topic_name : str):
        self.logger = logger
        kafka_config['logger'] = self.logger
        self.producer = Producer(kafka_config)
        self.topic = topic_name
        

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
            self.logger.info("finish publish event")
        except KafkaException as e:
            self.logger.error(f"kafka error. {e}")
            
    def close(self):
        self.logger.info("flushing all messages...")
        self.producer.flush(5)
            