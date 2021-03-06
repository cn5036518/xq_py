#!/usr/bin/env python
#-*- coding:utf-8 -*-

#需求，将日志文件中的每一行 2018-09-11 00:00:01|刘伟|吃鸡
#    存入一个字典，字典依次添加到列表中
# li1 = [{"time":"2018-09-11 00:00:01","name":"刘伟","action":"吃鸡"},
#        {"time":"2018-09-11 00:00:02","name":"jack","action":"打电话"}]
# 一般的日志文件，每一行的每个字段是\t tab空格来隔开

path1 = r".\2018-09-12.log"
li1 = []
with open(path1,mode="r",encoding="utf-8") as f:  #1 打开文件
    for i in f: #2 遍历循环文件对象
        dic1 = {}  #定义字典方法2
        i = i.strip()  #3去掉文件两端的空白
        time1,name2,action3 =i.split("|") #4 通过分隔符"|"进行拆分分割  解包
        # dic1 = {"time":time1,"name":name2,"action":action3}
        # #5 定义字典方法1--每一行的信息存入一个字典   一次性添加（一行）
        dic1["time"] = time1  #单个键值对一个一个添加
        dic1["name"] = name2
        dic1["action"] = action3
        li1.append(dic1) #6 不同的行（字典）依次添加到列表中
print(li1)
# [{'name': '刘伟', 'action': '吃鸡', 'time': '2018-09-11 00:00:01'},
#  {'name': '王玉杰', 'action': '打电话', 'time': '2018-09-11 00:00:02'}]

"""
字典的新建的2种方法：
方法1：一行添加（一次性添加）
dic1 = {"time":time1,"name":name2,"action":action3}

方法2:单个键值对添加
dic1 = {}
dic1["time"] = time1  #单个键值对一个一个添加
dic1["name"] = name2
dic1["action"] = action3

"""












