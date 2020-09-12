#!/usr/bin/env python
#-*- coding:utf-8 -*-

# 3.念数字.  给出一个字典. 在字典中标识出每个数字的发音. 包括相关符号.
# 然后由用户输入一个数字. 让程序读出相对应的发音(不需要语音输出. 单纯的打印即可)
dic = {
    "-": "fu",
    "1": "yi",
    "2": "er",
    "3": "san",
    "4": "si",
    "5": "wu",
    "6": "liu",
    "7": "qi",
    "8": "ba",
    "9": "jiu",
    "0": "ling",
    ".": "dian"
}
#需求:输入-127 输出fu yi er qi
#方法1   通过字典取值，print的end从换行改成空格
# num = input("请输入数字:")
# for i in num:
#     print(dic[i],end=" ")   #注意：dic[i] 而不是dic(1)  拼写

#方法2  通过累计拼接字符串   --累计拼接思想重要，要掌握  关键点
# num = input("请输入数字:")
# s1 = ""  #空字符串
# for i in num:
#     if i in dic: #判断输入的字符串中的每个字符是否在字典中
#         s1 = s1+dic[i]+" "  #初始字符串是空字符串，累计拼接字符串  #关键点
#     else: #如果输入非法字符，就要提示
#         print("您的输入存在不合法的字符 %s" % i)
# print(s1)

#方法3  用户多次输入   --累计拼接思想重要，要掌握  关键点
while 1: #不限定输入次数
    num = input("请输入数字，输入q退出:")
    if num.upper() == "Q":   #1主动退出
        print("主动退出")
        break
    elif num.isdigit() or num.startswith("-") or "." in num: #2 输入的是数字或者小数点，或者是-开头
        s1 = ""  # 空字符串  #每次都需要清空，就写在for外面  #注意点
        for i in num:
            # if i in dic: #判断输入的字符串中的每个字符是否在字典中
            s1 = s1+dic[i]+" "  #初始字符串是空字符串，累计拼接字符串  #关键点
            """
             拼接过程分析：  假设用户输入-1.2  #关键点
            s1第一次取值是  fu
            s1第二次取值是  fu yi
            s1第三次取值是  fu yi dian
            s1第四次取值是  fu yi dian er
            """
        print(s1)
    else: #3如果输入非法字符，就要提示
        print("您的输入存在不合法的字符 <%s>,请重新输入数字" % num)















