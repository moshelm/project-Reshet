import logging
from ingestion_config import IngestionConfig
from kafka_publisher import KafkaPublisher
from mongo_loader_client import MongoLoaderClient
from ocr_engine import OCREngine, MetadataExtractor
import os 

class IngestionOrchestrator():
    def __init__(self, config : IngestionConfig, ocr_engine : OCREngine,
                  metadata_extractor : MetadataExtractor, 
                  mongo_client : MongoLoaderClient, publisher : KafkaPublisher, logger : logging.Logger):
        self.logger = logger 
        self.config = config
        self.ocr_engine = ocr_engine
        self.metadata_extractor = metadata_extractor
        self.mongo_client = mongo_client
        self.publisher = publisher

    def process_image(self,image_path:str):
        try: 
            raw_text = self.ocr_engine.extract_text(image_path)
            image_id = self.metadata_extractor.generate_image_id(image_path)
            metadata = self.metadata_extractor.extract_metadata(image_path)
            self.mongo_client.send(raw_text, image_id)
            event = {
                "raw_text": raw_text,
                "image_id": image_id,
                "metadata": metadata
            }
            self.publisher.publish(event)
        except Exception as e:
            self.logger.error(f"failed process file {image_path}. {e}", exc_info=True)

    def run(self):
        try: 
            images_list = os.listdir(self.config.data_files_route)
            for image_name in images_list:
                image_path = os.path.join(self.config.data_files_route,image_name)
                self.process_image(image_path)

            self.logger.info("end of program success")
            self.publisher.close()
        except Exception as e:
            self.logger.error(f"failed run all data. {e}", exc_info=True)