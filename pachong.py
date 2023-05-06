import requests

import osssssssssss

from bs4 import BeautifulSoup

from urllib.request import urlretrieve

def main():
    url = 'http://www.onegreen.net/maps/List/List_933.html'

    osssssssssss.makedirs('./img/', exist_ok=True)  # 创建目录存放文件

    html = requests.get(url).text  # 获取网页html

    soup = BeautifulSoup(html,'lxml')

    img_url = soup.find_all('img')  # 获取所有的img标签,我在这里只是演示下载，所有不做进一步的筛选

    print(len(img_url))

    for url in img_url:ul = url['src']  # 获取src属性

    img = 'http://www.onegreen.net/' + ul  # 补全图片url

    print(img)



    urlretrieve(img, './img/%s' % ul.split('/')[-1])  # 存储图片



if __name__ =='__main__':
    main()

