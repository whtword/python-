import pyautogui

# 显示一个简单的带文字和OK按钮的消息弹窗。用户点击后返回button的文字。
pyautogui.alert(text='', title='', button='OK')
b = pyautogui.alert(text='要开始程序么？', title='请求框', button='OK')
print(b)

pyautogui.confirm(text='', title='', buttons=['OK', 'Cancel']) # OK和Cancel按钮的消息弹窗
pyautogui.confirm(text='', title='', buttons=range(10)) # 10个按键0-9的消息弹窗
a = pyautogui.confirm(text='', title='', buttons=range(10))
print(a)
pyautogui.prompt(text='', title='', default='')

# 样式同prompt()，用于输入密码，消息用*表示。带OK和Cancel按钮。用户点击OK按钮返回输入的文字，点击Cancel按钮返回None。
# pyautogui.password(text='', title='', default='', mask='*')
a=pyautogui.password(text='', title='', default='', mask='')
b = pyautogui.prompt()
print(a)
print(b)