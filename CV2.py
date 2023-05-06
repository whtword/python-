import pytesseract
from PIL import Image
img = "A:\dipingxian\eeeee.jpg"
pytesseract.pytesseract.tesseract_cmd = 'C://Program Files (x86)/Tesseract-OCR/tesseract.exe'
text = pytesseract.image_to_string(Image.open(img),lang='chi_sim')
print(text)