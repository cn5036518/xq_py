#!/usr/bin/env python
#-*- coding:utf-8 -*-

# 1，老男孩好声⾳选秀⼤赛评委在打分的时候呢,
# 可以进⾏输入. 假设, 老男孩有10个评委. 让10个评委进⾏打分, 要求, 分数必须⼤于5分, ⼩于10分.
# import random
# score = random.randrange(6,10)  #6-9
# print(score)

for i in range(10): #0-9 限定输入10次  #10个评委输入10次
    content = input("请输入分数，只能是5-9分中选择：")
    if content.upper() == "Q":
        break
    elif content.isdigit() == True:
        content = int(content)
        if content>5 and content<10:
            print("您输入的分数在合适范围内")
        else:
            print("您输入的分数不在合适范围内，请输入5-9分")
    else:
        print("你输入的分数不合法，请输入数字")























