from selenium import webdriver
import requests
url = 'https://www.baidu.com'
respone = requests.get(url)
print(respone.text)