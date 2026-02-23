import pytesseract
from PIL import Image

img = Image.open('tweet_98.png')
text = pytesseract.image_to_string(img)
print("-----")
print("read image")
print(text)