import os 


class CleanConfig():
    def __init__(self):
        self.log_level = os.getenv("LOG_LEVEL","INFO")
        self.kafka_host = os.getenv("KAFKA_HOST","localhost")
        self.kafka_port = os.getenv("KAFKA_PORT","9092")
        self.kafka_config = {"bootstrap.servers":f"{self.kafka_host}:{self.kafka_port}"}
        self.consumer_topic_name = os.getenv("CONSUMER_TOPIC_NAME","raw").split(",")
        self.producer_topic_name = os.getenv("PRODUCER_TOPIC_NAME","clean")
        self.kafka_group_id = os.getenv("GROUP_ID","ddd")
        self.service_name = os.getenv("SERVICE_NAME","clean")
        
    def validate(self):
        if not self.kafka_config :
            raise "configuration messing"
        
