#!/usr/bin/env python
#-*- coding:utf-8 -*-

dic1 = {"金庸":"笑傲江湖","古龙":"小李飞刀"}
print(dic1.keys())  #dict_keys(['金庸', '古龙'])  像列表，但是不是列表，但是可以当做列表来遍历使用
print(type(dic1.keys()))  #<class 'dict_keys'>

print(dic1.values()) #dict_values(['小李飞刀', '笑傲江湖'])
print(dic1.items()) #dict_items([('古龙', '小李飞刀'), ('金庸', '笑傲江湖')])  #列表中的元素是元组

#1 直接遍历字典（可以拿到key和value--dic1[key]就是value）
# 字典本身是一个可迭代对象,可以直接进行for循环
for i in dic1:  #重点1
    print(i,dic1[i])
# 古龙 小李飞刀
# 金庸 笑傲江湖

#2 遍历字典的key
for i in dic1.keys():
    print(i,dic1[i])
# 金庸 笑傲江湖
# 古龙 小李飞刀

#3 遍历字典的values
for i in dic1.values():
    print(i)
# 笑傲江湖
# 小李飞刀

#4 遍历字典的items  key和value组成的元组
for i in dic1.items():
    print(i)  #获取的是key,value组成的元组
    print(i[0])  #获取的是key
    print(i[1])  #获取的是value
# ('古龙', '小李飞刀')  #元组
# ('金庸', '笑傲江湖')
print("-----------0")

#5 遍历字典的items  key和value组成的元组
for i in dic1.items():
    k,v = i
    print(k)  #打印的是key
    print(v)  #打印的是value
print("-----------1")

#6 遍历字典的items  key和value组成的元组  重点2
#适用场景  当需要遍历字典. 在操作中涉及到key和value的时候.
#好处，可以获取到字典的key和value
for k,v in dic1.items():  #（k,v）  #将元组(k,v)直接解包成了k,v
    print(k)  ##打印的是key
    print(v)  ##打印的是value
print("-----------2")

#解包
a=10
b=20
a,b =10,20 #这里的等号右边实际上是一个元组，等效于(10,20)
print(a) #10
print(b) #20

#前面的变量的个数和后面解包的个数一致--元组  个数不一致，就会报错
a,b = (10,20)  ## 解构, 解包   元组
print(a)  # 10
print(b)  # 20

#前面的变量的个数和后面解包的个数一致--列表
a,b = [10,20]  ## 解构, 解包   列表
print(a)  # 10
print(b)  # 20

"""
小结：
遍历字典的2个典型方式
1、直接遍历字典本身
    i就是key  dic1[i]就是value
    for i in dic1():
        print(i)   #i就是key
        print(dic1[i])  #dic1[i]是value
2、遍历dic1.items()
    for k,v in dic1.items()
        print(k)  #k是key
        print(v) #v是value
"""









