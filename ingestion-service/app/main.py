import logging
import os 
from ingestion_config import IngestionConfig
from kafka_publisher import KafkaPublisher
from mongo_loader_client import MongoLoaderClient
from ocr_engine import OCREngine, MetadataExtractor
from ingestion_orchestrator import IngestionOrchestrator

config = IngestionConfig()
config.validate()


logging.basicConfig(
    level=config.log_level,
    format=f'%(asctime)s | {config.service_name} | %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)



mongo_logger = logging.getLogger("mongo_loader_client")
kafka_logger = logging.getLogger("kafka_publisher")
ocr_engine_logger = logging.getLogger("ocr_engine")
metadata_logger = logging.getLogger("metadata_extractor")
orchestrator_logger = logging.getLogger("orchestrator")

def main():
    mongo_loader = MongoLoaderClient(mongo_loader_url= config.mongo_loader_url ,logger=mongo_logger)
    kafka = KafkaPublisher(kafka_config= config.kafka_config, topic_name= config.kafka_topic_name, logger=kafka_logger)
    ocr_engine = OCREngine(logger=ocr_engine_logger)
    metadata_extractor = MetadataExtractor(logger=metadata_logger) 

    manager = IngestionOrchestrator(config=config, ocr_engine=ocr_engine, metadata_extractor=metadata_extractor, mongo_client=mongo_loader, publisher=kafka, logger=orchestrator_logger)

    manager.run()
    
if __name__=="__main__":
    main()