import pytesseract
from PIL import Image
import os

#ФУНКЦИЯ РАСПОЗНОВАНИЯ НОМЕРА И СОХРАНЕНИЕ В НУЖНОМ ФОРМАТЕ V1.0
def save_number():
    print("__________________________")
    for scan_name_file in os.listdir("image"):
        full_link = (os.path.abspath(f"image\{scan_name_file}"))
        pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
        img = Image.open(full_link)
        text = pytesseract.image_to_string(img)
        numb = (text.replace(" ", "").strip()).replace("-", "").replace("8", "7", 1)
        print(numb)
        link_numb = (f"https://wa.me/{numb}")
        link_numb_bad = (f"https://wa.me/{numb} - inspect")
        a = (len(link_numb))
        if a == 25:
            with open("log.txt", "a") as save_file:
                save_file.write(link_numb + "\n")
                save_file.close()
        else:
            with open("log_bad.txt", "a") as save_file:
                save_file.write(link_numb + "\n")
                save_file.close()
                print(link_numb_bad)
save_number()
numb_files = len(os.listdir("image"))
print("__________________________")
print(f"обработанно номеров: [{numb_files}] шт.")
