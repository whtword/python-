import pyautogui
import time
def mouseclic(img):
    for i in range(3):
        while True:
            location = pyautogui.locateCenterOnScreen(img, confidence=0.9)
            if location is not None:
                pyautogui.hotkey('ctrl', 'alt', 'a')
                pyautogui.click(clicks=2)
                pyautogui.click(location.x, location.y, clicks=1, interval=0.2, duration=0, button='left')
                time.sleep(1)
                pyautogui.hotkey('ctrl', 'v')
                pyautogui.hotkey('enter')
                pyautogui.hotkey('alt','f4')
                pyautogui.moveTo(sizex / 2, sizey / 2, duration=1)
                break
            print("未找到匹配图片,0.1秒后重试")
            time.sleep(0.1)
        # time.sleep(10500)
imgs = "D:\guii\step7.png"
sizex, sizey = pyautogui.size()
mouseclic(imgs)