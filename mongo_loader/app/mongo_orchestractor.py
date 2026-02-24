from logging import Logger
from mongo_manger import MongoManager

class MongoOrchestrator():
    def __init__(self,storage: MongoManager, logger :Logger):
        self.logger = logger
        self.storage = storage

    def upload_file(self,request):
        
        self.storage.save()

        