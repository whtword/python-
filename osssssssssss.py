import os,time
import pyautogui as pag
try:
    while True:
            x,y = pag.position() #返回鼠标的坐标
            posStr="鼠标位置:"+"x:"+str(x).rjust(4)+' '+'y:'+str(y).rjust(4)
            print(posStr)#打印坐标
            time.sleep(0.3)
            os.system('cls')#清除屏幕
except  KeyboardInterrupt:
    print('end....')