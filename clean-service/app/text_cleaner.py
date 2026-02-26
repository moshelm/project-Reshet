from logging import Logger
import re
import nltk 
from nltk.corpus import stopwords

class TextCleaner():
    def __init__(self, logger: Logger):
        self.logger = logger
        nltk.download('stopwords',quiet=True)
        self.stop_words = set(stopwords.words('english'))
    
    def clean(self, text):
        try: 
            self.logger.info("start process...")
            clean = re.sub(r'[^\w\s]','',text).lower()
            clean_text = re.sub(r'\s+', ' ', clean).strip()

            words = clean_text.split()
            filtered_words = [word for word in words if word not in self.stop_words]
            final_text = ' '.join(filtered_words)
            self.logger.info("finish process")
            return final_text
        except Exception:
            self.logger.error("error in process",exc_info=True)
            return None