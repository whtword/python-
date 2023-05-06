import pyautogui
me= input('鼠标连点器逆天点击十万次按l启动左键点击,r启动右键点击:')
pyautogui.rightClick()
if me =='l':
    for i in range(100000):
        pyautogui.click()
if me =='r':
    for i in range(100000):
        pyautogui.rightClick()


