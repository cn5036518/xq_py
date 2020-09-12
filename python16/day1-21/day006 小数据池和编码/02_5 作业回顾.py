#!/usr/bin/env python
#-*- coding:utf-8 -*-

# 6、输出商品列表，用户输入序号，显示用户选中的商品(升级题)
#
# 商品列表：
goods = [{"name": "电脑", "price": 1999}, {"name": "鼠标", "price": 10},
 {"name": "游艇", "price": 20}, {"name": "美女", "price": 998}, ]
#
# 要求:
# 1：页面显示 序号 + 商品名称 + 商品价格，如：
#       		1 电脑 1999
# 	   		2 鼠标 10
for i in range(len(goods)):#取索引号 必须用到range(len(列表))
    print(i+1,goods[i]["name"],goods[i]["price"])  #根据不同索引号，依次取值

#      		…
# 2：用户输入选择的商品序号，然后打印商品名称及商品价格
while 1: #不限定次数，限定输入次数用for range
    num = input("请输入商品编号：")  #商品编号-1就是索引号 输入的是字符串
    if num.upper() == "Q":
        break  #退出当层循环
    elif num.isdigit() == True:  #1判断用户输入的字符串是否是字符串类型的数字，比如："1"  #关键点
        num = int(num)  #字符串转换成int  #注意拼写：这里是int，而不是input
        if num > 0 and num <= len(goods): #2判断用户输入的数字是否在1-4范围内
            print(goods[num-1]["name"],goods[num-1]["price"]) #3 商品编号-1就是索引号，通过索引号取值
        else:
            print("你输入的商品编号不存在，请重新输入")
    else:  #1如果用户输入的字符串不是字符串类型的数字
        print("你输入的不合法，请输入数字")

# 3：如果用户输入的商品序号有误，则提示输入有误，并重新输入。
# 4：用户输入Q或者q，退出程序。













