import logging 
from service_config import MongoConfig
from fastapi import FastAPI, File, UploadFile, Form
from mongo_orchestrator import MongoOrchestrator
from mongo_manager import MongoManager

config = MongoConfig()
config.validate()

logging.basicConfig(
    level=config.log_level,
    format=f'%(asctime)s | {config.service_name} | %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
manager_logger = logging.getLogger("mongo_manager")
orchestrator_logger = logging.getLogger("mongo_orchestrator")

logging.getLogger("uvicorn").handlers = logging.getLogger().handlers
logging.getLogger("uvicorn.access").handlers = logging.getLogger().handlers
logging.getLogger("fastapi").handlers = logging.getLogger().handlers

mongo_manager = MongoManager(config.mongo_uri,config.mongo_database,manager_logger)
mongo_orchestrator = MongoOrchestrator(mongo_manager,orchestrator_logger)

app = FastAPI()

@app.post("/upload_files",status_code=200)
def upload(file : UploadFile = File(...), image_id :str = Form(...)):
    return mongo_orchestrator.run(file,image_id)