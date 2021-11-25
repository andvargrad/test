import pytesseract
from PIL import Image


img = Image.open('/1.png')
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
print(pytesseract.image_to_string(img))

