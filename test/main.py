import pytesseract
from PIL import Image
import os
def number():
    for scan_name_file in os.listdir("image"):
        full_link = (os.path.abspath(f"image\{scan_name_file}"))
        pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
        img = Image.open(full_link)
        text = pytesseract.image_to_string(img)
        numb = (text.replace(" ", ""))
        numb2 = (numb.replace("-", ""))
        print(numb2.strip())
number()
