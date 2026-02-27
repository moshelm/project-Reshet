import logging 
from orchestrator import Orchestrator
from text_analyzer import TextAnalyzer
from service_config import ServiceConfig
from shared.kafka.kafka_publisher import KafkaPublisher
from shared.kafka.kafka_consumer import KafkaConsumer


config = ServiceConfig()
config.validate()

logger = logging.basicConfig(
    level=config.log_level,
    format=f'%(asctime)s | {config.service_name} | %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

text_logger = logging.getLogger()
publisher_logger = logging.getLogger()
consumer_logger = logging.getLogger()
orchestrator_logger = logging.getLogger()

def main():
    try:
        text_analyzer = TextAnalyzer(text_logger)
        publisher = KafkaPublisher(publisher_logger,config.kafka_config,config.producer_topic_name)
        consumer = KafkaConsumer(config.kafka_config, config.consumer_topic_name, config.kafka_group_id, consumer_logger)
        orchestrator = Orchestrator(publisher,consumer,text_analyzer,orchestrator_logger)

        orchestrator.run()
    except Exception:
        raise

if __name__=="__main__":
    main()