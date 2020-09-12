#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2019/11/2 11:03
#@author:wangtongpei

#需求，将列表中的元素都取其平方值
li1 =[1,2,3]

#方法1 列表推导式
li2 = [i**2 for i in li1]  #[返回值 遍历循环]
print(li2)  #[1, 4, 9]
print('-----------------1 列表推导式')

#方法2 map（）函数
m1 = map(lambda x:x**2,li1)
print(m1)  #<map object at 0x00000078981CA5C8>
print('__iter__' in dir(m1)) #True  迭代器
print(list(m1)) #[1, 4, 9]  将迭代器转换成列表-iterable
print('-----------------2 map()函数')

#练习1将下面学生的年龄都加一岁
li1 = [{'name': 'jack', 'age': 29}, {'name': 'tom', 'age': 19}]
m2 = map(lambda dic:dic['age']+1,li1)
print(list(m2))  #[30, 20]
print('-----------------3 map()函数 批量修改')

#练习2 将下面学生信息，先按照年龄筛选出大于20岁的，然后按照年龄升序排列，最后把年龄都加一岁
li2 =[{'name':'jack','age':29},{'name':'tom','age':19},{'name':'bob','age':23}]

#1筛选 大于20
f1 =filter(lambda dic:dic['age']>20,li2)
li3 =list(f1)
print(li3)  #[{'name': 'jack', 'age': 29}, {'name': 'bob', 'age': 23}]

#2排序
li4 = sorted(li3,key=lambda dic:dic['age'],reverse=False)
print(li4) #[{'name': 'bob', 'age': 23}, {'name': 'jack', 'age': 29}]

#3批量修改
def func(dic1):
    dic1['age'] +=1
    return dic1

# m1 =map(lambda dic:dic['age']+1,li4)  #[24, 30]
#这里因为dic1字典本身修改了（年龄都加1岁，批量修改），这里不适合用匿名函数，适合用自定义函数  #注意点
m1 =map(func,li4)
li5 = list(m1)
print(li5)  #[{'name': 'bob', 'age': 24}, {'name': 'jack', 'age': 30}]

# 练习3 计算两个列表相同位置的数据的和
li1 = [1, 2, 3, 4, 5]
li2 = [2, 4, 6, 8, 10]
m1 =map(lambda x,y:x+y,li1,li2)#这里参数2和参数3都是iterable
li3 =list(m1)
print(li3)  #[3, 6, 9, 12, 15]

'''
filter函数和map函数的区别
1、作用
    前者用于筛选，后者用于返回值（不是特定的筛选）
2、写法一样
    前者 filter(func(自定义函数名字或者匿名函数),iterable)
        返回的是iterator（迭代器）  通过list(迭代器)转换成列表（iterable）
    前者 map(func(自定义函数名字或者匿名函数),iterable)
        返回的是iterator（迭代器）  通过list(迭代器)转换成列表（iterable）
3、运行原理--概念
    前者 将iterable中的每一个元素，作为参数依次传递到参数1-自定义函数中，
         将函数的返回值保留 （自定义函数完成对参数的条件判断-筛选）
    后者 将iterable中的每一个元素，作为参数依次传递到参数1-自定义函数中，
         将函数的返回值保留 （自定义函数完成对参数的计算--并非特定的条件判断）
4、应用
     对下面的学生信息进行筛选和修改信息
    li1 =[{'name':'jack','age':29},{'name':'tom','age':19}]
    filter() 函数可以把年龄大于20的学生筛选出来
    map()函数可以把年龄都加1岁

sorted函数、filter函数和map函数的区别
1、作用
    前者用于排序，
    中者用于筛选，
    后者用于返回值（不是特定的筛选或者排序）

1-2、返回值--关键点
    filter最终返回的是普通函数（或者匿名函数）的参数（符合条件）组成的的迭代器（可转成列表）
        --filter对参数做了if条件筛选
            可以return参数
            也可以return筛选条件（if后的）
    map最后返回的是普通函数（或者匿名函数）的返回值组成的迭代器（可转成列表）
        --map对参数没有做if条件筛选，而是做了批量修改或者2个列表的同位置运算等

2、写法
    前者 sorted（iterable,key=自定义函数名字或者匿名函数，reverse=False）
        返回的是iterable
    中者 filter(func(自定义函数名字或者匿名函数),iterable)
        返回的是iterator（迭代器）  通过list(迭代器)转换成列表（iterable）
    前者 map(func(自定义函数名字或者匿名函数),iterable)
        返回的是iterator（迭代器）  通过list(迭代器)转换成列表（iterable）
3、运行原理--概念
    前者 将iterable中的每一个元素，作为参数依次传递到key后面的自定义函数中（或者匿名函数中）
         依据函数的返回值-数字int，作为排序的依据
    中者 将iterable中的每一个元素，作为参数依次传递到参数1-自定义函数中，
         将函数的返回值-True或者False，True的保留 （自定义函数完成对参数的条件判断-筛选）
    后者 将iterable中的每一个元素，作为参数依次传递到参数1-自定义函数中，
         将函数的返回值保留 （自定义函数完成对参数的计算--并非特定的条件判断或者排序）
4、应用
     对下面的学生信息进行筛选和修改信息
    li1 =[{'name':'jack','age':29},{'name':'tom','age':19}]
    sorted() 函数可以依据年龄进行升序排列
    filter() 函数可以把年龄大于20的学生筛选出来
    map()函数可以把年龄都加1岁
5、适用场景
    1、map()函数适合比较复杂的操作，此时，参数1是自定义函数，而不是匿名函数
        将参数2-iterable中的每个元素，依次传递到自动化函数中进行操作
    2、列表推导式适合比较简单的操作，一行搞定
    3、匿名函数也适合比较简单的操作
6、例子
    #练习 将下面学生信息，先按照年龄筛选出大于20岁的，然后按照年龄升序排列，最后把年龄都加一岁
    li2 =[{'name':'jack','age':29},{'name':'tom','age':19},{'name':'bob','age':23}]

    #1筛选 大于20
    f1 =filter(lambda dic:dic['age']>20,li2)
    li3 =list(f1)
    print(li3)  #[{'name': 'jack', 'age': 29}, {'name': 'bob', 'age': 23}]

    #2排序
    li4 = sorted(li3,key=lambda dic:dic['age'],reverse=False)
    print(li4) #[{'name': 'bob', 'age': 23}, {'name': 'jack', 'age': 29}]

    #3批量修改
    def func(dic1):
        dic1['age'] +=1
        return dic1 #返回字典本身

    # m1 =map(lambda dic:dic['age']+1,li4)  #[24, 30]
    #这里因为dic1字典本身修改了（年龄都加1岁，批量修改），这里不适合用匿名函数，适合用自定义函数  #注意点
    m1 =map(func,li4)
    li5 = list(m1)
    print(li5)  #[{'name': 'bob', 'age': 24}, {'name': 'jack', 'age': 30}]
'''











