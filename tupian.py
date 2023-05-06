import requests
import re
import time
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36 Edg/100.0.1185.29'
}
response = requests.get('https://www.tooopen.com/img/88_878.aspx',headers=headers)
html = response.text
urls = re.findall('<img data-original="(.*?)" src="(.*?)" data-default-img="84x84" alt="(.*?)" title="(.*?)">'
       ,html)
print(urls)
print(response)
filename = 'A:\name\aaa.txt'
for url in urls:
    response = requests.get(url, headers=headers)
    with open(filename, 'wb') as f:
        f.write(response.content)

