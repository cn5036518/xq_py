#!/usr/bin/env python
#-*- coding:utf-8 -*-

# 2. 电影投票. 程序先给出⼀个⽬前正在上映的电影列表. 由⽤户给每⼀个电影投票. 最终 将该⽤户投票信息公布出来
lst = ['⾦瓶梅', '解救吾先⽣', '美国往事', '⻄⻄⾥的美丽传说']
# 结果: {'⾦瓶梅': 99, '解救吴先⽣': 80, '美国往事': 6, '⻄⻄⾥的美丽传说': 23}

dic1 = {}
for i in lst:
    score = input("请输入电影<%s>评分，输入q退出评分:" % i) #输入的是字符串，需要转换成int
    #注意点  这里需要通过占位符，显示电影名称
    if score.upper()=="Q":
        print("您已经主动退出评分")
        break
    elif score.isdigit() == True: #判断用户输入的字符串是否是数字  "99"
        score = int(score)
        dic1[i] = score #把电影名字和评分，作为键值对，依次推荐到字典中
    else:
        print("您的输入不合法，请重新输入数字")
print(dic1)













