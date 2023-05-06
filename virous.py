import requests
url = 'http://xxmh1016.com/#/pages/user/index'
headers = {
'Accept': '*/*',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
'appId': '870C0F71027B077B1783B1913D8B46DD',
'Connection': 'keep-alive',
'Content-Length': '99',
'Content-Type': 'application/json',
'Origin': 'http://xxmh1016.com',
'Referer': 'http://xxmh1016.com/',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.47'}
response = requests.get(url,headers=headers)
print(response.text)
print(response)