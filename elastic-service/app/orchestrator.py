from logging import Logger
from es_client import ESClient
from shared.kafka.kafka_consumer import KafkaConsumer,KafkaException

class Orchestrator():
    def __init__(self, consumer: KafkaConsumer, es_client: ESClient, logger : Logger):
        self.logger = logger 
        self.es_manager = es_client
        self.consumer = consumer

    def handel_event(self,data):
        try:
            self.logger.info("start insert to elastic...")
            self.es_manager.upsert(data,data["image_id"])
            self.logger.info(f"new event app for id:{data["image_id"]}")
        except Exception:
            self.logger.error("error from handel")
            raise
    def run(self):
        try:
            self.logger.info("start...")
            self.consumer.start(self.handel_event)
        except KafkaException:
            self.logger.error("kafka failed")
            raise
        except Exception:
            self.logger.error("error in running")
            raise        
