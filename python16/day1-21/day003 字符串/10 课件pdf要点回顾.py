#!/usr/bin/env python
#-*- coding:utf-8 -*-

#一  大小写转换
"""
1 首字母大写（只是首字母大写，不是每个单词的首字母大写）
2 全部小写
3 全部转换成大写
"""

# 1 首字母大写（只是首字母大写，不是每个单词的首字母大写）
s1 = "hello world"
print(s1.capitalize())  #Hello world

# 2 全部小写
s1 = "Hello World"
print(s1.lower())  #hello world    #对某些字符支持不好
print(s1.casefold()) #hello world  #对所有字母都有效，比如：东欧的字母  (不常用，了解即可)

s2 = "БBß" # 俄美德
print(s2.lower())  #бbß
print(s2.casefold())  #бbss

# 3 全部转换成大写  应用场景：验证码，忽略大小写   重点1
s1 = "Hello World"
print(s1.upper())  #HELLo WORLD
print("-----------1")

#校验验证码
# verify_code = "abCD"
# user_verify_code = input("请输入验证码：")  #字符串类型
# if verify_code.upper() == user_verify_code.upper():  #忽略大小写
#     print("验证成功")
# else:
#     print("验证失败")

#4 大小写互换 大写字母转小写，小写字母转大写
s1 = "Hello World"
print(s1.swapcase())  #hELLO wORLD

#5 每个被特殊字符隔开的单词首字母大写
s1 = "alex is good man"  #空格是特殊字符
print(s1.title())  #Alex Is Good Man
s1 = "alex*is,good_man"  #这里* ， _是特殊字符
print(s1.title())  #Alex*Is,Good_Man
s1 = "alex马云is马化腾good雷军man"  #中文也是特殊字符
print(s1.title())  #Alex马云Is马化腾Good雷军Man
print("-----------2")

#二、切来切去
"""
1 居中 center
2 去空格 strip lstrip rstrip
3 替换 replace
4 分割拆分 split
"""
#1 居中 center
s1 = "alex"
print(s1.center(10)) #   alex      总长度是10 alex左右各3个空格，默认填充符是空格
print(s1.center(10,"*")) #***alex***  参数1是总长度，参数2是填充符号

#2 去掉空白（空白：包含空格，回车换行，tab等）
s1 = "  alex wusir \r\n "
print(s1.strip())  #alex wusir  #去掉两边的空白   重点2
print(s1.lstrip()) #alex wusir  #去掉左边的空白，右边的\r\n没有去掉
print(s1.rstrip()) #  alex wusir  #去掉右边的空表

#去掉指定的子字符串（这个功能也可以通过切片来实现）
s2 = "abcwusirabc"
print(s2.strip("abc")) #wusir  #去掉字符串左右两边指定的字符串"abc"
print(s2.lstrip("abc")) #wusirabc  #去掉字符串左边指定的字符串"abc"
print(s2.rstrip("abc"))  #abcwusir  #去掉字符串右边指定的字符串"abc"
print("-----------3去掉空白")

#典型应用场景：用户输入用户名和密码登录
# usrname = input("请输入用户名:").strip()   #去掉用户输入的空白
# password = input("请输入登录密码:").strip()
# if usrname == "jack" and password == "123":
#     print("登录成功")
# else:
#     print("用户名或者密码输入错误")

#3 替换
s1 = "jack_tom_bob"
print(s1.replace("tom","james")) #jack_james_bob  #参数1是old 参数2是new   重点3
s1 = "jack_tom_tom_tom_bob"
print(s1.replace("tom","alex",2)) #jack_alex_alex_tom_bob
#参数1是old 参数2是new 参数3是从左到右替换次数
# （如果old中是3个tom，替换次数是2，那么就是前面2个tom被替换，最后一个tom不替换）
print("-----------4替换")

#4 分割拆分 split   重点4
s1 ="jack tom  bob"
print(s1.split()) #['jack', 'tom', 'bob']
# 默认的分隔符是空白（空格、tab、回车换行\r\n）--whitespace string，返回的是列表，列表的元素是分割后的子字符串
s1 ="jack*tom*bob"
print(s1.split("*")) #['jack', 'tom', 'bob']
#星号是指定的分隔符，返回的是列表，列表的元素是分割后的子字符串
s1 ="jack*tom*bob"
print(s1.split("*",1)) #['jack', 'tom*bob']
#参数1-星号*是指定的分隔符，参数2是分割次数（从左到右开始），返回的是列表，列表的元素是分割后的子字符串

s2 = """北国风光
千里冰封
万里雪飘"""
print(s2.split("\n"))  #\n是换行符号 \r是回车符号  #['北国风光', '千里冰封', '万里雪飘']
print(s2.split("\n",1))  #['北国风光', '千里冰封\n万里雪飘']

s3 = "jacktombob"
print(s3.split("b")) #['jacktom', 'o', '']
print(s3.split("bob")) #['jacktom', '']
#注意：当分隔符是字符串的最前面或者最后面的字符时，会多出一个空字符串
print("-----------5分割")

#三、格式化输出  --4种方式
print("我是%s,我今年%s,我喜欢%s"%("alex",18,"周杰伦")) #我是alex,我今年18,我喜欢周杰伦   #推荐 最简洁
print("我是{},我今年{}，我喜欢{}".format("alex2",18,"周杰伦")) #我是alex2,我今年18，我喜欢周杰伦
print("我是{1},我今年{0}，我喜欢{2}".format("alex3",18,"周杰伦")) #我是18,我今年alex3，我喜欢周杰伦
# 指定位置的索引号从0开始
print("我是{name},我今年{age}，我喜欢{hobby}".format(name="alex4",age=18,hobby="周杰伦"))
# 我是alex4,我今年18，我喜欢周杰伦   #指定参数名字
print("-----------三 格式化输出")

#四 查找
"""
1 startswith
2 endswith
3 count
4 find   重点5
5 index
"""
#1 判断以什么开头 startswith   重点5
s1 = "jack tom bob"
print(s1.startswith("jack")) #True  #判断是s1是否是以“jack”字符串开头的
print(s1.startswith("jack",0,4)) #True  #参数2和参数3 是取值范围（从索引下标是0开始到3索引下标是3结束）
print(s1.startswith("jack",1,5)) #False
print("-----------四 查找 startswith")

#2 判断以什么结尾 endswith
s1 = "jack tom bob"
print(s1.endswith("bob")) #True  #判断是s1是否是以“bob”字符串结尾的
print(s1.endswith("bob",0,)) #True  #参数2和参数3 是取值范围（从索引下标是0开始到最后结束）
print(s1.endswith("jack",1,5)) #False
print("-----------四 查找 endswith")

#3 计算字符或者子字符串在目标字符串出现的次数  count
s1 = "jack tom bob"
print(s1.count("b"))  #计算字符b在目标字符串出现的次数
print(s1.count("bo"))  #计算字符串"bo"在目标字符串出现的次数
print(s1.count("b",1,5)) #0 计算字符"b"在取值范围（索引下标是1，到索引下标是4）出现的次数
print(s1.count("b",1,)) #2
print("-----------四 查找 count")

#4 返回字符或者子字符串在目标字符串的索引下标号   重点6
s1 = "jack tobm bob"
print(s1.find("o")) #6 #返回字符"o"在目标字符串第一次出现（从左到右）的索引下标号
print(s1.find("ob")) #6 #返回字符串"ob"在目标字符串第一次出现（从左到右）的索引下标号
print(s1.find("ob",1,5)) #-1 #返回字符串"ob"在目标字符串取值范围（索引号从1开始到4结束）第一次出现（从左到右）的索引下标号
                         #如果找不到，就返回-1
print(s1.find("ob",1,-1)) #6 #返回字符串"ob"在目标字符串取值范围（索引号从1开始到-2结束）第一次出现（从左到右）的索引下标号
print("-----------四 查找 find")

#5 返回字符或者子字符串在目标字符串的索引下标号
s1 = "jack tobm bob"
print(s1.index("ob")) #6
# print(s1.index("ob",1,5))  #ValueError: substring not found
"""
find和index的区别：
1、find，当无法找到的时候，返回的索引下标号是-1
2、index，当无法找到的时候，会报错  #ValueError: substring not found
"""
print("-----------四 查找 index")

#五 条件判断（数字字母组成判断# ）
"""
1 判断是否是数字或者字母组成
2 判断是否是数字组成
3 判断是否是字母组成
"""
# 1 判断是否是数字或者字母组成
s14 = "123.16"
s15 = "abc11"
s16 = "_abc!@"
s17 = "73895"
s18 = "838一二壹"
s19 = "abc"
print(s16.isalnum())  #False 因为包含了字母和数字之外的特殊字符_ !@
print(s14.isalnum()) #Fasle 因为包含了字母和数字之外的小数点.
print(s15.isalnum()) #True
print("----------五 条件判断 字母或者数字")

# 2 判断是否是数字组成（不能包含小数点）
print(s14.isdigit()) #False 因为包含了小数点   重点7
print(s17.isdigit()) #True
print(s17.isnumeric()) #True
print(s14.isnumeric()) #False  因为包含了小数点
print(s18.isnumeric()) #True   可以包含一二壹（可以识别中文）
print(s17.isdecimal()) #True
print(s14.isdecimal()) #True   因为包含了小数点
print("----------五 条件判断 数字")

# 3 判断是否是字母组成
print(s15.isalpha()) #False 因为包含了数字11
print(s19.isalpha()) #True
print("----------五 条件判断 字母")

#课上练习
# 用程序实现判断一个数是否是小数
s1 = "-123.16"
"""
思路：
1、去掉-负号  替换replace  strip
2、判断是否是整数isdigit()
3、如果不是整数，判断小数点在字符串中in，且小数点只有1个-count，但不是开头-startswith也不是结尾-endswith
"""
def isfloat(num):
    # num = num.strip("-")  #去掉两边的-
    num = num.replace("-","")  #去掉两边的-
    if num.isdigit(): #判断是否是整数
        print("%s是整数"% num)
    else: #判断是否是小数
        if "." in num and num.count(".") == 1 and not num.startswith(".") and not num.endswith("."):
            print("%s是小数"% num)
        else:
            print("%s不是小数"% num)
isfloat(s1)  #123.16是小数

#六，计算字符串的长度    重点8
s1 = "jack"
print(len(s1)) #4   内置函数，类似print()的写法

#七 迭代
#1可迭代对象的概念：可以一个个往外取值的对象（字符串、列表等）
#可以通过for循环遍历（取值）可迭代对象的每一个元素
# for 变量 in 可迭代对象:
#       pass
"""
1 遍历字符串中的每一个字符
    while-切片
    for循环
2 in的两种用法
    for循环
    判断xxx是否是目标字符串的子集
"""

s1 = "jack"
# 1 遍历字符串中的每一个字符
#     while-切片
count =0
while count <len(s1):  #0-3
    # print(s1[count])   #通过切片，依次获取字符串中每一个字符
    count += 1

#     for循环
# for i in s1:  #从字符串s1中取出每一个字符，赋值给变量i
#     print(i)

# for i in 10:
#     print(i)  #TypeError: 'int' object is not iterable
print("-----------可迭代")

# 2 in的两种用法
#     for循环   #把字符串或者列表的每一个元素获取后，赋值给变量i
#     判断xxx是否是目标字符串的子集

#课上练习 计算在字符串"I am sylar, I'm 14 years old, I have 2 dogs!"中数字出现的次数
# 注意：这里14是当2个数字来统计的，如果14当一个数字统计，如何实现？--正则\d+(扩展)  findall
"""
思路：
1、for循环遍历字符串
2、判断i是否是数字  isdigit()
3、是数字的话，count自增1
"""
s1 = "I am sylar, I'm 14 years old, I have 2 dogs!"
count = 0
for i in s1:
    if i.isdigit():
        count+=1
print(count)  #3

#扩展
import re
s1 = "I am sylar, I'm 14 years old, I have 2 dogs!"
count = 0
print(re.findall("\d+",s1))  #['14', '2']
#参数1是正则表达式，参数2是目标字符串，返回的数列表
# \d+表示1个或者多个数字
result = re.findall("\d+",s1)
print("字符串中含有%s个数字"%len(result))  #字符串中含有2个数字




