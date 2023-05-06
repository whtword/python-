import os
import time
import requests
import re

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0'}

response = requests.get('https://www.vmgirls.com/12985.html', headers=headers)
print(response.text)
# print(req.request.headers)
html = response.text

# 解析网页
dir_name =re.findall('<h1 class="post-title h3">(.*?)</h1>', html)[-1]
if not os.path.exists(dir_name):
    os.mkdir(dir_name)

urls = re.findall('<a href="(.*?)" alt=".*?" title=".*?">', html)  # 正则表达式解析网页
print(urls)

# 保存图片
for url in urls:
    time.sleep(1)  # 延时1秒
    # 图片名字
    file_name = url.split('/')[-1]  # 文件命名
    response = requests.get(url, headers=headers)
    with open(dir_name + '/' + file_name, 'wb') as f:  # 以2进制形式写入文件名
        f.write(response.content)