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

class MetadataExtractor():
    def __init__(self, logger : logging.Logger):
        self.logger = logger

    def generate_image_id(self, image_path : str)-> str | None:
        try:
            if not image_path or not isinstance(image_path, str) :
                raise ValueError(f"Invalid image path provided: {image_path}")
            file_name = os.path.basename(image_path)
            last_change = os.path.getmtime(image_path)
            code_id = f"{file_name}_{last_change}"
            hash_id = hashlib.md5(code_id.encode()).hexdigest()
            return hash_id
        except FileNotFoundError as e:
            self.logger.error("not found for generate id",exc_info=e)
            return None
        except Exception as e:
            self.logger.error("som error in generate",exc_info=e)
            return None

    
    def extract_metadata(self, image_path : str) -> dict | None:
        try:
            file_size = os.path.getsize(image_path)
            img = Image.open(image_path)
            format_file = img.format
            width, height = img.size
            return {
                "file_id":self.generate_image_id(image_path),
                "file_name": os.path.basename(image_path),
                "size_bytes":file_size,
                "format": format_file,
                "dimensions_as_str": f"{width}x{height}",   
                "dimensions": (width, height),   
            }
        except FileNotFoundError as e:
            self.logger.error("image not found" ,exc_info=e)
            return None