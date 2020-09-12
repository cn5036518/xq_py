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
#方法1   通过print的end  空格来实现
while 1:
    content = input("请输入数字，输入q退出：") #输入的是字符串
    if content.upper() == "Q":
        print("程序退出")
        break  #退出当层循环
    elif content.isdigit() or content.startswith("-") or "." in content:
        #关键点：判断输入的字符串是"-"开头或者从第二位起（切片），都是字符串类型的数字
        #关键点：isdigit（）判断
        for j in content:  #1 遍历循环用户输入的字符串类型的数字（字符串本身是可以迭代的类型）
            print(dic1[j],end=" ")  #2 end不写默认是“\n”换行，这里改成空格  #通过dic1[j]进行取值value
            #这里没有拼接字符串，而是通过print的空格分割实现的--方法1
        print() #换行
    else:#如果输入的不是"-"开头，或者输入的不是数字字符串形式的数字，提示不合法
        print("您的输入不合法，请输入数字")











