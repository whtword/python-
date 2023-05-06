import os
import subprocess
import pyautogui
import time
# print(os.system('adb shell input tap 200 1000 '))
# print(os.system('adb shell input tap 200 300 '))
# print(os.system('adb shell input keyevent 41 '))
# print(os.system('adb shell input keyevent 33 '))
# print(os.system('adb shell input keyevent 37 '))
# print(os.system('adb shell input keyevent 46 '))
# print(os.system('adb shell input keyevent 37 '))
# print(os.system('adb shell input keyevent 62 '))
# print(os.system('adb shell input tap 400 1000 '))
# print(os.system('adb shell input tap 200 700 '))#搜索后的进入打卡坐标
def daka():
    print(os.system('adb shell input tap 200 1000 '))  # 桌面启动钉钉
    time.sleep(4)
    print(os.system('adb shell input tap 500 2100 '))  # 控制台
    print(os.system('adb shell input tap 400 300 '))  # 搜索
    print(os.system('adb shell input keyevent 41 '))
    print(os.system('adb shell input keyevent 33 '))
    print(os.system('adb shell input keyevent 37 '))
    print(os.system('adb shell input keyevent 46 '))
    print(os.system('adb shell input keyevent 37 '))
    print(os.system('adb shell input keyevent 62 '))
    time.sleep(2)
    print(os.system('adb shell input tap 200 700 '))  # 搜索后的进入打卡坐标
    time.sleep(2)
    print(os.system('adb shell input tap 200 1500 '))  # 进入今日的表单
    time.sleep(2)
    print(os.system('adb shell input tap 500 2100 '))
    print(os.system('adb shell input swipe 747 1413 747 323'))  # 向下滑动
    print(os.system('adb shell input swipe 747 1413 747 323'))
    time.sleep(2)
    print(os.system('adb shell input tap 1000 1600 '))
    time.sleep(1)
    print(os.system('adb shell input swipe 747 1413 747 0'))
    print(os.system('adb shell input swipe 747 1413 747 0'))
    print(os.system('adb shell input tap 700 1800 '))

daka()















# os.system('adb shell input tap 100 300')
# print(os.system('adb shell input keyevent 224'))
# print(os.system('adb shell input tap 100 300 '))
# adb shell input swipe 747 1413 747 323
# for i in range(10000):
#     print(os.system('adb shell input swipe 747 1413 747 323'))
#     print('滑动第',i,'次')
# print(os.system('adb shell pm list packages '))
# print(os.system('adb shell am start -n com.tencent.mm/.ui.LauncherUI'))
# print(os.system('adb shell input keyevent 62 '))
# os.system('adb shell input tap 100 300')
# print(os.system('adb shell input keyevent 224'))
# print(os.system('adb shell input tap 100 300 '))
# print(os.system('adb" "shell" "input" "keyevent" "37" "'))
# pyautogui.typewrite('adb shell input keyevent 37')
# print(os.system('cmd'))
# cmd = '"adb shell input keyevent 62 " "-h"'
# ps = subprocess.Popen(cmd)
# pyautogui.hotkey('win','r')
# pyautogui.hotkey('enter')
# pyautogui.typewrite('adb shell input keyevent 41 ')
# pyautogui.hotkey('enter')
# time.sleep(1)
# pyautogui.typewrite('adb shell input keyevent 33 ')
# pyautogui.hotkey('enter')
# time.sleep(1)
# pyautogui.typewrite('adb shell input keyevent 37 ')
# pyautogui.hotkey('enter')
# time.sleep(1)
# pyautogui.typewrite('adb shell input keyevent 46 ')
# pyautogui.hotkey('enter')
# time.sleep(1)
# pyautogui.typewrite('adb shell input keyevent 37 ')
# pyautogui.hotkey('enter')
# time.sleep(1)
# pyautogui.typewrite('adb shell input keyevent 62 ')
# pyautogui.hotkey('enter')
# time.sleep(2)
# pyautogui.typewrite('adb shell input tap 200 700 ')
# pyautogui.hotkey('enter')


# ps.wait()