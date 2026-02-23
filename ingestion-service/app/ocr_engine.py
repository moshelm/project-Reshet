import logging 
import pytesseract as pt
from PIL import Image
import os 
import hashlib

class OCREngine():
    def __init__(self, logger :logging.Logger):
        self.logger = logger
    
    def extract_text(self,image_path:str):
        try:
            img = Image.open(image_path)
        except FileNotFoundError as e:
            self.logger.error("image not found" ,exc_info=e)
        try:
            text = pt.image_to_string(img)
            return text 
        except Exception as e:
            self.logger.error("failed convert image to string", exc_info=e)
