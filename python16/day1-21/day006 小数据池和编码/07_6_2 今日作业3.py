#!/usr/bin/env python
#-*- coding:utf-8 -*-

# 3. 念数字.  给出一个字典. 在字典中标识出每个数字的发音.
# 包括相关符号. 然后由用户输入一个数字. 让程序读出相对应的发音(不需要语音输出. 单纯的打印即可)

dic1 = {
    "-":"fu",    "0":"ling",    "1":"yi",    "2":"er",    "3":"san",   "4":"si",
                 "5":"wu",      "6":"liu",   "7":"qi",    "8":"ba",    "9":"jiu",
    ".": "dian",
}
#输入-127 输出fu yi er qi

#方法2  这里只支持用户输入一次，就结束了
# s1 = ""
# num = input("请输入你要读的数字:")
# for i in num:
#     s1 = s1 + dic1[i] + " "   #拼接字符串   这里只支持用户输入一次，就结束了
# print(s1)

#方法3  这里支持用户输入多次，直到用户主动输入q退出
# s1 = ""  #这个写在while循环外面，就会每次while循环都累加
while 1:
    s1 = ""  #这个写在while循环里面，就会每次while循环的时候，都清空字符串，
    # 在内循环for的时候，才累加     --关键点
    num = input("请输入你要读的数字,输入q退出:")
    if num.upper() == "Q":
        print("程序退出")
        break
    elif num.isdigit() or num.startswith("-") or "." in num:
        for i in num:
            s1 = s1 + dic1[i] + " "   #拼接字符串的思想，非常重要
        print(s1)
    else:
        print("你输入的内容不合法，请重新输入数字")















