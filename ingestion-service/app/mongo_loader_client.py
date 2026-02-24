import requests
import logging
from requests.exceptions import RequestException

class MongoLoaderClient():
    def __init__(self, mongo_loader_url:str, logger :logging.Logger):
        self.logger = logger
        self.mongo_loader_url = mongo_loader_url
    
    def send(self,file_path:str, image_id:str):
        try:
            with open(file_path,"br") as file:
                files = {"file":file}
                response = requests.post(self.mongo_loader_url,files=files)
                self.logger.info("sending to mongo success")
            return response
        except FileNotFoundError as e:
            self.logger.error(f"file not found to send {e}",exc_info=True)
            return None
        except RequestException as e:
            self.logger.error(f"failed to send to mongo loader {e}",exc_info=True)
            return None