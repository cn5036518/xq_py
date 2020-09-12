#!/usr/bin/env python
#-*- coding:utf-8 -*-

# 2.有字符串s = "123a4b5c"
# 1)通过对s切片形成新的字符串s1,s1 = "123"
s = "123a4b5c"
print(s[:3]) #123

# 2)通过对s切片形成新的字符串s2,s2 = "a4b"
print(s[3:6]) #a4b

# 3)通过对s切片形成新的字符串s3,s3 = "1345"
print(s[::2]) #1345

# 4)通过对s切片形成字符串s4,s4 = "2ab"
print(s[1:-1:2]) #2ab

# 5)通过对s切片形成字符串s5,s5 = "c"
print(s[-1]) #c

# 6)通过对s切片形成字符串s6,s6 = "ba2"
print(s[-3::-2]) #ba2
print("-----------切片1")

# 3.使用while和for循环分别打印字符串s="asdfer"中每个元素。
#1 for循环
s = "asdfer"
# for i in s:
#     print(i)

#2 while 循环
count = 0
while count < len(s): #限定范围
    # print(s[count])
    count += 1

# 4. 使用for循环对s = "asdfer"进⾏循环，但是每次打印的内容都是"asdfer"。
s = "asdfer"
# for i in range(len(s)):
#     print(s[:])

# 5 使用for循环对s="abcdefg"进⾏循环，每次打印的内容是每个字符加上sb，
# 例如：asb, bsb，csb,...gsb。
# s="abcdefg"
# for i in s:
#     print(i+"sb")  #asb
#     # print(i,"sb")  #默认是空格  a sb
# print("-----------sb")

# 6.使用for循环对s="321"进⾏循环，打印的内容依次是："倒计时3秒"，"倒计时2秒"，"倒计时1秒"，"出发！"。
s="321"
# for i in s:
#     print("倒计时%s秒" % i)
# else: #当for循环正常结束（条件不满足的）时候，执行else后面的内容；当break后，else就不执行了
# 如果不写else，直接print("出发")，会出现即使for循环break了，下面的“出发”还是可以打印出来---区别
#     print("出发!")

# 7，实现⼀个整数加法计算器(两个数相加)：
# 如：content = input("请输⼊内容:") 用户输⼊：5+9或5+ 9或5 + 9，然后进
# ⾏分割再进⾏计算。
# content = input("请输入内容：").replace(" ","")  #字符串类型  replace去掉空格（包含中间的空格，strip之恩给你去掉两端的空格）
# li1 = content.split("+")
# # sum = int(li1[0]) + int(li1[1])
# sum = 0
# for i in li1:
#     sum = sum + int(i)  #这里的i是字符串，必须转换成整数才能计算
# print(sum)

# 9，计算用户输入的内容中有几个整数（以个位数为单位）。
# 如：content = input("请输入内容：") # 如fhdal234slfh98769fjdla
# content = input("请输入内容：")
content = "fhdal234slfh98769fjdla"
count = 0
for i in content:
    if i.isdigit():
        # print(i)
        count += 1 #自增1， 每次判断是整数就自增1
print(count)
print("-----------------9")

#9-2扩展  计算用户输入的内容中有几个整数（不是以个位数为单位）。
import re
s1 = "fhdal234slfh98769fjdla"
count = 0
print(re.findall("\d+",s1))  #['234', '98769']
#参数1是正则表达式，参数2是目标字符串，返回的是列表
# \d+表示1个或者多个数字
result = re.findall("\d+",s1)
print("字符串中含有%s个数字"%len(result))  #字符串中含有2个数字
print("-----------------9-2")

# 10、写代码，完成下列需求：
# 用户可持续输入（用while循环），用户使用的情况：
# 输入A，则显示走大路回家，然后在让用户进一步选择：
# 是选择公交车，还是步行？
# 选择公交车，显示10分钟到家，并退出整个程序。
# 选择步行，显示20分钟到家，并退出整个程序。
# 输入B，则显示⾛小路回家，并退出整个程序。
# 输入C，则显示绕道回家，然后在让用户进一步选择：
# 是选择游戏厅玩会，还是网吧？
# 选择游戏厅，则显示 ‘一个半小时到家，爸爸在家，拿棍等你。’并让其
# 重新输入A，B,C选项。
# 选择网吧，则显示‘两个小时到家，妈妈已做好了战斗准备。’并让其重
# 新输入A，B,C选项
# count = 0
# while count<11: #限定10次机会   while 1就是无限循环
#     selection = input("请输入ABC：").strip().upper()  #去掉左右两边的空白，忽略大小写
#     if selection == "A":
#         print("走大路回家")
#         while 1:   #这个while内循环是可以不需要的，如果去掉，后面的同级break也同步去掉
#             traffic = input("是选择公交车，还是步行？").strip()
#             if traffic == "公交车":
#                 print("10分钟到家")
#                 # break #退出当层整个循环（内循环）
#             elif traffic == "步行":
#                 print("20分钟到家")
#             break  # 退出当层整个循环（内循环）  #公交车和步行的break 合二为一，代码优化，少一行
#         break ##退出当层整个循环（外循环）
#     elif selection == "B":
#         print("走小路回家")
#         break #退出当层整个循环（外循环）
#     elif selection == "C":
#         print("绕道回家")
#         while 1:  #这个while内循环是可以不需要的，如果去掉，后面的break也同步去掉
#             choice = input("是选择游戏厅玩会，还是网吧？").strip()
#             if choice == "游戏厅":
#                 print("一个半小时到家，爸爸在家，拿棍等你")
#                 # break  # 只退出当层整个循环（内循环）
#             elif choice == "网吧":
#                 print("两个小时到家，妈妈已做好了战斗准备。")
#             break  # 只退出当层整个循环（内循环）
#     else:
#         print("请重新输入")
#     count += 1

# 11、写代码：计算 1 - 2 + 3 ... + 99 中除了88以外所有数的总和
sum_odd = 0   #sum累加的初始值是0；累乘的话，初始值就是1（不能是0）
sum_even = 0
for i in range(1,100):
    if i%2 == 1: #奇数
        sum_odd = sum_odd + i
        #sum_odd第一次取值0 第二次取值0+1 第三次取值0+1+3
    else:
        if i == 88:  #for循环自带自增1的功能  类似while的count+=1
            continue  #当i=88的时候，不进行累加
        sum_even = sum_even + i
sum = sum_odd - sum_even
# print(sum) #138

# 13. 输入⼀个字符串，要求判断在这个字符串中大写字母，小写字母，数字(isdigit())，
# 其它字符共出现了多少次，并输出来
# s1 = "DFdj12*&"
# for i in s1:
#     print(i)
# print(len(s1))
content = "DFdj12*&q"
count = 0
for i in content:
    if i.isdigit() or i.upper() == i or i.lower() == i:
        # print(i)
        count += 1 #自增1， 每次判断是整数就自增1
print(count)  #9
print("-----------------13")

# 14、制作趣味模板程序需求：等待用户输入名字、地点、爱好，根据用户的名
# 字和爱好进⾏任意实现 如：敬爱可亲的xxx，最喜欢在xxx地⽅干xxx
# name = input("请输入姓名：")
# address = input("请输入地点：")
# hobby = input("请输入爱好：")
# print("敬爱可亲的%s,最喜欢在%s地方干%s" % (name,address,hobby))

# 8，升级题：实现⼀个整数加法计算器（多个数相加，长度是不定的）：
# 如：content = input("请输入内容:") 用户输入：5+9+6+12+ 13，然后进⾏
# 分割再进⾏计算。
# content = input("请输入内容:").replace(" ","") #字符串类型  replece用于去掉中间的空格
content = "5+9+6+12+ 13".replace(" ","")
li1 = content.split("+")
print(li1) #['5', '9', '6', '12', '13']
sum = 0
for i in li1:
    sum = sum + int(i) #这里的i是字符串，必须转换成整数才能计算
    #sum第一次取值是0 第二次取值是0+5 第三次取值是0+5+9
    # print(int(i))
print(sum) #45

# 12. (升级题)判断⼀句话是否是回文. 回文: 正着念和反着念是一样的. 例如, 上海
# 自来水来自海上(升级题)
#方法1 简便方法
s1 = "aba"
def palindrome(str1):
    if s1 == s1[::-1]:  #判断回文   s1[::-1]是反转
        print("是回文")
    else:
        print("不是回文")
palindrome(s1)

#方法2 算法实现  while实现字符串的反转
"""
"""
s0 = ""  #定义空字符串
s1 = "aba"
count = len(s1)-1  #最后一个字符的索引下标号
while count >= 0:
    s0 = s0 + s1[count] # 字符串的累计拼接--就是累加（和数字的累加类似）
    #s0第一次取值是"" 第二次取值是"a"（倒数第一个字符） 第三次取值是"ab"（倒数第一个字符+倒数第二个字符）
    # print(s1[count])
    count -= 1 #自减1
print(s0)  #aba
if s0 == s1:
    print("是回文")
else:
    print("不是回文")

# 方法3 算法实现  for
s0 = ""
s1 = "aba"
for i in s1[::-1]:#这里while可以去到索引号，for循环无法取到索引号，而是直接取元素
    s0 = s0 + i  # 字符串的累计拼接--就是累加（和数字的累加类似）
# s0第一次取值是"" 第二次取值是"a"(倒数第一个字符) 第三次取值是"ab"（倒数第一个字符+倒数第二个字符）
print(s0) #aba

# 15. (升级题) 给出百家姓. 然后用户输入一个人的名字. 判断这个人是否是百家
# 姓中的姓氏(升级题)
# 百家姓:
# first_names = """
# 赵钱孙李李，周吴郑王。
# 冯陈褚卫，蒋沈沈韩杨。"""

first_names = """赵钱孙李李，周吴郑王。
冯陈褚卫，蒋沈沈韩杨。
欧阳"""

s1 = "王海波"
if s1[0] in first_names:  #只考虑单姓，没有考虑复姓-欧阳、上官等
    print("此人是百家姓的姓氏")
else:
    print("此人不是百家姓的姓氏")

s1 = "欧阳海波"
if s1[0] in first_names or s1[:2] in first_names:  # 除了考虑单姓，也考虑复姓-欧阳、上官等
    print("此人是百家姓的姓氏")
else:
    print("此人不是百家姓的姓氏")



