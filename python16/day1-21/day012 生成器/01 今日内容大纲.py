#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2019/10/6 8:55
#@author:wangtongpei

''''''
'''
一、昨日内容回顾
    1、函数名的应用
        1、函数名的命名规则和变量名一样
        2、函数名可以赋值给变量   __name__
        3、函数名可以作为参数
        4、函数名可以作为返回值
        5、函数名可以作为容器（比如：列表）的元素
        6、函数名表示函数的内存地址
        7、函数名()表示函数的执行
        8、函数的注释  __doc__

        2、函数名可以赋值给变量   __name__
            def func():
                print('我是函数')
            a = func
            b = a
            c = b
            print(c)  #打印函数func的内存地址
            print(c.__name__)  #func  可以找到原函数名

        3、函数名可以作为参数
            01代理设计模式
            def panpan():
                print("我是panpan")
            def pingping():
                print('我是瓶瓶')
            def ximen():
                print("我是大官人")

            def wangpo(female,male): #核心业务逻辑，一般不变，不同的场景，传入不同的函数作为参数即可
                female()
                male()

            wangpo(panpan,ximen)

            02
            def func():
                print('我是一个函数')

            def func2(args):  #形参是函数名
                args()

            func2(func)  #实参也是函数名

        4、函数名可以作为返回值
            def outer():
                a = 10
                def inner():
                    print(a)
                return inner  #函数名作为返回值
            ret = outer()  #返回的是inner函数的内存地址
            ret() #inner（） 就是执行inner函数

        5、函数名可以作为容器（比如：列表）的元素--批量执行多个函数
            def func1():
                print('我是函数1')
            def func2():
                print('我是函数2')

            li1 = [func1,func2]
            for i in li1:
                i()  #这里i是函数名

        8、函数的注释  __doc__
           def func(arg1,arg2):
                """
                这里输入函数的功能--这个函数是用来做什么的
                :param args1: 函数形参的含义
                :param args2:
                :return:          函数返回值的含义
                """
                pass
                return
            print(func.__doc__)  #可以打印函数的文档注释

    2、闭包
        1、闭包的概念
            内部函数中，对外部函数的变量的引用（访问、修改、返回），内部函数就是闭包函数（简称-闭包）

        2、闭包的特点
            1、外部函数中的变量常驻内存
            2、外部函数中变量的保护机制

        3、闭包的写法
            def outer():
                a = 10
                def inner():
                    print(a)
                    return a
                return inner
            ret = outer()  #inner函数的内存地址
            ret() #inner()  内部函数的执行

        4、如何判断函数是否是闭包函数？
            print(ret.__closure__)  #输出含有cell，表示是闭包函数--inner函数是
            print（outer.__closure__） #输出是None，表示不是闭包函数--outer函数不是
            注意：__closure__后面不带小括号，表示是属性；带小括号的是方法（类中）或者函数

        5、闭包的应用
            爬虫：好处是，网络访问值进行一次，其余的时候，都是从常驻内存中获取网页内容
            from urllib.request import urlopen
            def outer():
                content = urlopen("https://www.baidu.com").read()
                def inner():  #闭包函数
                    print(content)  #content是被保护，常驻内存的变量
                return inner
            ret = outer()  #返回inner函数的内存地址  这个第一次访问网络，需要加载
            ret()  #inner（）第一次执行inner函数  #这个就不需要再次访问网络了，而是直接从常驻内存的content来获取了
            ret()  #inner（）第二次执行inner函数

    3、迭代器
        1、概念
            1、可迭代类型的（可迭代的）--iterable
            2、迭代器--iterator
            3、迭代--iteration
        2、可迭代类型的（可迭代的）对象有哪些？
            str list tuple dict set open() range（3）
        3、如何判断一个对象或者类（类型）是可迭代类型的（可迭代的）-iterable？
            #方法1
            li1 = [1,2,3]
            print('__iter__' in dir(li1)) #True 说明是可迭代类型的（可迭代的）-iterable
                                           #如果是False，说明不是
            注意dir()函数是列出对象的所有方法或者函数
            #方法2   isinstance（对象，类型）函数
            from collections import Iterable   #注意：首字母必须大写
            from collections import Iterator   #注意：首字母必须大写
            li1 = [1,2,3]
            it1 = li1.__iter__()  #对象调__iter__()方法就是生成迭代器
            print(isinstance(li1,Iterable))  #True #列表是Iterable
            print(isinstance(li1,Iterator))  #False #列表对象不是Iterator

            print(isinstance(it1,Iterable)) #True  #迭代器是Iterable
            print(isinstance(it1,Iterator)) #True  #迭代器是Iterator
        4、迭代器的应用
            for循环是迭代器来实现的--重点掌握
            li1 = [1,2,3]
            for i in li1:
                print(i)

            li1 = [1,2,3]
            it1 = li1.__iter__()  #对象调__iter__()方法生成 迭代器
            while 1：
                try:
                    print(it1.__next__())
                except StopIteration：
                    print（"循环遍历结束了"）
                    break

        5、迭代器的特点
            Iterable对象都含有__iter__()方法
            Iterator都含有__iter__()方法和__next__()方法
            1、节省内存
            2、惰性（每次调一次__next__()方法，就取值一次）
            3、只能向前，不能退后


二、今日主要内容
    1、生成器
        1、概念：生成器的本质是迭代器
        2、产生方式：
            1、生成器函数
            2、生成器表达式
        3、生成器特点：
            1、节省内存
            2、惰性机制（调一次__next__()，就取值一次，不调就不向下取值）
            3、只能向前，不能退后
        4、生成器取值
            1、__next__()方法-单次向下取值
            2、for循环-取出全部值

    2、生成器函数
        1、概念：函数中含有yield，就是生成器函数
                yield有return的返回功能，同时还有暂停的功能
        2、取值的方法：__next__()和send()的区别
            1、前者是向下取值，生成器函数中，取的是yield后面的值
            2、后者除了向下取值，还能向上一次yield传递值
               注意：第一次取值只能是__next__()，而不能是send（）
        3、生成器函数的写法
            def func():
                a = 10
                yield 222
            gen=func() #这里并没有执行生成器函数，而是生成了一个生成器
            li1 = list(gen)把生成器中的每一个数据拿出来组合成一个列表  注意点
            gen.__next__() #取值一次  取值一次后，不能再次取第一个值
            for i in gen:  #生成所有值，取出来
                print(i)

    3、推导式（列表推导式，字典推导式等）
        1、列表推导式：[结果      for循环 if条件]
        2、字典推导式：{key:value for循环 if条件}
        3、集合推导式：{key       for循环 if条件}
        注意：没有元组推导式

    4、生成器表达式（笔试题）
        1、生成器表达式：（结果 for循环 if条件）
        2、惰性机制（类比：弹夹没子弹了，不能将同一个值，生成2次）
           生成器是记录在内存中的一段代码，产生的时候，没有执行

        生成器表达式和列表推导式的区别类比：
        1、买100个鸡蛋，列表推导式：是一次性把100个鸡蛋买回来，需要地方存储
        2、            生成器表达式：是买一只母鸡，需要鸡蛋就给下蛋




'''













