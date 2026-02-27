from confluent_kafka import Consumer
from confluent_kafka.error import KafkaException
from logging import Logger
from shared.utils.serialize import json_deserializer

class KafkaConsumer():
    def __init__(self,kafka_config:str, topic_name:list[str], group_id:str, logger:Logger):
        self.logger = logger
        
        consumer_config = kafka_config
        consumer_config["group.id"] = group_id 
        try: 
            self.logger.info("create consumer...")
            self.consumer = Consumer(consumer_config)
            self.logger.info("consumer initialize in success")
        except KafkaException:
            self.logger.critical("consumer not work",exc_info=True)
            raise 
        self.topic = topic_name
        self.group_id = group_id

    def start(self,callback):
        self.logger.info("start subscribe")
        self.consumer.subscribe(self.topic)
        while True:
            msg = self.consumer.poll()
            if msg is None:
                continue
            if msg.error():
                self.logger.error(f"consumer error append. {msg.error()}")
                continue
            try: 
                data = json_deserializer(msg.value())
            except Exception:
                self.logger.error("failed get data by json",exc_info=True)
                raise 
            try:
                self.logger.info("send to process...") 
                callback(data)
            except Exception:
                self.logger.error("process failed",exc_info=True)
                raise