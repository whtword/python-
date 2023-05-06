import requests
import os
import webbrowser
from selenium import webdriver
import time
# keys = '正面碰撞'
# driver = webdriver.Edge(executable_path='C:\Program Files (x86)\Microsoft\Edge\Application\msedgedriver.exe')
# url='https://www.cnki.net/'
# driver.get(url)
# driver.find_element_by_xpath('//*[@id="txt_SearchText"]').send_keys(keys)
# driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[1]/input[2]').click()
# time.sleep(2)
# driver.find_element_by_xpath('//*[@id="gridTable"]/table/tbody/tr[1]/td[9]/a[1]/i').click()
item = input('次数：')
items = int(item)
for i in range(items):
    webbrowser.open('https://sci-hub.et-fine.com/')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 SE 2.X MetaSr 1.0'
        }
    httpurl = 'https://www.baidu.com'
    response = requests.get(httpurl, headers=headers)
    html = response.text
    print(html)




