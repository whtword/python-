import requests
from bs4 import BeautifulSoup

# 设置请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

# 设置搜索关键词和搜索引擎网址
keyword = '人工智能'
search_engine = 'https://scholar.google.com/'

# 发送请求并获取搜索结果页面
response = requests.get(search_engine, headers=headers, params={'q': keyword})
soup = BeautifulSoup(response.text, 'html.parser')

# 解析搜索结果页面，获取文献信息
results = soup.select('.gs_r.gs_or.gs_scl')
for result in results:
    # 获取文献标题、作者、摘要、出版社等信息
    title = result.select_one('.gs_rt a').text.strip()
    authors = result.select_one('.gs_a').text.strip()
    abstract = result.select_one('.gs_rs').text.strip()
    publisher = result.select_one('.gs_pb').text.strip()

    # 将文献信息保存到文件中
    with open('文献.txt', 'a', encoding='utf-8') as f:
        f.write(f'{title}\n{authors}\n{abstract}\n{publisher}\n\n')

