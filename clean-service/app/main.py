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