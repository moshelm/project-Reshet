import os 


class CleanConfig():
    def __init__(self):
        self.log_level = os.getenv("LOG_LEVEL","INFO")
        self.kafka_host = os.getenv("KAFKA_HOST","localhost")
        self.kafka_port = os.getenv("KAFKA_PORT","9092")
        self.kafka_config = {"bootstrap":f"http:{self.kafka_host}:{self.kafka_port}"}
        self.kafka_topic_name = os.getenv("KAFKA_TOPIC_NAME","raw")
        self.kafka_group_id = os.getenv("GROUP_ID","ddd")
    def validate(self):
        if not self.kafka_config or not self.data_files_route or not self.mongo_loader_url:
            raise "configuration messing"
        
