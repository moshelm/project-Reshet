import os 

class IngestionConfig():
    def __init__(self):
        self.kafka_host = os.getenv("KAFKA_HOST", "localhost")
        self.kafka_port = int(os.getenv("KAFKA_PORT", "9092"))
        self.kafka_config = {"bootstrap.servers" : f"{self.kafka_host}:{self.kafka_port}"}
        self.source_route = "data\messaging_images.zip"