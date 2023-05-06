import osssssssssss
import time
path = 'D:\\xiaolunwenfangzheng3'
today_time = time.strftime(('%Y-%m-%d'), time.localtime())
print(today_time)
for i in range(5):
    i = str(i)
    print(type(i))
    print(i)
    foldername= path +'\\' + 'result'+i+'-'+today_time
    word_name = osssssssssss.path.exists(foldername)
    if not word_name:
        osssssssssss.makedirs(foldername)

# os.makedirs('D:\\xiaolunwenfangzheng3\\doorandbody1')
# os.makedirs(word_name)