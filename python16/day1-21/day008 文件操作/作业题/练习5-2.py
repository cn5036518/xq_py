#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
5，文件t51.txt内容(升级题)

name:apple price:10 amount:3 year:2012
name:tesla price:100000 amount:1 year:2013
.......

通过代码，将其构建成这种数据类型：
[{'name':'apple','price':10,'amount':3},
{'name':'tesla','price':1000000,'amount':1}......]
并计算出总价钱。
'''

f = open('t51.txt',mode='r',encoding='utf-8')
# s5 = f.read()
# print(s5)
li1 = []
for i in f:
    # print(i.strip())
    line = i.strip().split()
    # print(line)  #['name:apple', 'price:10', 'amount:3', 'year:2012']
    dic1 = {}   #注意点：字典必须放在内循环外面，而不能放在内循环里面
    for j in line:
        # print(j)
        # dic1 = {}
        lst = j.split(":")
        # print(lst)  #['name', 'apple']
        dic1[lst[0]] = lst[1]
    print(dic1) #{'year': '2012', 'price': '10', 'name': 'apple', 'amount': '3'}
    li1.append(dic1)
print(li1) #[{'amount': '3', 'name': 'apple', 'year': '2012', 'price': '10'},
             #{'amount': '1', 'name': 'tesla', 'year': '2013', 'price': '100000'}]
f.close()


#计算总价钱


'''
伪代码思路：
1、读取文件的每一行
2、遍历循环文件对象
3、空格拆分每一行，得到键值对
4、冒号拆分每一个键值对，构成字典
5、字典依次追加都空列表
'''











