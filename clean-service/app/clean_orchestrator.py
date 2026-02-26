from logging import Logger 
from kafka_consumer import KafkaConsumer
from shared.kafka.kafka_publisher import KafkaPublisher
from text_cleaner import TextCleaner

class CleanOrchestrator():
    def __init__(self, consumer: KafkaConsumer, publisher:KafkaPublisher, cleaner: TextCleaner, logger: Logger):
        self.logger = logger
        self.consumer = consumer
        self.publisher = publisher
        self.cleaner = cleaner

    def handle_event(self, event):
        try:
            text = event['raw_text']
            clean_text = self.cleaner.clean(text)
            self.logger.info("proper event to send...")
            del event['raw_text']
            event['clean_text'] = clean_text
            self.publisher.publish(event)
            
        except Exception:
            self.logger.error("error in handel event",exc_info=True)
            raise

    def run(self):
        try:
            self.consumer.start(self.handle_event)
        except Exception:
            self.logger.error("error in running",exc_info=True)
            raise
        finally:
            self.publisher.close()