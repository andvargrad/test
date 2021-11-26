import pytesseract
from PIL import Image
import os

#ФУНКЦИЯ РАСПОЗНОВАНИЯ НОМЕРА И СОХРАНЕНИЕ В НУЖНОМ ФОРМАТЕ V1.0
def save_number():
    for scan_name_file in os.listdir("image"):                                                          #листает все файлы в папке ./image
        full_link = (os.path.abspath(f"image\{scan_name_file}"))                                        #полный поть до файла
        pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"       #
        img = Image.open(full_link)                                                                     #открывает фаил .JPG or .PNG
        text = pytesseract.image_to_string(img)                                                         #конвертирует текст в строку
        numb = (text.replace(" ", "").strip()).replace("-", "").replace("8", "+7", 1)                   #убираем лишнии пробелы
        link_numb = (f"https://wa.me/{numb}")                                                           #подставляем ссылку
        with open("log.txt", "a") as save_file:                                                         #сохраняем в файл log.txt
            save_file.write(link_numb + "\n")                                                           #_______________

save_number()       #ЗАПУСК ФУНКЦИИ