#!/usr/bin/env python
#-*- coding:utf-8 -*-

#五 条件判断
# #1 判断是否由字母和数字组成
# s = "abc123"
# s2 =s.isalnum()
# print(s2)  #True
#
# s = "abc123一二壹"
# s2 =s.isalnum()  #注意:一二 壹 isalnum()也认识
# print(s2) #True
#
# #2 判断是否是字母组成
# s ="abc"
# s2 =s.isalpha()
# print(s2) #True
#
# s ="abc "
# s2 =s.isalpha()  #多了一个空格
# print(s2) #False

#3判断是否是数字组成(整数\十进制整数\中文数字-一二壹等)
# s = "123"
# s2 =s.isdigit()  #判断整数 数字    #重点 判断是否由数字组成
# print(s2) #True
#
# s = "123.2"
# s2 =s.isdigit()  #判断整数 数字
# print(s2) #False

# s = "1.5"
# s2 =s.isdecimal()  #判断十进制数字,而不是判断小数
# print(s2) #False
#
# s = "145"
# s2 =s.isdecimal()  #判断十进制数字,而不是判断小数
# print(s2) #True

# s ="一二壹123"
# s2 =s.isnumeric() #认识中文 一二壹
# print(s2) #True

# s ="一二壹123两"
# s2 =s.isnumeric() #认识中文 一二壹  注意:两 isnumeric认为不是数字
# print(s2) #False

##判断数字的应用场景:购物车,用户在输入菜单的时候,必须保证用户输入的是数字,即可以用上isdigit()

#课上练习:用算法判断某一个字符串是否是小数
s = "-123.12"

"""
思路:
1、先去掉-,用替换-replace
2、先判断是否是整数  -isdigit()
3、如果不是整数的话
    1、计算.出现的次数-count
    2、判断 如果.出现的次数是1且它不是出现在最前面--startswith()，也不是出现在最后面--endswith()
       就是小数
    3、否则，就不是小数

注意点:
1、判断是否是整数时候，是无法判断负号-的，所以要用replace先去掉负号

"""

def isfloat(s):
    s1 = s.replace("-","")  #注意：判断整数的时候，是不能判断负号的-，所有要先去掉负号-
    # print(s1)  #123.12   字符串类型
    if s1.isdigit():
        print("%s是整数"%s)
    else:
        count_point = s.count(".") #计算点 出现的次数是1
        # print(count_point) #1   #
        if count_point == 1 and not s.startswith(".") and not s.endswith("."):
            print("%s是小数"% s)
        else:
            print("%s不是小数"% s)
s="-123.99"  #注意：这里的数必须是字符串类型，才能判断，最后可以用int float转换成数字
isfloat(s)  #-123.99是小数

#六 计算字符串的长度
s = "dfhdhafk"
print(len(s))  #8   内置函数 和print()的写法类型  不是s.函数名()的写法

#七 可迭代
"""
可迭代的概念：可以一个一个往外取值的对象
1、字符串就是可迭代的（列表、字典都是可迭代的）  可以通过索引号的递增来取值
2、数字就不是可迭代的
"""

s = "朱元璋朱棣"
#1while取出字符串的每个字符--nok
count = 0
while count<len(s):
    print(s[count])  #这里的count是索引号  可迭代对象（字符串、列表等）：可以通过索引号的递增来取值
    count+=1
print("----------1")

# #2for取出字符串的每个字符   (可迭代对象-字符串、列表等可以直接用for循环进行遍历，取出其中的元素)
for i in s:  #把可迭代对象的每一个元素，每循环一次，都分别赋值给前面的变量i（方便可迭代对象的遍历）
# for 变量 in 可迭代对象
    pass
    print(i)

"""
in的两种用法
1、不在for中，是判断xxx是非在出现在str中（判断子字符串）--例子：判断敏感词-广告法
2、在for中，是把可迭代对象（字符串、列表等）的每一个元素取出来，赋值给前面的变量i

 4. for循环
for 变量 in 可迭代对象:
     循环体(break, continue)
else:
    当循环正常结束的时候执行else（如果break，就不会执行else）
"""

#计算在字符串串"I am sylar, I'm 14 years old, I have 2 dogs!" 数字的个数
s1 = "I am sylar, I'm 14 years old, I have 2 dogs!"
count=0
for i in s1:
    if i.isdigit():
        # print(i)
        count+=1
print(count)  #统计字符串中有多少个数字

# for i in 10:  #TypeError: 'int' object is not iterable
#     #因为整数10不是可迭代的类型
#     print(i)

for i in "10":  #这里的“10”是字符串，可迭代类型
    print(i)












