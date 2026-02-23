import os 
from pathlib import Path

class IngestionConfig():
    def __init__(self):
        kafka_host = os.getenv("KAFKA_HOST", "localhost")
        kafka_port = os.getenv("KAFKA_PORT", "9092")
        self.kafka_bootstrap_servers = f"{kafka_host}:{kafka_port}"
        self.kafka_config = {"bootstrap.servers":self.kafka_bootstrap_servers} 
        self.source_route = Path("data") / "messaging_images"
        self.mongo_loader_url = os.getenv("MONGO_LOADER_URL","http://localhost:27017")
    
    def validate(self):
        if not self.kafka_config or not self.source_route or not self.mongo_loader_url:
            raise "configuration messing"
        