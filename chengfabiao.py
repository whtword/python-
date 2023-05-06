import pyperclip
import pyautogui
import pyperclip
import time

get_msg = ['宝贝','明天去游泳']
get_msg1=['我要去恰饭了','我要去恰饭了','我要去恰饭了','我要去恰饭了','我要去恰饭了','我要去恰饭了','我要去恰饭了'
    , '我要去恰饭了','我要去恰饭了','我要去恰饭了','我要去恰饭了','我要去恰饭了','我要去恰饭了','我要去恰饭了','我要去恰饭了'
    , '我要去恰饭了','我要去恰饭了','我要去恰饭了','我要去恰饭了','我要去恰饭了','我要去恰饭了','我要去恰饭了','我要去恰饭了'
    , '我爱你', '我爱你', '我爱你', '我爱你', '我爱你', '我爱你', '我爱你', '我爱你', '我爱你', '我爱你', '我爱你', '我爱你'
    , '我爱你', '我爱你', '我爱你', '我爱你', '我爱你', '我爱你', '我爱你', '我爱你', '我爱你', '我爱你', '我爱你', '我爱你'
    , '我爱你', '我爱你', '我爱你', '我爱你', '我爱你', '我爱你', '我爱你', '我爱你', '我爱你']
# def get_msg():
#     """想发的消息，每条消息空格分开"""
#     contents ="宝贝 ""宝贝" "宝贝" "宝贝" "宝贝" "宝贝" "宝贝" "宝贝" "宝贝" "宝贝" "宝贝" "宝贝" "宝贝" "宝贝"
#     return contents.split(" ")


def send(msg):
    for i in range(100):
        pyperclip.copy(msg)
        # 模拟键盘 ctrl + v 粘贴内容
        pyautogui.hotkey('ctrl', 'v')
        # 发送消息
        pyautogui.press('enter')





def send_msg(friend):
    # Ctrl + alt + w 打开微信
    pyautogui.hotkey('ctrl', 'alt', 'w')
    # 搜索好友
    pyautogui.hotkey('ctrl', 'f')
    # 复制好友昵称到粘贴板
    pyperclip.copy(friend)
    # 模拟键盘 ctrl + v 粘贴
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    # 回车进入好友消息界面
    pyautogui.press('enter')
    # 一条一条发送消息
    for msg in get_msg:
        send(msg)
        # 每条消息间隔 2 秒
        # time.sleep(1)


if __name__ == '__main__':
    friend_name = "活祖宗"
    send_msg(friend_name)
