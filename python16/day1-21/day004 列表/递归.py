#!/usr/bin/env python
#-*- coding:utf-8 -*-

# lis = [2, 3, "k",  "ab", "adv"]
lis = [2, 3, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]

def forcase1(lis):
    for i in range(len(lis)):  #通过索引来取值
        # print(i,lis[i])
        if type(lis[i]) == list:  #注意 type的小括号 拼写
            forcase1(lis[i]) #是列表，就递归自己掉自己
        else: #关键点 不是列表就修改值
            if lis[i] == 3:
                lis[i] = "100"
# print(lis)
forcase1(lis)
print(lis)

















