import os 
import logging 


class MongoConfig():
    def __init__(self):
        mongo_host = os.getenv("MONGO_HOST","localhost")
        mongo_port = os.getenv("MONGO_PORT","27017")
        
        self.mongo_database = os.getenv("MONGO_DATABASE","db_reshet")
        self.mongo_uri = f"mongodb://{mongo_host}:{mongo_port}"
        self.log_level = os.getenv("LOG_LEVEL","INFO")
        self.service_name = os.getenv("SERVICE_NAME","mongo")
        
    def validate(self):
        if not self.mongo_uri or not self.log_level or not self.service_name:
            raise "configuration is missing"