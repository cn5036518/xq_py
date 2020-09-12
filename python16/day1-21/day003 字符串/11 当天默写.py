#!/usr/bin/env python
#-*- coding:utf-8 -*-

# 默写内容：
# 分别用while，for循环输出字符串s = input（"你想输入的内容"）的每一个字符。
# s1 = input("你想输入的内容：")  #字符串类型
# 方法1
# # for i in s1:
# #     print(i)
#
# 方法2
# count = 0
# while count<len(s1):#限定范围
#     # print(s1[count])  #通过切片完成，每个字符的输出
#     count+=1  #for循环自带-自增1的功能

name = "aleX leNb"
# 1.有变量name = "aleX leNb" 完成如下操作：
# 1)移除 name 变量对应的值两边的空格,并输出处理结果
print(name.strip())  #aleX leNb

# 2)移除name变量左边的"al"并输出处理结果
print(name.strip("al")) #eX leNb

# 3)移除name变量右⾯面的"Nb",并输出处理结果
print(name.strip("Nb")) #aleX le

# 4)移除name变量开头的a"与最后的"b",并输出处理结果
print(name.strip("a").strip("b")) #leX leN  #比较好理解
print(name.strip("ab"))  #leX leN  #迭代匹配

# 5)判断 name 变量是否以 "al" 开头,并输出结果
print(name.startswith("al")) #True

# 6)判断name变量是否以"Nb"结尾,并输出结果
print(name.endswith("Nb"))  #True
print('---------1')

# 7)将 name 变量对应的值中的 所有的"l" 替换为 "p",并输出结果
name = "aleX leNb"
print(name.replace("l","p"))  #apeX peNb

# 8)将name变量对应的值中的第⼀个"l"替换成"p",并输出结果
print(name.replace("l","p",1)) #apeX leNb

# 9)将 name 变量对应的值根据 所有的"l" 分割,并输出结果。
print(name.split("l")) #['a', 'eX ', 'eNb']

# 10)将name变量对应的值根据第一个"l"分割,并输出结果。
print(name.split("l",1)) #['a', 'eX leNb']
print("-------2")

# 11)将 name 变量对应的值变大写,并输出结果
print(name.upper()) #ALEX LENB

# 12)将 name 变量对应的值变小写,并输出结果
print(name.lower()) #alex lenb

# 13)将name变量对应的值首字母"a"⼤写,并输出结果
name = "aleX leNb"
# print(name.title()) #Alex Lenb
print(name.capitalize()) #Alex lenb  #只有首单词的首字母大写，后面的字母全部变成小写  （N变成了小写n）

# 14)判断name变量对应的值字母"l"出现几次，并输出结果
print(name.count("l")) #2

# 15)如果判断name变量对应的值前四位"l"出现几次,并输出结果
print(name.count("l",0,4)) #1
print("-------3")

# 16)从name变量对应的值中找到"N"对应的索引(如果找不到则报错)，并输出结果
print(name.index("N")) #7

# 17)从name变量对应的值中找到"N"对应的索引(如果找不到则返回-1)输出结果
print(name.find("N")) #7

# 18)从name变量对应的值中找到"X le"对应的索引,并输出结果
print(name.find("X le")) #3

# 19)请输出 name 变量对应的值的第 2 个字符?
name = "aleX leNb"
print(name[1]) #l

# 20)请输出 name 变量对应的值的前 3 个字符?
print(name[:3]) #ale
print("-------4")

# 21)请输出 name 变量对应的值的后 2 个字符?
print(name[-2:]) #Nb

# 22)请输出 name 变量对应的值中 "e" 所在索引位置?
print(name.find("e")) #2   #find是找出左边第一个出现的e
# 扩展：如何输出name变量对应的值中第二个（所有的e）"e"的索引位置？
print(name.rfind("e")) #6  #rfind是找出右边第一个出现的e（但是无法找到右边倒数第二个e）

#算法
name = "aleX leNb"
count = 0
while count < len(name): #注意：这里用for循环是找不到索引号的,for循环直接拿到的就是字符，而不是索引号
    if name[count] == "e":
        print(count)  #2 6 即是e第一次的索引号是2 第二次出现的索引号是6 可以找到所有e出现的索引号
    count += 1

# for i in name:
#     if i == "e":
#         pass  #问题：for循环无法取到索引号
#         print(name.index("e")) # 2 2

#总结：当一个题目不会做的时候，将题目只字不差的再读1,2遍，就会有思路了--足够耐心，认真审题










