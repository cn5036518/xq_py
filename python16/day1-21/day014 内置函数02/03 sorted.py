#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2019/11/2 8:19
#@author:wangtongpei

li1 = ['jack','tom','bob','james']
li12 = ['张三','李四','欧阳锋','天天向上']
li2 = [1,3,2]

li3 = sorted(li1)  #字母顺序
print(li3)  #['bob', 'jack', 'james', 'tom']

li4 = sorted(li2)
print(li4)  #[1, 2, 3]

li5 = sorted(li12)
print(li5)  #['天天向上', '张三', '李四', '欧阳锋']
#按照utf-8的字符编码顺序排列
print(ord('天'))  #22825
print(ord('张')) #24352
print(ord('李')) #26446
print(ord('欧')) #27431
print('------------------------1')

li6 = sorted(li2,reverse=True)
print(li6)  #[3, 2, 1]   倒序  reverse不写默认是False-升序

def func(x):
    return len(x)

# li7 = sorted(li2,key=func)
# print(li7)  #报错 TypeError: object of type 'int' has no len()
# #int是没有长度的

li8 = sorted(li1,key=func)  #key后面是函数名字，按照元素的长度来排序
#过程是，把列表（参数1）中的每一个元素，依次传递给函数func，然后根据func函数的返回值，对新产生的列表进行排序
print(li8)  #['tom', 'bob', 'jack', 'james']
print('------------------------2 sorted（）+key 普通函数')

a = lambda x:len(x)
li9 = sorted(li1,key=a)
print(li9)  #['tom', 'bob', 'jack', 'james']
print('------------------------3 sorted（）+key 匿名函数')

li10 = sorted(li1,key=lambda x:len(x))
print(li10)  #['tom', 'bob', 'jack', 'james']
print('------------------------4 sorted（）+key 匿名函数2')

li11 = sorted(li1,key=lambda x:len(x)%2)
#按照元素除以2的余数，进行排序，余数都是1的话，就保持原来的顺序
print(li11)  #['jack', 'tom', 'bob', 'james']
print('------------------------5 sorted（）+key 匿名函数3')

'''
sorted()和sort()的区别
1 sorted（）的参数1是iterable
    sorted对iterable本身没有修改，而是新创建了一个新的iterable
2 sort()是列表的内置函数  li1.sort()
    sort()对列表本身做了修改
'''

#练习1 按照年龄对学生的信息进行排序
li21 =[{'name':'jack','age':29},{'name':'tom','age':19}]
def func2(dic): #这里的参数dic是列表的元素
    return dic['age']

li22 = sorted(li21,key=func2)
#key的机制是：把iterable-比如列表（参数1）中的每一个元素依次传入函数后，将返回值，作为排序的依据
print(li22) #[{'name': 'tom', 'age': 19}, {'name': 'jack', 'age': 29}]

li23 = sorted(li21,key=lambda dic:dic['age'])
print(li23) #[{'name': 'tom', 'age': 19}, {'name': 'jack', 'age': 29}]
print('------------------------6-1 练习1')

#练习2 按照名字的长度对学生的信息进行排序
li21 =[{'name':'jack','age':29},{'name':'bob','age':19}] #列表嵌套字典，字典是列表的元素
li24 = sorted(li21,key=lambda dic:len(dic['name']))
print(li24)  #[{'name': 'bob', 'age': 19}, {'name': 'jack', 'age': 29}]
print('------------------------6-2 练习2')

#练习3 按照名字的首字母（ascii）对学生的信息进行排序
#注意：ascii码就是按照字母顺序-升序
li21 =[{'name':'jack','age':29},{'name':'bob','age':19},{'name':'tom','age':19}]
# li25 = sorted(li21,key=lambda dic:ord(dic['name'][0]))  #可以对中文的unicode编码排序
# li25 = sorted(li21,key=lambda dic:ascii(dic['name'][0]))
li25 = sorted(li21,key=lambda dic:dic['name'][0])  #和上面的2行等效
#将姓名的首字母转成ascii后，然后进行排序
print(li25)
#[{'name': 'bob', 'age': 19}, {'name': 'jack', 'age': 29}, {'name': 'tom', 'age': 19}]
print('------------------------6-3 练习3')

'''
sorted函数的key的执行过程：
1、把参数-iterable中的每一个元素，作为参数传到自定义函数（或者你们函数中），得到返回值，
   然后根据这个返回值进行排序。

扩展：
1、如何按照中文姓名的姓的拼音的首字母进行排序--应用：手机通讯录
#比较复杂一点，方法还是
li25 = sorted(li21,key=lambda dic:ord(dic['name'][0]))

'''





















