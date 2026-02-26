import logging
from config_service import CleanConfig
from clean_orchestrator import CleanOrchestrator
from text_cleaner import TextCleaner
from kafka_consumer import KafkaConsumer
from shared.kafka.kafka_publisher import KafkaPublisher


config = CleanConfig()


logger = logging.basicConfig(
    level=config.log_level,
    format=f'%(asctime)s | {config.service_name} | %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

clean_logger = logging.getLogger("clean_text")
consumer_logger = logging.getLogger("consumer")
producer_logger = logging.getLogger("producer")
orchestrator_logger = logging.getLogger("orchestrator")

def main():
    try: 
        clean_text = TextCleaner(clean_logger)
        consumer = KafkaConsumer(config.kafka_config,config.consumer_topic_name,config.kafka_group_id,consumer_logger)
        publisher = KafkaPublisher(producer_logger,config.kafka_config,config.producer_topic_name)

        manager = CleanOrchestrator(consumer,publisher,clean_text,orchestrator_logger)

        manager.run()
    except Exception as e:
        raise e

if __name__=="__main__":
    main()