import requests
from bs4 import BeautifulSoup

# 商品页面的URL地址
url = 'https://detail.tmall.com/item.htm?id=644742788225&ali_refid=a3_430673_1006:1152053504:N:emtiAWsF8%2Bzhhxaiwzc0Aw%3D%3D:f293dfc8fe386e177a5510b2b8d4f321&ali_trackid=1_f293dfc8fe386e177a5510b2b8d4f321'

# 发送请求，获取页面内容
res = requests.get(url)

# 解析页面HTML
soup = BeautifulSoup(res.text, 'html.parser')

# 获取价格信息
price_elements = soup.select('.tm-promo-price .tm-price')
prices = [elem.text.strip() for elem in price_elements]

# 打印价格
print(prices)
