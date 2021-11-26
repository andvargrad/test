import pytesseract
from PIL import Image
import os
def save_number():
    for scan_name_file in os.listdir("image"):
        full_link = (os.path.abspath(f"image\{scan_name_file}"))
        pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
        img = Image.open(full_link)
        text = pytesseract.image_to_string(img)
        numb = (text.replace(" ", "").strip())
        numb2 = (numb.replace("-", ""))
        numb3 = (numb2.replace("8", "+7", 1))
        link_numb = (f"https://wa.me/{numb3}")
        with open("log.txt", "a") as save_file:
            save_file.write(link_numb + "\n")

save_number()
