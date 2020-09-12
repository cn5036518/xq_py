#!/usr/bin/env python
#-*- coding:utf-8 -*-

# 2. 电影投票. 程序先给出⼀个⽬前正在上映的电影列表. 由⽤户给每⼀个电影投票. 最终 将该⽤户投票信息公布出来
lst = ['⾦瓶梅', '解救吾先⽣', '美国往事', '⻄⻄⾥的美丽传说']   #pdf的字体copy可能有问题
# 结果: {'⾦瓶梅': 99, '解救吴先⽣': 80, '美国往事': 6, '⻄⻄⾥的美丽传说': 23}

"""
思路：
1、投票是递增的过程  +=1
"""

# 方法3 get方法2  简洁版
li1 = ["金瓶梅","解救吾先生","美国往事","西西里的魅力传说"]
dic1 = {}
# count =1
while 1:
    content = input("请输入您最喜欢的电影名字，输入q退出投票：")  #输入的是字符串
    if content.upper() == "Q":
        break
    elif content in li1: #1判断是否在列表中，在的话
        if dic1.get(content) == None:  #2判断key在空字典是否有，没有的话
            dic1[content] = 1  #3新建键值对，初始value是1
        else:  #3 如果key在字典中，就需要对value（这里的value除了1-写死的，还可以用dic1[content]表示--活的）自增1
            dic1[content] += 1  #自增1  和空列表的追加类似[].append(新元素)
    else:
        print("您输入的电影还没有上映，请重新输入正在上映的电影")
print(dic1)












