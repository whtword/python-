from selenium import webdriver
import requests
import random
import pyperclip
import time
import pyautogui

driver = webdriver.Edge(executable_path='C:\Program Files (x86)\Microsoft\Edge\Application\msedgedriver.exe')
driver.get('https://www.scidown.cn/')
time.sleep(2)
driver.find_element_by_xpath('//*[@id="TuTuJieXi"]/div/div[1]/div[2]/div/div/div[2]/form/input').click()
pyperclip.paste()
pyautogui.hotkey('ctrl','v')
driver.find_element_by_xpath('//*[@id="TuTuJieXi"]/div/div[1]/div[2]/div/div/div[3]/button').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="TuTuJieXi"]/div/div[2]/div/div[1]/div/div/form[1]/div/input[2]').click()
# driver.find_element_by_xpath('//*[@id="buttons"]/ul/li[2]').click()
# def main():
#
#
#
#
# if __name__ =="__main__":
#     main()