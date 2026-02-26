from logging import Logger
from collections import Counter
import re
import nltk 
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from pathlib import Path

class TextAnalyzer():
    def __init__(self, logger:Logger):
        self.logger = logger 
        nltk.download('vader_lexicon')
    def analyze(self, text:str ):
        try:
            words = re.findall(r'\w+', text.lower())
            most_common = get_most_common(words)
            weapon_in_text = list(set(words).intersection(weapon_list()))
            label = get_sentiment(' '.join(words))
            return {
                "most common":most_common,
                "weapon in text":weapon_in_text,
                "label":label
            }
        except Exception:
            self.logger.error("failed!!!",exc_info=True)
            raise
    
def get_sentiment(words):
    compound = SentimentIntensityAnalyzer().polarity_scores(words)['compound'] 
    if 0.5 < compound < 1:
        return {'label':{"pos":compound}}
    elif -0.5 < compound <= 0.5:
        return {'label':{"neo":compound}}
    else:
        return {'label':{"neg":compound}}
    
def get_most_common(words: list):
    words_count = Counter(words)
    if words_count is None:
        return []
    sorted_counts = words_count.most_common()
    if len(sorted_counts) <= 10:
        return [word for word, count in sorted_counts]
    return [word for word ,count in sorted_counts if word in words[:10]]

def weapon_list():
    data_files_route = Path("/data") / "weapon_list.txt"
    with open(data_files_route,"r") as file:
        return [line.strip() for line in file.readlines()]
