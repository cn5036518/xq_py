#!/usr/bin/env python
#-*- coding:utf-8 -*-

dic1={"name":"jack","age":18}  #字典的定义，字典是无序的（通过key取值），列表是有序的（通过索引号取值）
#字典通过key取值的速度是快于列表通过索引号取值的

#一、增删改查
#1 新增
dic1={"name":"jack","age":18}
dic1["class"]="first"  #往字典添加一个键值对
print(dic1)  #{'name': 'jack', 'age': 18, 'class': 'first'}

#2 删除
#001 删除一个键值对 del（不是字典的内置函数，列表也可以用）
#    删除字典的一个元素
dic1={"name":"jack","age":18}
del dic1["name"]  #删除一个键值对
print(dic1)  #{'age': 18}

#002 清空，删除全部键值对  clear(字典的内置函数，列表的内置函数也有这个)
dic1={"name":"jack","age":18}
dic1.clear()   #清空列表，和析构不同，清空后字典的内存空间并没有释放回收，字典还是存在的
print(dic1)  #{}

#003 删除整个字典，回收内存空间
dic1={"name":"jack","age":18}  #定义字典-构建
# del dic1  # 删除整个字典，回收内存空间，字典已经不存在了--析构
# print(dic1)  #NameError: name 'dic1' is not defined

#3 修改
dic1={"name":"jack","age":18}
dic1["age"]=8   #修改字典中一个键的值
# dic1["age1"]=8  #注意：如果key不小心写错了，是字典之前不存在的key，那么就是新增另外一个键值对到字典中
print(dic1)  #{'age': 8, 'name': 'jack'}

#4 查  取值（根据key取value）
dic1={"name":"jack","age":18}
print(dic1["name"]) #方法1：根据key取value   jack  这个通过key取值和列表的通过索引号取值的写法是相似的
# print(dic1["name1"]) #根据key取value 如果key不存在，就会报错key error
print(dic1.get("name")) #方法2：根据内置方法get取key的值
print(dic1.get("name1","not found"))  #not found   get方法,如果key不存在，就输出参数2-"not found"

"""
二、字典的特点
1、字典的key是不能重复的，key是字典中元素(即键值对)的唯一标识，如果key重复，后面的value会覆盖前面的value
2、字典的key必须是不可变的，只能是字符串，数字，元组，
   字典的key不能是可变的，不能是列表、字典、集合
   字典的value不限，即不可变的，可变的都可
3、字典是无序的，列表是有序的
"""
#1、key不能重复
dic1={"name":"jack","age":18,"age":11}  #这里key都是"age"的时候，以后面的value=11为准
print(dic1) #{'age': 11, 'name': 'jack'}

#2、key必须是不可变
dic1={"name":"jack",18:18,(11,22):555} #这里字典的key "name"是字符串，18是数字，(11,22)是元组 都是不可变的
print(dic1) #{'name': 'jack', 18: 18, (11, 22): 555}

# dic1={"name":"jack",[11,22]:555} #这里字典的key [11,22]是列表，是可变的类型，不可哈希，所以报错
# print(dic1) #TypeError: unhashable type: 'list'

# dic1={"name":"jack",{"city":"beijing"}:555} #这里字典的key {"city":"beijing"}是字典，是可变的类型，不可哈希，所以报错
# print(dic1)  #TypeError: unhashable type: 'dict'

# dic1={"name":"jack",{'apple','orange'}:555} #这里字典的key {'apple','orange'}是集合，是可变的类型，不可哈希，所以报错
# print(dic1)  #TypeError: unhashable type: 'set'

set1={"11","23","23"}  #集合的定义，去重，无序、不可变
print(set1)  #{'23', '11'}

