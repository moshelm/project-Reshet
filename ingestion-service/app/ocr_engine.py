import logging 
import pytesseract as pt
from PIL import Image


class OCREngine():
    def __init__(self,image):
        self.logger = logging.getLogger(__name__)
    
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
