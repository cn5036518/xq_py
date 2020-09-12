#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2019/11/10 7:49
#@author:wangtongpei
#@email: cn5036520@163.com

#1 count() 计数
li1 = ['jack','tom','bob']
print(li1.count('tom'))  #1
#计算元素在列表中出现的个数
print('-------------------1  count')

'''
思路：
1、建立一个空字典
2、遍历循环列表，
   判断，不在字典，就添加进去
   在字典的话，字典的value就自增1
'''

li1 = ['jack','tom','bob']  #算法 字典 qym
dic1 = {}
for i in li1:
    if i not in dic1:
        dic1[i] = 1
    else:
        dic1[i] += 1
print(dic1) #{'jack': 1, 'tom': 1, 'bob': 1}

#2 index()  #计算列表元素的索引号
li1 = ['jack','tom','bob']
print(li1.index('tom'))  #1
print('-------------------2  index')

#3 sort()  排序-列表本身修改了
li3 = ['jack','tom','bob']
li3.sort()
print(li3)  #['bob', 'jack', 'tom']
print('-------------------3  sort 排序')

#4 reverse() 反转(不是倒序)--列表本身修改了
li4 = ['jack','tom','bob']
li4.reverse()
print(li4)  #['bob', 'tom', 'jack']
print('-------------------4  reverse 反转')

# 5 列表在循环遍历的过程中，不能删除元素，因为涉及到元素的移动
# 解决办法：
# 把要删除的元素，添加到新的列表中，循环新列表，删除老列表
li5 = ['jack','tom','bob']
li6 = []
for i in li5:
    li6.append(i)

for i in li6:  #循环新列表，删除老列表--根据索引号连接
    li5.remove(i)
print(li5)  #[]
print(li6)  #['jack', 'tom', 'bob']
print('-------------------5  循环遍历的同时 不能直接删除元素')

#6深浅拷贝和赋值
#01 赋值 =
li1 = ['tom','bob']
li2 = li1  #id相同，说明li1和li2指向的是同一个内存地址（同一个内存空间）
print(id(li1))  #114192399752
print(id(li2))  #114192399752
print('-------------------6-1 赋值 =')

#02 浅拷贝
li1 = ['tom','bob']
#方法1
li2 = li1.copy() #id不同，说明li1和li2指向的不是同一个内存地址
#就是说 li2是从li1复制了一份，新开辟了一个内存空间
print(id(li1)) #761310795016
print(id(li2)) #761338769032
print('-------------------6-2-1 浅拷贝 copy() 第一层')

li11 = ['tom','bob',['jack']]
li12 = li11.copy()
print(id(li11))  #1015758987848
print(id(li12))  #1015758987592
# li11和li12的id不同，说明实现了拷贝，新开辟了一个内存空间

print(id(li11[-1]))  #1015758987720
print(id(li12[-1]))  #1015758987720
# li11[-1]和li12[-1]的id系统，说明列表的第二层没有实现拷贝，第二层还是指向的是同一个内存空间
# 类比：浅拷贝  列表的第一层拷贝就是家庭夫妻财务AA，
#      浅拷贝  列表的第二层拷贝就是家庭夫妻设立的共同账户
print('-------------------6-2-1 浅拷贝 copy() 第2层')

#方法2
li3 = li1[:] #id不同，说明li1和li2指向的不是同一个内存地址
#就是说 li2是从li1复制了一份，新开辟了一个内存空间
print(id(li1)) #1072053998920
print(id(li3)) #1072054648584
print('-------------------6-2-2 浅拷贝 [:] 第一层')

li11 = ['tom','bob',['jack']]
li12 = li11[:]
print(id(li11))  #1015758987848
print(id(li12))  #1015758987592
# li11和li12的id不同，说明实现了拷贝，新开辟了一个内存空间

print(id(li11[-1]))  #1015758987720
print(id(li12[-1]))  #1015758987720
# li11[-1]和li12[-1]的id系统，说明列表的第二层没有实现拷贝，第二层还是指向的是同一个内存空间
# 类比：浅拷贝  列表的第一层拷贝就是家庭夫妻财务AA，
#      浅拷贝  列表的第二层拷贝就是家庭夫妻设立的共同账户
print('-------------------6-2-2 浅拷贝 [:] 第2层')

from copy import deepcopy
#03 深拷贝
li21 = ['tom','bob',['jack']]
li22 = deepcopy(li21)  #注意点：deepcopy需要引包才行
print(id(li21))  #529028216584
print(id(li22))  #529028217352
print(id(li21[-1])) #529028216648
print(id(li22[-1])) #529028358856
#id不同，说明深拷贝的第一层和第二层拷贝了，没有指向同一个内存空间
print('-------------------6-2-3 深拷贝')

#7 列表推导式
li7 = [1,2,3]
#需求：将列表中的奇数，变成其平方数
li8 = [i*i for i in li7 if i%2 == 1 ]
print(li8)  #[1, 9]
print('-------------------7 列表推导式')












