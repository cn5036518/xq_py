#!/usr/bin/env python
#-*- coding:utf-8 -*-

#需求，将日志文件中的每一行 2018-09-11 00:00:01|刘伟|吃鸡   #日志处理非常重要，必须重点掌握
#    存入一个字典，字典依次添加到列表中
# li1 = [{"time":"2018-09-11 00:00:01","name":"刘伟","action":"吃鸡"},
#        {"time":"2018-09-11 00:00:02","name":"jack","action":"打电话"}]
# 一般的日志文件，每一行的每个字段是\t tab空格来隔开

path1 = r".\2018-09-12.log"
li1 = []
with open(path1,mode="r",encoding="utf-8") as f:  #1 打开文件
    row1 = f.readline()  # 注意点：先读取一行，就是时间|名字|action  表头
    # 返回的是字符串
    row1 = row1.strip()  #去掉两端的空白，包好换行\n等
    # print(row1)  #时间|名字|action
    time, name, action = row1.split("|")  # 字符串拆分后，返回列表，对列表进行解包
    # 表头的字段 作为字典的key

    for i in f: #2 遍历循环文件对象
        # dic1 = {}  #定义字典方法2
        i = i.strip()  #3去掉文件两端的空白
        time1,name2,action3 =i.split("|") #4 通过分隔符"|"进行拆分分割  解包
        dic1 = {time:time1,name:name2,action:action3}  #一行来构造字典
        # #5 定义字典方法1--每一行的信息存入一个字典   一次性添加（一行）
        # dic1["time"] = time1  #单个键值对一个一个添加
        # dic1["name"] = name2
        # dic1["action"] = action3
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

处理日志文件的总结：
思路：
1、打开文件
2、遍历循环文件
3、拆分每一行，split
4、将拆分后的列表解包，添加到字典中
   （一行添加）  dic1 = {"time":time1,"name":name2,"action":action3}
    （多个键值对，一个一个添加）
    dic1 = {}
    dic1["time"] = time1  #单个键值对一个一个添加
        dic1["name"] = name2
        dic1["action"] = action3
5、把每个字典整体作为元素，依次添加到列表中
6、列表中嵌套字典，每个字典中存一行数据信息

优化：
1、如何处理日志文件的第一行  时间|名字|action  类似表头的情况？--nok
解决办法：
1在循环遍历文件之前，先读取一行--readline，  注意：去掉两端的空白，包括换行\n等
2拆分字符串-split，得到每个字段--列表解包的方式
3每个字段分别作为字典的key
"""












