import pyautogui
import time
import openpyxl
file = 'D:\\1.xlsx'
workbook = openpyxl.load_workbook(file)
sheet1 = workbook['Sheet1']
cell = sheet1['A1:A50']
print(cell)
for cells in cell:
    imgs = cells[0].value
    print(imgs)
    imgs1=imgs.strip('""')
    print(imgs1)
    while True:
        location = pyautogui.locateCenterOnScreen(imgs1, confidence=0.9)
        if location is not None:
            pyautogui.click(location.x, location.y, clicks=1, interval=0, duration=0, button='left')
            break
        print("未找到匹配图片,0.1秒后重试")
        time.sleep(0.1)
    # for img in imgs:
    #     print(img)

#     imgs.appends
# imgs = []
# a=input('输入第一个图片地址：')
# imgs.append(a)
# b=input('输入第一个图片地址：')
# imgs.append(b)
# print(imgs)




# imgs = ["D:\q.png",'D:\w.png','D:\e.png'
#
#
# ]





