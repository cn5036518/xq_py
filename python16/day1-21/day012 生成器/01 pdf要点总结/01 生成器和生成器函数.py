#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2019/10/7 15:29
#@author:wangtongpei

''''''
'''
1、生成器和生成器函数的概念
    1、生成器的本质是迭代器
    2、函数中包含yield，就是生成器函数

2、生成器函数的写法
    def func():
        a =10
        yield 20
    gen = func()  #没有执行，而是生成一个生成器
    普通函数和生成器函数的不同
    1、普通函数名()表示函数的的执行
    2、生成器函数名()不是函数的执行，而是生成一个生成器

    yield和return的不同
    1、retun表示返回，同时函数执行终止，return之后的代码不会执行
    2、yield也表示返回，函数暂停，函数分段执行

    def func():
        a =10
        yield 20
        b = 30
        yield 40
    gen = func()  #生成一个生成器
    li1 = list(gen) #把生成器中每一个元素取出来，放进列表  #注意点
    gen.__next__() #返回20 执行到第一个yield
    gen.__next__() #返回40 从第一个yeild开始执行到第二个yield

3、如何得到生成器
    1、生成器函数
       生成器函数名()
    2、生成器表达式
    3、类型转换

4、生成器的特点
    1、节省内存
    2、惰性机制（每执行一次__next__（）方法，取值一次）
    3、只能向前取值，不能退后

5、生成器的取值
    __next__()方法和send()方法的区别
       前者表示向下取值
       后者除了表示向下取值，还可以给上一个yield传递值
       注意：send()方法不能用在第一个取值，第一个取值只能用__next__()
            最后一个yield也不能用send()

6、生成器的好处
    节约内存
'''

#关于__next__()方法和send()方法的例子
def func():
    a = 1
    a2 = yield 2
    print(a2)
    c = 3
    c2 = yield 4
    print(c2)
    yield 5
gen = func() #生成一个生成器
gen.__next__()  #执行到了第一个yield
gen.send('test') #把参数传递到第一个yield
gen.send('娃哈哈') #把参数传递到第2个yield

#生成器的好处-节约内存的例子
#一次性买100件衣服，需要地方保存，比较浪费内存
li1 = []
def func2():
    for i in range(1,11):
        li1.append('衣服 %s' % i)
    return li1
ret = func2()
print(ret)  #100件衣服一次性生成出来，放到列表到了
print('----------1')

#最好的方式是下一个100件衣服的订单，但是呢，需要一件，送一件，就不需要专门的地方保存了，节约内存
#方法1 生成器函数
def func3():
    for i in range(1,11):
        yield ('衣服 %s' %i)
gen = func3()  #生成一个生成器
print(gen.__next__()) #第一件
print(gen.__next__()) #第二件
for i in gen: #生成器本质是迭代器，支持for循环
    print(i)

#方法2 生成器表达式
# gen = (i for i in range(1,11))
# print(gen)  #生成一个生成器（类比：就是买衣服订单）
# print(gen.__next__()) #第一件
# print(gen.__next__()) #第二件
# for i in gen: #生成器本质是迭代器，支持for循环
#     print(i)











