# 1135 y:1008
# 1721 y: 859
# 1724 y: 841
# 357 y: 518
# 2057 y:1311
# 536 y: 290
# 1250 y: 546
# 1194 y:1007shuangren
# 1168 y:1050
# 847 y: 179
# 561 y: 490
import pyautogui
import time
import os
import ctypes

option1 = input('双人还是单人？2 or1 ')
option = str(option1)
# if option == 2:

os.popen('C:\\Users\Public\Desktop\WeGame.lnk')
time.sleep(3)
pyautogui.click(1724,841)
time.sleep(2)
pyautogui.click(847,179)
time.sleep(2)
pyautogui.click(449,436)
time.sleep(0.5)
pyautogui.click(2057,1311)
time.sleep(18)
pyautogui.click(536,290)
time.sleep(1)
pyautogui.click(1250,546)
if option == '2':
    pyautogui.click(1194,1007)
    pyautogui.click(1171,1266)
elif option=='1':
    pyautogui.click(1168,1050)
    pyautogui.click(1171, 1266)

