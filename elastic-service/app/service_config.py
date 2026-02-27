import os 

class ServiceConfig():
    def __init__(self):
        self.log_level = os.getenv("LOG_LEVEL","INFO")
        self.kafka_host = os.getenv("KAFKA_HOST","localhost")
        self.kafka_port = os.getenv("KAFKA_PORT","9092")
        self.kafka_config = {"bootstrap.servers":f"{self.kafka_host}:{self.kafka_port}"}
        self.topics= os.getenv("TOPICS","raw,clean").split(',')
        self.kafka_group_id = os.getenv("GROUP_ID","ddd")
        self.service_name = os.getenv("SERVICE_NAME","el")
        
        es_host = os.getenv("ES_HOST","localhost") 
        es_port = os.getenv("ES_PORT","9200") 

        self.es_uri = f'http://{es_host}:{es_port}'
        self.index_name = os.getenv("INDEX_NAME","all_data")
    def validate(self):
        if not self.kafka_config :
            raise "configuration messing"
        
