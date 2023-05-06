import requests
import re
import time
import os
t = time.strftime('%Y-%m-%d_%H.%M.%S',time.localtime(time.time()))
headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 SE 2.X MetaSr 1.0'
}
pic = input('请输入url：')
httpurl =pic
response = requests.get(httpurl,headers = headers)
html = response.text
urls = re.findall(r'<a rel="nofollow" href="(.*)" alt=".*" title=".*">',html)
tile = re.findall(r'<img alt="(.*)" src=".*" alt=".*"/>',html)
# print(html)
tile1 = tile[1]
print(tile)
i = 0
for url in urls:
    t = time.strftime('%Y-%m-%d_%H.%M.%S', time.localtime(time.time()))
    # file_name = t+url.split('/')[-1]
    i = i+1
    # a , b = os.path.splitext(url)
    # '.' + url.split('.')[-1]
    # print(b)
    file_name =tile1+' '+'Picture'+' '+str(i)+' '+t+ '.'+url.split('.')[-1]
    print(file_name)
    response = requests.get(url,headers=headers)
    with open('A:\gggg'+'\\'+file_name,'wb') as f:
        f.write(response.content)
