from logging import Logger
from elasticsearch import Elasticsearch
from elasticsearch.exceptions import NotFoundError,ConnectionError


class ESClient():
    def __init__(self,ec_uri:str,index_name:str, logger:Logger):
        self.logger = logger
        self.es = Elasticsearch(ec_uri)
        self.index = index_name

    def upsert(self,document, image_id):
        try:
            result = self.es.update(
                index=self.index,
                id=image_id,
                body={"doc":document,"doc_as_upsert":True}
            )
            self.logger.info(f"Document {image_id} upserted. Result: {result['result']}")
        except Exception as e:
            self.logger.error(f"Failed to upsert document {image_id}: {e}")
            raise

    def search(self, query:dict):
        try:
            return self.es.search(index=self.index,body=query)
        except Exception:
            raise