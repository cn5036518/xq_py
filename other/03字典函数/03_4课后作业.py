#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""
2 以下不能创建一个字典的语句是
A、dict1 = {}
B、dict2 = { 3 : 5 }
C、dict3 = {[1,2,3]: “uestc”}
D、dict4 = {(1,2,3): “uestc”}

3 以下代码输出什么
dict1={'1':1,'2':2}
theCopy=dict1.copy()
dict1['1']=5
sum=dict1['1']+theCopy['1']
print(sum)

4 有两个字典分表为dict1 = {3:"c", 4:"d"}和dict2 = {1:"a", 2:"b"}，请实现对他们进行合并并输出为{1: 'a', 2: 'b', 3: 'c', 4: 'd'}
提示：可以使用update函数，语法为：xxx.update(yyy)

5 无return的函数，返回什么？

6 如何在一个function里面设置一个全局的变量？

7 输入一个标准的日期如(20160503)，打印对应的年月日即2016年05月03日

8 写一个函数，实现随机生成6位验证码，验证码从0-9A-Za-z中随意生成
思路提示：
1）搞一个空list进行追加
2）利用random.sample(指定的数据, 获取的长度)函数来实现获取任意的6位数据

下次课预告：
模块、文件、异常处理等
上课之前把我给你的文档简单看下，了解下即可，都是一些参数介绍，主要是写的时候知道在哪里看即可

平时我不在有事情可以找助教，有可能助教也比较忙不能即使回复，都理解下，淡定点哈

摆正心态，多练习才是王道，不要看着简单就觉得简单，你动起手来就知道自己会犯很多低级错误了，有问题自己要多思考。
"""

# 2 以下不能创建一个字典的语句是
# A、dict1 = {}    #能，空列表
# B、dict2 = { 3 : 5 } #能，key是不可变的数字
# C、dict3 = {[1,2,3]: “uestc”}  #不能，key是可变类型的列表，不可哈希
# D、dict4 = {(1,2,3): “uestc”}  #能，key是不可变的元组，

dict1 = {}    #能，空列表
dict2 = { 3 : 5 } #能，key是不可变的数字
# dict3 = {[1,2,3]: "uestc"}  #不能，key是可变类型的列表，不可哈希  #TypeError: unhashable type: 'list'
dict4 = {(1,2,3): 'uestc'}  #能，key是不可变的元组，

# 3 以下代码输出什么
dict1={'1':1,'2':2}
theCopy=dict1.copy()  #theCopy={'1':1,'2':2}
dict1['1']=5  #dict1={'1':5,'2':2}
sum=dict1['1']+theCopy['1'] #5+1
print(sum) #6

# 4 有两个字典分表为dict1 = {3:"c", 4:"d"}和dict2 = {1:"a", 2:"b"}，
# 请实现对他们进行合并并输出为{1: 'a', 2: 'b', 3: 'c', 4: 'd'}
# 提示：可以使用update函数，语法为：xxx.update(yyy)

#合并列表用extend 合并字典用update
li1=[1,2]
li2=[3,4]
li1.extend(li2) #将列表2的元素合并到列表1
print(li1) #[1, 2, 3, 4]

dict1 = {3:"c", 4:"d"}
dict2 = {1:"a", 2:"b"}
dict1.update(dict2) #将字典2的元素-键值对合并到字典1
print(dict1) #{1: 'a', 2: 'b', 3: 'c', 4: 'd'}

# 5 无return的函数，返回什么？  None

#6 如何在一个function-函数里面设置一个全局的变量？global关键字
counter=0
def fun1():
    global counter #将函数内的局部变量升级成全局变量
    counter+=1

fun1()
print(counter) #1

# 7 输入一个标准的日期如(20160503)，打印对应的年月日即2016年05月03日
print("%s年%s月%s日"%("2016","05",'03'))  #2016年05月03日  %s是字符串的占位符
print("%d年%d月%d日"%(2016,5,3))  #2016年5月3日  %d是数字的占位符
# 注意：5是数字，05不是数字，而是字符串，需要加引号"05"才行
#上述是直接格式化输出，并没有输入的过程

# #2 改进思路
# #1、先input接收输入，保存在变量
# #2、将变量格式化输出
# a=input("请输入年份:") #输入的都是字符串 因此下面用%s当占位符
# b=input("请输入月份:")
# c=input("请输入日子:")
# print("%s年%s月%s日"%(a,b,c))

# #3 函数的实现思路
# #1、先input接收输入，保存在变量
# #2、函数输出
# a=input("请输入年份:") #输入的都是字符串 因此下面用%s当占位符
# b=input("请输入月份:")
# c=input("请输入日子:")
# def func1(x,y,z):
#     print("%s年%s月%s日"%(x,y,z))
# func1(a,b,c)

#4 字符串切片的思路--推荐
#1 定义一个字符串
#2通过切片分别取出年（前4位）-月（第5,6位）-日（最后2位），然后格式化输出
data1= "20160503"
print("%s年%s月%s日"%(data1[0:4],data1[4:6],data1[-2:]))
print("===============")

#7 反转输出字符串，把abcd变成dcba(可以多个方法实现)
str1="abcd"
str2=str1[::-1]  #dcba  这个除了适用字符串反转，同时适用列表的反转 这里的-1表示步长，从右到左
# str2=str1[-1::-1] #dcba 第一个-1表示最后一位是起始位 从右往左
# str2=str1[-1:0:-1] #dcb 第一个-1表示最后一位是起始位 从右往左 中间的0表示第一位是结束位（不包含）
print(str2) #
print("===============")
"""
总结：关于反转   从右到左的话，步长就是负数，从左到右，步长就是正数
    str2=str1[::-1]
    str2=str1[-1:0:-1]
  这里：参数1是切片起始点   -1表示起始位是最后一位
        参数2是切片结束点0   0表示结束位是第一位（不包含）
        参数3是步长-1        步长-1表示从右往左
"""

# 8 写一个函数，实现随机生成6位验证码，验证码从0-9A-Za-z中随意生成
# 思路提示：
# 1）搞一个空list进行追加
# 2）利用random.sample(指定的数据, 获取的长度)函数来实现获取任意的6位数据
#思路1：a-z全部追加 本办法
#思路2：a对应的阿斯克码是97  A对应的阿斯克码是65 转换优化

#思路1：一个一个添加到空列表，笨办法
li1=[]
li1.append(0)
li1.append(1)
li1.append("a")
li1.append("A")
print(li1) #[0, 1, 'a', 'A']

import random  #导入内置库-包random-随机函数包
result1= random.sample(li1,2)
print(result1)  #从列表的四个元素中随机取2个元素  #[1, 'A']
result2 = [str(i) for i in result1]  #将列表的元素全部转换成字符串
str1="".join(result2) #通过空白连接符，连接列表中的字符串（如果列表中有数字，需要将数字转换成字符串才能连接,否则报错）
print(str1)  #1A   验证码是字符串，而不是列表
print("================")

#思路2：for循环添加到空列表，改进办法
li1=[]
for i in range(0,10): #添加数字
    li1.append(i)
# print(li1) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(65,91): #添加大写字母
    li1.append(chr(i))  #chr(65) 是将数字65，转换成阿斯克码-ascii是65的字母“A”
# print(li1) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C'
for i in range(97,122): #添加小写字母
    li1.append(chr(i))
# print(li1)
import random  #导入内置库-包random-随机函数包
li2= random.sample(li1,6)
print(li2) #[8, 'Y', 'r', 6, 'T', 'W']
li3 = [str(i) for i in li2] #将列表的元素全部转换成字符串
print(li3) #['8', 'Y', 'r', '6', 'T', 'W']
str1="".join(li3) #通过空白连接符，连接列表中的字符串（如果列表中有数字，需要将数字转换成字符串才能连接,否则报错）
print(str1)  #avox8F  #验证码是字符串，而不是列表
print("================")

# li1=[8, 'Y', 'r', 'T', 'W']  #如果列表中有数字和字符串，需要转换成字符串才能连接,否则报错
li1=['8', 'Y', 'r', 'T', 'W']
# li1=[8, 9] ##如果列表中有数字，需要将数字转换成字符串类型才能连接,否则报错
str1="".join(li1)  #TypeError: sequence item 0: expected str instance, int found
print(str1)
print("================")

print(chr(65)) #A  是将数字65，转换成阿斯克码是65的字母“A”   chr是数字转换从字符-chr是字符英文单词前三位
print(ord("A")) #65  是将字母"A"，转换成字母对应的阿斯克码

#思路3 产生6位验证码 函数形式，不传参数
import random
def generate_verifycode3():
    li1 = []
    for i in range(0, 10):  # 添加数字
        li1.append(i)
    # print(li1) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(65, 91):  # 添加大写字母
        li1.append(chr(i))  # chr(65) 是将数字65，转换成阿斯克码-ascii是65的字母“A”
    # print(li1) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C'
    for i in range(97, 122):  # 添加小写字母
        li1.append(chr(i))
    # print(li1)
    import random  # 导入内置库-包random-随机函数包
    li2 = random.sample(li1, 6)
    print(li2)  # [8, 'Y', 'r', 6, 'T', 'W']
    li3 = [str(i) for i in li2]  # 将列表的元素全部转换成字符串
    print(li3)  # ['8', 'Y', 'r', '6', 'T', 'W']
    str1 = "".join(li3)  # 通过空白连接符，连接列表中的字符串（如果列表中有数字，需要将数字转换成字符串才能连接,否则报错）
    print(str1)
    return str1  #将6位验证码的字符串返回

#调函数
str1=generate_verifycode3()
print(str1)
print("-----------------")

#思路4 产生6位验证码 函数形式，传参数-验证码位数--默认参数
import random
def generate_verifycode(len=6):  #默认参数
    pass
    li1 = []
    for i in range(0, 10):  # 添加数字
        li1.append(i)
    # print(li1) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(65, 91):  # 添加大写字母
        li1.append(chr(i))  # chr(65) 是将数字65，转换成阿斯克码-ascii是65的字母“A”
    # print(li1) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C'
    for i in range(97, 122):  # 添加小写字母
        li1.append(chr(i))
    # print(li1)
    import random  # 导入内置库-包random-随机函数包
    li2 = random.sample(li1, len)
    print(li2)  # [8, 'Y', 'r', 6, 'T', 'W']
    li3 = [str(i) for i in li2]  # 将列表的元素全部转换成字符串
    print(li3)  # ['8', 'Y', 'r', '6', 'T', 'W']
    str1 = "".join(li3)  # 通过空白连接符，连接列表中的字符串（如果列表中有数字，需要将数字转换成字符串才能连接,否则报错）
    print(str1)
    return str1  #将6位验证码的字符串返回

#调函数
str2=generate_verifycode(5)  #产生5位验证码，如果不传参数，默认产生6位验证码
print(str2)
print("-----------------")

#思路5 列表中0-9的数字，添加的时候，就从int转换成str字符串类型
import random
def generate_verifycode2(len=6):  #默认参数
    pass
    li1 = []
    for i in range(0, 10):  # 添加数字
        li1.append(str(i))  #将数字转换成str字符串类型  对应259行（如果列表中有数字，需要将数字转换成字符串才能连接,否则报错）
    # print(li1) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(65, 91):  # 添加大写字母
        li1.append(chr(i))  # chr(65) 是将数字65，转换成阿斯克码-ascii是65的字母“A”
    # print(li1) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C'
    for i in range(97, 122):  # 添加小写字母
        li1.append(chr(i))
    # print(li1)
    import random  # 导入内置库-包random-随机函数包
    li2 = random.sample(li1, len)
    print(li2)  # [8, 'Y', 'r', 6, 'T', 'W']
    # li3 = [str(i) for i in li2]  # 将列表的元素全部转换成字符串  #前面第246行已经将数字转换成了字符串
    # print(li3)  # ['8', 'Y', 'r', '6', 'T', 'W']
    str1 = "".join(li2)  # 通过空白连接符，连接列表中的元素形成字符串
    # （如果列表中有数字，需要将数字转换成字符串才能连接,否则报错）
    print(str1)
    return str1  #将6位验证码的字符串返回

#调函数
str3=generate_verifycode2(5)  #产生5位验证码，如果不传参数，默认产生6位验证码
print(str3)
print("-----==------==------")


"""
伪代码
1、for循环依次将数字，大写字母，小写字母添加到空列表li1
2、大写字母的添加通过chr（65）
3、random.sample(li1,6)函数随机从列表中选取6个元素，组成新的列表li2
   导入ramdom包
4、将新的列表li2的所有元素都转换成字符串，形成新的列表li3（也可以在前面添加数字到列表的时候，就将数字转换成str字符串）
   li3 = [str(i) for i in li2] #表达式
5、6位随机验证码的类型是字符串，而不是列表
   通过str1="".join(li3) ,将列表的元素通过空白符连接成字符串
   （注意：这里通过join将列表的元素通过空白符连接成字符串的时候，列表的元素必须全部是字符串，数字必须转换成字符串
    否则，报错）

知识点总结
1、for循环，空列表
2、chr(65) 数字转换成字母
3、random.sample(li1,6)函数--随机从列表中选取6个元素
4、li3 = [str(i) for i in li2]  --将列表的元素全部转换成字符串，便于后面的join
   （也可以在前面添加数字到列表的时候，就将数字转换成str字符串）
5、str1="".join(li3) --将列表的元素通过空白连接符转换成6位字符串
"""

#一、字符串反转，函数形式
#方式1  推荐简洁
str1="abc"
str2=str1[::-1]
print(str2) #"cba"

#函数
def str_reverse1(str1): #形参
    return str1[::-1]

#调用
str1="abc"
str2= str_reverse1(str1) #实参
print(str2) #cba

#方式2  倒着取下标，理解思路
str1="abc"
str2=""
for i in str1:
    str2+=i #正向取下标，复制字符串
print(str2) #abc

str1="abc"
str2=""
for i in range(len(str1)-1,0,-1):
    str2+=str1[i]  ##反向取下标，反转字符串
print(str2) #cb

str1="abc"
str2=""
for i in range(len(str1)-1,-1,-1):#参数2是-1，下标会取到-1的前一个0  参数3是-1，负数，表示从右往左取
    str2+=str1[i]  ##反向取下标，反转字符串
print(str2) #cba
print("=============")

#函数
def str_reverse3(str1):
    str2 = ""
    for i in range(len(str1) - 1, -1, -1):
        str2 += str1[i]
    return str2

#调用
str1="abc"
str2=str_reverse3(str1)
print(str2) #cba

#二、字符串的倒序排列
#方式1  sorted不是反转，而是倒序排列
str1="abdc"
li2=sorted(str1,reverse=True)
print(li2) #['d', 'c', 'b', 'a']
str2="".join(li2)
print(str2) #dcba
print("=============")

#函数
def str_reverse2(str1):
    li2=sorted(str1,reverse=True)
    return "".join(li2)

#调用
str1="abdc"
str2 = str_reverse2(str1)
print(str2) #dcba
print("=============")

#三、列表元素反转，函数形式
#方式1  推荐简洁
li1=[1,3,2]
li2=li1[::-1]
print(li2) #[2, 3, 1]

#函数
def str_reverse1(li1): #形参
    return li1[::-1]

#调用
li1=[1,3,2]
li2= str_reverse1(li1) #实参
print(li2) #[2, 3, 1]
print("=======")

#方式2  倒着取下标，理解思路
#函数
def str_reverse3(li1):
    li2 = []
    for i in range(len(li1) - 1, -1, -1):
        li2.append(li1[i])
    return li2

#调用
li1=[1,3,2]
li2=str_reverse3(li1)
print(li2) #[2, 3, 1]







