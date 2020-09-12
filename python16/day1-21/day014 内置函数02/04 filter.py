#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2019/11/2 9:32
#@author:wangtongpei

#1筛选出列表中大于3的元素
li1 = [1,2,3,4,5]
def func(x):
    if x>3:  #x>3是判断条件
        return x

def func1(x):  #和上面的函数等效
    return x>3  #x>3是返回值

li2 = filter(func,li1)  #参数1是自定义函数名 参数2是iterable
print(li2) #<filter object at 0x000000E2FB4DB4C8>  迭代器
print('__iter__' in dir(li2))  #True 说明是迭代器Iterator
print(list(li2))  #[4, 5]  将迭代器转换成列表（迭代器支持for循环）  对于迭代器，都可以通过list(迭代器)来取值
print('-----------------1 filter 普通函数')

li1 = [1,2,3,4,5]
li2 = filter(lambda x:x>3,li1)  #x是参数 x>3是返回值（也可以是判断条件）
print(li2) #<filter object at 0x000000E2FB4DB4C8>  迭代器
print(list(li2))  #[4, 5]
print('-----------------2 filter 匿名函数')

'''
filter函数的运行过程：--概念
1、把参数2-iterable中的每一个元素，依次作为参数传递到自定义函数中，将函数返回值保留
'''

#2筛选出列表中大于3且是偶数的元素
li3 = [1,2,3,4,5]
def func(x):
    if x>3 and x%2 ==0:  #x>3和x%2==0是判断条件  ==优先级高于and
        return x

def func1(x):  #和上面的函数等效
    return x>3 and x%2 ==0  #x>3 and x%2==0是返回值

# li4 = filter(func,li3)
li4 = filter(func1,li3)
print(li4)
print(list(li4))  #[4]
print('-----------------3 filter 普通函数2')

li3 = [1,2,3,4,5]
li4 = filter(lambda x:x>3 and x%2 ==0,li3)  #x>3 and x%2 ==0 两个条件可以作为自定义函数的返回值
print(li4)
print(list(li4))  #[4]
print('-----------------4 filter 匿名函数2')

#3筛选出列表中大于3且是偶数的元素，且将列表中筛选后的元素进行排序
li5 = [1,2,3,4,5,9,8,7,6]
f1 = filter(lambda x:x>3 and x%2 ==0,li5)  #x>3 and x%2 ==0 两个条件可以作为自定义函数的返回值
li6 = sorted(f1)
print(li6)  #[4, 6, 8]
print('-----------------5 filter函数 sorted函数 匿名函数2')

#练习1 筛选出年龄大于20岁的学生
li21 =[{'name':'jack','age':29},{'name':'tom','age':19}]
def func21(dic):
    return dic['age'] > 20

f1 = filter(func21,li21)  #参数1是自定义函数名，参数2是iterable（和sorted的参数位置不同）
li22 = list(f1)
print(li22)  #[{'name': 'jack', 'age': 29}]
print('-----------------6 filter函数  普通函数')

li23 =[{'name':'jack','age':29},{'name':'tom','age':19}]
f1 = filter(lambda dic:dic['age'] >20,li23)
li24 = list(f1)
print(li24)  #[{'name': 'jack', 'age': 29}]
print('-----------------7 filter函数  匿名函数')

#练习2 筛选出年龄大于20岁的学生，并且按照年龄进行升序排列
li31 =[{'name':'jack','age':29},{'name':'tom','age':19},{'name':'bob','age':23}]
def func31(dic):
    return dic['age'] > 20

f2 = filter(func31,li31)  #参数1是自定义函数名，参数2是iterable（和sorted的参数位置不同）
li32 = list(f2)
print(li32)  #[{'name': 'jack', 'age': 29}, {'name': 'bob', 'age': 23}]  筛选完成（筛选出大于20岁的）

def func32(dic2):
    return dic2['age']

li33 = sorted(li32,key=func32)  #按照年龄排序
print(li33)  #[{'name': 'bob', 'age': 23}, {'name': 'jack', 'age': 29}]
print('-----------------8 filter函数+sorted函数  普通函数')

li31 =[{'name':'jack','age':29},{'name':'tom','age':19},{'name':'bob','age':23}]

f2 = filter(lambda dic:dic['age']>20,li31)  #参数1是自定义函数名，参数2是iterable（和sorted的参数位置不同）
li32 = list(f2)  #迭代器转换成列表-iterable
print(li32)  #[{'name': 'jack', 'age': 29}, {'name': 'bob', 'age': 23}]  筛选完成（筛选出大于20岁的）

li33 = sorted(li32,key=lambda dic:dic['age'])  #按照年龄排序
print(li33)  #[{'name': 'bob', 'age': 23}, {'name': 'jack', 'age': 29}]
print('-----------------9 filter函数+sorted函数  匿名函数')

'''
sorted和filter的区别
1、作用
    前者用于排序，后者用于筛选
2、写法
    前者 sorted（iterable,key=func(自定义函数名字或者匿名函数),reverse=False）
        返回的是iterable
   后者 filter(func(自定义函数名字或者匿名函数),iterable)
        返回的是iterator（迭代器）  通过list(迭代器)转换成列表（iterable）
3、运行原理--概念
    前者 将iterable中的每一个元素，作为参数依次传递到key后面的函数中，根据函数的返回值，
         对新产生的iterable的元素进行排序
    后者 将iterable中的每一个元素，作为参数依次传递到参数1-自定义函数中，
         将函数的返回值保留 （自定义函数完成对参数的条件判断-筛选）
4、应用
    对下面的学生信息进行排序和筛选
    li1 =[{'name':'jack','age':29},{'name':'tom','age':19}]
    sorted（）函数可以按照年龄进行排序
    filter() 函数可以把年龄大于20的学生筛选出来
             可以支持先筛选，后排序
'''


