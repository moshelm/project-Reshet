from logging import Logger
from text_analyzer import TextAnalyzer
from shared.kafka.kafka_publisher import KafkaPublisher,KafkaException
from shared.kafka.kafka_consumer import KafkaConsumer

class Orchestrator():
    def __init__(self,publisher : KafkaPublisher, consumer: KafkaConsumer, analyzer: TextAnalyzer, logger : Logger):
        self.logger = logger 
        self.publisher = publisher
        self.consumer = consumer
        self.analyzer = analyzer

    def handel_event(self,data):
        try:
            self.logger.info("start analyze...")
            info = self.analyzer.analyze(data['clean_text'])
            self.logger.info("publish new event...")
            self.publisher.publish(info)
        except Exception:
            self.logger.error("error from handel")
            raise
        except KafkaException:
            self.logger.error("kafka failed")
            raise
    def run(self):
        try:
            self.logger.info("start...")
            self.consumer.start(self.handel_event)
            self.logger.info("new event success")
        except KafkaException:
            self.logger.error("kafka failed")
            raise
        except Exception:
            self.logger.error("error in running")
            raise
        
