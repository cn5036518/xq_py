#!/usr/bin/env python
#-*- coding:utf-8 -*-

#课上练习1
dic1={"name":"jack","age":18,"class":"first"}
# 分别实现一次性输出dic1中的所有keys和所有的values

print(dic1.keys()) #dict_keys(['class', 'name', 'age'])
#  注意这个dict_keys不是列表，无法通过索引号取值，但是可以for循环遍历
print(dic1.values()) #dict_values(['first', 'jack', 18])
print(type(dic1.values()))  #<class 'dict_values'>  类型

a=dic1.keys()
print(a)  #dict_keys(['age', 'name', 'class'])
# print(a[0]) #TypeError: 'dict_keys' object does not support indexing
c=list(a)  #将类dict_keys转换成列表（列表这个类型也是类）
print(c) #['name', 'age', 'class']
for i in a:  #可以循环遍历所有的key
    print(i)

b=dic1.values()
for j in b: #循环遍历所有的value
    print(j)
print("=====================")

# 课上练习2 下面代码输出什么？
counter=1
def do_sf():
    # global counter  #将局部变量counter升级成了全局变量
    counter=1 #局部变量
    for i in (1,2,3):
        counter+=1
    print("函数内局部变量counter：", counter)

    #调用函数
do_sf()
print("函数外全局变量counter：",counter) #1 循环外
print("=====================")

counter=1
def do_sf():
    global counter  #将局部变量counter升级成了全局变量，所以counter的初始值是1
    # counter=1 #局部变量
    for i in (1,2,3):
        counter+=1
    print("函数内局部变量counter：", counter)  #4

    #调用函数
do_sf()
print("函数外全局变量counter：",counter) #4 循环外
print("=====================")
"""
思考过程：
这里函数内局部变量counter是4，函数外全局变量counter是1,如果没有函数内的global，那么打印函数外变量就是1
但是这里的glabal将局部变量counter=4升级成了全局变量，这一全局变量4就覆盖了全职变量的初始值1，最后打印函数外变量是4
"""

counter=1
for i in (1, 2, 3):
    counter += 1
print(counter)  #4 循环3次，每次counter加1，最后循环外print一次，输出4

for i in (1, 2, 3):
    i += 1
    # print(i) #2 3 4  #循环内输出
print(i) #4  循环外输出













