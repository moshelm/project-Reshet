import logging 
from service_config import MongoConfig
from fastapi import FastAPI, File, UploadFile, HTTPException, Form
from mongo_orchestrator import MongoOrchestrator
from mongo_loader.app.mongo_manager import MongoManager
config = MongoConfig()
config.validate()

logging.basicConfig(
    level=config.log_level,
    format=f'%(asctime)s | {config.service_name} | %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

app = FastAPI()

@app.post("/upload_files")
def upload(file : UploadFile = File(...)):
    pass