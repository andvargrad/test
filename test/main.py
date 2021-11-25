import pytesseract
from PIL import Image

img = Image.open(r"C:\Users\Xiaomi\PycharmProjects\github\test\1.png")
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

text = pytesseract.image_to_string(img)
print(text.strip())
