from pymongo import MongoClient
from logging import Logger
from  gridfs.errors import FileExists,GridFSError
import gridfs
from fastapi import Form , File , UploadFile

class MongoManager():
    def __init__(self, mongo_uri:str, mongo_database:str, logger : Logger):
        self.logger = logger
        self.client = MongoClient(mongo_uri)
        self.db = self.client[mongo_database]
        self.bucket = gridfs.GridFSBucket(self.db)

    def save(self, file_stream: UploadFile = File(...), image_id:str =Form(...)):
        file_name = file_stream.filename
        try:
            with self.bucket.open_upload_stream_with_id(file_id= image_id, filename= file_name) as grid:
                self.logger.info("start insert to mongo in bucket")
                while True:
                    chunk = file_stream.file.read(1024*1024)
                    if not chunk:
                        break
                    grid.write(chunk)
                self.logger.info(f"success insert file {file_name} id: {image_id}")
                return {"status":"success",
                        "file_name":file_name,
                        "image_id":image_id}
        except GridFSError as e :
            self.logger.error(f"error in gridfs. {e}",exc_info=True)
            return None
        except FileExists as e :
            self.logger.error(f"there is already file name {e}",exc_info=True)
            return None