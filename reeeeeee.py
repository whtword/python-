import re
#pip install 包名 -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com 镜像源
#正则结构：类型＋量词
# re.search()：查找符合模式的字符，只返回第一个，返回Match对象
# re.match()：和search一样，但要求必须从字符串开头匹配
# re.findall()：返回所有匹配的字符串列表
# re.finditer()：返回一个迭代器，其中包含所有的匹配，也就是Match对象
# re.sub()：替换匹配的字符串，返回替换完成的文本
# re.subn()：替换匹配的字符串，返回替换完成的文本和替换的次数
# re.split()：用匹配表达式的字符串做分隔符分割原字符串
# re.compile()：把正则表达式编译成一个对象，方便后面使用
# \s  表示空格   \n换行符   \r  回车符    \t  tab符号  \YYY八进制符号YYY      \xYY16进制符号YY
#\w表示字符  ()表示组 {}表示次数  [] 表示字符类别和\d差不多,[asdac]匹配这个元组里有的任意字符
text = '1896546541,是164891654654，身高：175，体重：155,4564532453,0571-52152166，barbarbarcarcar'
print(re.findall(r'\d+',text))#+号重复多次
print(re.findall(r'\d{3,4}-{7,8}',text))# {3,4}找到3至4位（包含3和4位）的数字字符串，加杠是组合匹配，{4}：找到四位数的字符串
print(re.findall(r'^\d{10}|\d{7,8}',text))#   ^  表示只有开头的才能匹配得到,，所以只有1896546541才能匹配到
print(re.findall(r'(\w{3})(\1)',text))#(\1)的意思重复\w{3}的内容，即要 满足两个的模式 匹配重复的字符串
print(re.findall(r'.{3}',text))#'.'that's mean similiar with \w,指定类型，代表所有的字符
print(re.findall(r'[1-5]',text))#找出一到五的所有数字
print(re.findall(r'5',text))#找出all字符5
print(re.findall(r'[^5-7]',text))#找出除5—7的所有字符
print(re.findall(r'\d{6}[a-z]{6}',text))#表示6个数字后边跟六个字母
print(re.findall(r'(bar){2}',text))#bar重复1次
print(re.findall(r'.*',text))#   *  0次或者多次，+  一次或者多次
print(re.findall(r'.*',text,flags=re.I))#忽略大小写        \n换行符   \r  回车符    \t  tab符号  \YYY八进制符号YYY      \xYY16进制符号YY
print(re.split(r' \s*[,;/]\s* ','asdasd  ;  fds  fqqw'))