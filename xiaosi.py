import pyperclip
import pyautogui
import pyperclip
import time

get_msg = ['多少沾点']
time.sleep(2)
for i in range(150):
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.hotkey('enter')
    # for msg in get_msg:
    #     pyperclip.copy(msg)
    #     pyautogui.hotkey('ctrl', 'v')
    #     pyautogui.hotkey('enter')

