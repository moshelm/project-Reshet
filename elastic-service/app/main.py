import logging 
from orchestrator import Orchestrator
from service_config import ServiceConfig
from shared.kafka.kafka_consumer import KafkaConsumer
from es_client import ESClient

config = ServiceConfig()

logger = logging.basicConfig(
    level=config.log_level,
    format=f'%(asctime)s | {config.service_name} | %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

es_logger = logging.getLogger("es client")
publisher_logger = logging.getLogger("publisher")
consumer_logger = logging.getLogger("consumer")
orchestrator_logger = logging.getLogger("orchestrator")

def main():
    try:
        es_client = ESClient(config.es_uri,config.index_name,es_logger)
        consumer = KafkaConsumer(config.kafka_config, config.topics, config.kafka_group_id, consumer_logger)
        orchestrator = Orchestrator(consumer,es_client,orchestrator_logger)

        orchestrator.run()
    except Exception:
        raise

if __name__=="__main__":
    main()