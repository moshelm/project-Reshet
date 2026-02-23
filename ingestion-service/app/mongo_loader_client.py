import requests
import logging
from requests.exceptions import RequestException

class MongoLoaderClient():
    def __init__(self, mongo_loader_url:str, logger :logging.Logger):
        self.logger = logger
        self.mongo_loader_url = mongo_loader_url
    
    def send(self,file_path:str, image_id:str):
        try:
            response = requests.post(self.mongo_loader_url,data=file_path, params= image_id)
            return response
        except RequestException as e:
            print(f"failed to send to mongo loader {e}")
            return None