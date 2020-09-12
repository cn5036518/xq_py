#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""
切片和range的区别
1、切片 s1[start:end:step]
2 range(start,end,step)
相同点：都是取头不取尾
不同点：1分隔符不同
        切片是冒号；作为分隔符
        range是逗号，作为分隔符
        2 切片是中括号--取索引是中括号来取
           range后面是小括号
"""

#如何给for循环添加索引号（类似while的count）  range() 和len()组合即可（可以替代while循环中的count-索引号）
li1 =["jack","tom","bob"]
for i in li1:
    print(i)  #没有索引
print("-------1")

for i in range(len(li1)):  #0-2 限定范围   重点写法1  必须会默写   重点
    print(i,li1[i]) #这里的i就是列表的索引 li1[i]就是列表根据索引号取值  --有索引了

s1 = "abc"
for i in range(len(s1)): #0-2 限定范围
    print(i,s1[i]) #这里的i就是字符串的索引 s1[i]就是字符串根据索引号取值  --有索引
print("-------2")

#索引号和通过索引号取值的典型 场景应用：购物车
tu1 = ("首页","登录","注册","购物","退出")  #菜单组成的元组
for i in range(len(tu1)):
    # print(i,tu1[i]) #显示i索引号（菜单的编号--从0开始） tu1[i]是根据索引号取值
    # print(i+1,tu1[i]) #显示i索引号（菜单的编号--从1开始） tu1[i]是根据索引号取值
    print(i + 1, tu1[i],sep=",",end=" ")
"""
print(value, ..., sep=' ', end='\n'）
1、sep=' '  print后面的多个参数之间，默认的分隔符是空格
    如果sep=","  print后面的多个参数之间的分隔符就是逗号
2、end="\n" 每打印一行，默认都会换行
    如果end=" "  把\n换行 改成" "空格后，每打印一行，就不会换行，而是空格隔开
"""

#print小结
li1 =["jack","tom","bob"]
for i in li1:
    print(i,sep=",",end=" ")
    #这里的end参数默认是\n换行，改成空格后，就不换行
    #这里的sep分割符逗号，是用来分割两个参数的，如果只有一个参数i，sep就忽略
        #比如分割索引号和索引号对应的值，sep就派上了用场

#collections 中Counter小结
li1 =["jack","tom","tom","bob"]
from collections import Counter
print(Counter(li1))  #Counter({'tom': 2, 'jack': 1, 'bob': 1})
print(type(Counter(li1))) #<class 'collections.Counter'>
print(dict(Counter(li1))) #{'bob': 1, 'jack': 1, 'tom': 2}
print("-------3")

tu = ("首页", "登录", "注册", "购物", "退出")
for i in range(len(tu)):
    print(i,tu[i])











