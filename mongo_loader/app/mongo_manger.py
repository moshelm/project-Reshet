from pymongo import MongoClient
from logging import Logger
import gridfs

class MongoManager():
    def __init__(self, mongo_uri:str, mongo_database:str, logger : Logger):
        self.logger = logger
        self.client = MongoClient(mongo_uri)
        self.db = self.client[mongo_database]
        self.bucket = gridfs.GridFSBucket(self.db)

    def save(self,file_stream,image_id:str):
        with self.bucket.open_upload_stream_with_id(file_id=image_id,filename=file_stream) as grid:
            res = grid.write(file_stream)
            return res
    