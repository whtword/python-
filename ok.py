from selenium import webdriver
import  bottle
import pymysql
from bottle import route, run
import time

#数据库连接
def con_mysql(sql):
    try:
        # 获取一个数据库连接，注意如果是UTF-8类型的，需要制定数据库
        conn = pymysql.connect(host='localhost', user='root', passwd='admin', db='test', port=3306, charset='utf8')
        cur = conn.cursor()  # 获取一个游标
        cur.execute(sql)
        cur.close()  # 关闭游标
        conn.close()  # 释放数据库资源

    except  Exception:
        print("发生异常")
#页面登录

def login(username, password):
 url = 'https://account.chsi.com.cn/passport/login?service=https://my.chsi.com.cn/archive/j_spring_cas_security_check'
 driver=webdriver.Edge(executable_path='msedgedriver.exe')
 driver.get(url)


 #模拟登录
 driver.find_element_by_id('username').send_keys(username)
 driver.find_element_by_id('password').send_keys(password)
 driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div/div/form/input[4]").click()
 #让这家伙睡会  O(∩_∩)O哈哈~  为什么要睡呢，这是为了模拟手动登录，防止被封
 time.sleep(3)
 driver.refresh()
 # 以上模拟登录算是完成了
 driver.get("https://my.chsi.com.cn/archive/gdjy/xj/show.action")  # 具体要爬取那个页面数据就是那个页面的URL

 time.sleep(2)
 # sql语句我们 参数传值的形式
 sql = '''
         INSERT INTO xue_xin_info VALUES((SELECT REPLACE(UUID(),'-','')),
          '{u_name}','{sex}','{birthday}','{nation}','{identified}',
          '{school_name}','{leve}','{major}','{year_}','{edu_class}',
          '{learning}','{branch_institute}','{department}','{class1}','{stu_no}',
          '{entrance_school}','{graduate_time}','{state}','{photo_address}',NOW())
          '''
 uname = driver.find_element_by_xpath(".//table[@class='mb-table']/tbody/tr[1]/td[1]").text
 u_sex = driver.find_element_by_xpath(".//table[@class='mb-table']/tbody/tr[1]/td[2]").text
 # 2
 u_birthday = driver.find_element_by_xpath(".//table[@class='mb-table']/tbody/tr[2]/td[1]").text
 u_nation = driver.find_element_by_xpath(".//table[@class='mb-table']/tbody/tr[2]/td[2]").text
 # 3
 u_identified = driver.find_element_by_xpath(".//table[@class='mb-table']/tbody/tr[3]/td[1]").text
 u_school_name = driver.find_element_by_xpath(".//table[@class='mb-table']/tbody/tr[3]/td[2]").text
 # 4
 u_leve = driver.find_element_by_xpath(".//table[@class='mb-table']/tbody/tr[4]/td[1]").text
 u_major = driver.find_element_by_xpath(".//table[@class='mb-table']/tbody/tr[4]/td[2]").text
 # 5
 u_year_ = driver.find_element_by_xpath(".//table[@class='mb-table']/tbody/tr[5]/td[1]").text
 u_edu_class = driver.find_element_by_xpath(".//table[@class='mb-table']/tbody/tr[5]/td[2]").text
 # 6
 u_learning = driver.find_element_by_xpath(".//table[@class='mb-table']/tbody/tr[6]/td[1]").text
 u_branch_institute = driver.find_element_by_xpath(".//table[@class='mb-table']/tbody/tr[6]/td[2]").text
 # 7
 u_department = driver.find_element_by_xpath(".//table[@class='mb-table']/tbody/tr[7]/td[1]").text
 u_class = driver.find_element_by_xpath(".//table[@class='mb-table']/tbody/tr[7]/td[2]").text
 # 8
 u_stu_no = driver.find_element_by_xpath(".//table[@class='mb-table']/tbody/tr[8]/td[1]").text
 u_entrance_school = driver.find_element_by_xpath(".//table[@class='mb-table']/tbody/tr[8]/td[2]").text
 # 9
 u_graduate_time = driver.find_element_by_xpath(".//table[@class='mb-table']/tbody/tr[9]/td[1]").text
 u_state = driver.find_element_by_xpath(".//table[@class='mb-table']/tbody/tr[9]/td[2]").text

 driver.get_screenshot_as_file(r"D:\pythonPath\\" + username + ".jpg")
 PHaddress = "D:\pythonPath\\" + username + ".jpg"
 inser_sql = sql.format(u_name=uname, sex=u_sex, birthday=u_birthday, nation=u_nation, identified=u_identified,
                        school_name=u_school_name, leve=u_leve, major=u_major, year_=u_year_, edu_class=u_edu_class,
                        learning=u_learning, branch_institute=u_branch_institute, department=u_department,
                        class1=u_class,
                        stu_no=u_stu_no, entrance_school=u_entrance_school, graduate_time=u_graduate_time,
                        state=u_state, photo_address=PHaddress)
 print(inser_sql)
 con_mysql(inser_sql)
 driver.close()
def main():
    username='18274932375'
    password='study@'
    login(username, password)
if __name__ =="__main__":
    main()

