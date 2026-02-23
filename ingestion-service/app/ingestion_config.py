import os 
from pathlib import Path

class IngestionConfig():
    def __init__(self):
        kafka_host = os.getenv("KAFKA_HOST", "localhost")
        kafka_port = os.getenv("KAFKA_PORT", "9092")
        kafka_bootstrap_servers = f"{kafka_host}:{kafka_port}"

        self.log_level = os.getenv("LOG_LEVEL","INFO")
        self.service_name = os.getenv("SERVICE_NAME","ingestion_service")
        self.kafka_config = {"bootstrap.servers" : kafka_bootstrap_servers} 
        self.kafka_topic_name = os.getenv("KAFKA_TOPIC_NAME","RAW")
        self.mongo_loader_url = os.getenv("MONGO_LOADER_URL","http://localhost:27017")

        self.data_files_route = Path("data") / "messaging_images" / "tweet_images"
    
    def validate(self):
        if not self.kafka_config or not self.data_files_route or not self.mongo_loader_url:
            raise "configuration messing"
        