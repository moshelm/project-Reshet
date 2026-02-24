from logging import Logger
from mongo_manager import MongoManager
from fastapi import HTTPException, File, UploadFile, Form

class MongoOrchestrator():
    def __init__(self,storage: MongoManager, logger :Logger):
        self.logger = logger
        self.storage = storage

    def upload_file(self,request: UploadFile = File(...), image_id: str = Form(...)):
        self.logger.info("upload file")
        result = self.storage.save(request, image_id)
        return result

    def run(self,request: UploadFile = File(...), image_id: str = Form(...)):
        self.logger.info("start running")
        try: 
            result = self.upload_file(request,image_id)
            if result is None:
                raise Exception 
            self.logger.info("finish insertion to mongo")
            return result
        except Exception as e:
            self.logger.error(f"failed insert to mongo. {e}",exc_info=True)
            raise HTTPException(f"server failed. {e}", status_code=400)

        