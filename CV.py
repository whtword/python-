import time
import cv2 as cv
import os
from threading import Thread
import sys
from pynput import keyboard
# import pyto
import easyocr
import torch
image = 'A://dipingxian/aaaaaaaa.png'
ocr = easyocr.Reader(['ch_sim', 'en'],gpu=False)
content = ocr.readtext(image,detail=0)
print(content)





