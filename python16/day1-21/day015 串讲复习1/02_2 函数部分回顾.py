#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2019/11/19 5:59
#@author:wangtongpei
#@email: cn5036520@163.com

''''''
'''
一、函数
1、函数定义
    对功能或者动作的封装
        在类中定义，就是方法
        在类之外定义，就是函数

2、函数写法
    1、定义或者申明函数
        def 函数名(形参列表):
            函数体(return)
    2、调用函数
        函数名(实参)

3、函数名
    1、定义
        是一个变量的名字（函数名也属于变量）

    2、用途
        1、可以进行赋值。
        2、可以作为参数，可以作为返回值。
        3、可以作为集合类的元素。
            集合类是狭义-集合数据类型set？还是广义list、tuple、set？

4、参数
    1、形参
        1、定义
            在函数声明的位置定义的变量

        2、分类
            1、位置参数--最常见
            2、默认值参数
            3、动态参数
                1、 *args   动态接收多个位置参数
                2、**kwargs 动态接收多个关键字参数
                3、* **在形参位置，表示聚合
                   * **在实参位置，表示打散  *列表 **字典   *li1 **dic1

        3、参数顺序
            位置参数 *args 默认值参数 **kwargs

        4、无敌参数
            1、定义
                可以接收任何类型或者数量的参数
            2、写法
                def func(*args,**kwargs):
                   pass

    2、实参
        1、定义
            在函数调用的时候，给函数传递的具体值

        2、分类
            1、位置参数
            2、关键字参数
            3、混合参数

    3、传参
        定义
            把实参赋值（传递）给形参的过程

5、名称空间-命名空间
    分类
        1、内置名称空间  比如：print
        2、全局名称空间
        3、局部名称空间

6、作用域
    分类
        1、全局作用域
            包含：内置名称空间和全局名称空间
        2、局部作用域--函数内

    globals()和locals()函数的区别
        1、前者查看全局作用域中的内容
        2、后者查看当前作用域中的内容

    global和nonlocal关键字的区别
        1、前者在局部引入全局变量，创建全局变量
        2、后者，在局部引用离它最近的上一级变量

7、函数嵌套和闭包
    1、嵌套
        写法：
            def func():
                def inner():
                    pass
                return inner   #返回内层函数的函数名

    2、闭包
        1、概念-定义
            内层函数用到了外层函数的变量

        2、写法
            def func():
                a = 10
                def inner():
                    return a  #内层函数用到了外层函数的变量
                return inner  #返回内层函数的函数名

        3、作用
            1、保护变量不被修改
                原因：内层函数用的的外层函数的变量，这个变量是外层函数内，所以不能直接修改
            2、变量常驻内存
                原因：外层函数定义的变量，内层函数可能会随时用到
                      如果不是常驻内存，一旦内层函数调用就会报错（类似缓存的机制）

二、迭代器
    1、iterable-可迭代对象
        定义：在该对象的方法中包含了__iter__

    2、iterator-迭代器
        定义：访问对象的__iter__()方法，就可以得到该对象的迭代器

    3、特点
        1、节省内存
        2、惰性机制（一步一步next）
        3、只能向前不能退后

    4、用迭代器写for循环的实现过程
        li4 = [3,4]
        it4 = iter(li4)
        while 1:
            try:
                ret4 = next(it4)
                print(ret4)
            except StopIteration as e:
                print('没有值可以取了',e)
                break  #跳出整个循环

三、生成器
    1、概念
        本质是迭代器

    2、创建方式-3种
        1、生成器函数
        2、生成器表达式
        3、类型转换-range

    3、生成器函数
        1、概念
            函数体中包含yield的函数就是生成器函数
        2、写法
            def func():
                yield xxx
            func()  #调用生成器函数，函数没有被执行，而是产生了生成器generator

            例子：
            def func(li):  #1 定义生成器函数
                for i in li:
                    yield i
            li1 = ['jack', 'tom', 'bob']
            gen1 = func(li1)  #把iterable转成生成器
            # print(next(gen1))  #jack  生成器的取值（单次取值） next() __next__()
            for i in gen1:
                print(i)

        3、yield关键字
            1、和return一样 表示返回
            2、yield可以分段执行
        4、生成器的使用
            1、__next__()或者next()
                每次调用上述方法，可以执行到写一个yield
            2、send()
                可以给上一个yield进行传值
        5、yield from
            把iterable-可迭代对象转换成生成器
            def func3(li):
                yield from li #实现把iterable转换成generator
            li1 = [1,2,3]
            gen3 = func3(li1)  #把iterable转换成生成器-generator
            print(gen3)  #<generator object func3 at 0x000000E53FF24CC8>
            for i in gen3:
                print(i)

    4、生成器表达式
        写法：
            生成器表达式格式  (结果 for循环)
        例子：
            gen = (i for i in range(10))

    5、产生生成器genarator的两种方式
        1、生成器函数
            函数体包含yield的函数就是生成器函数
        2、生成器表达式
            (结果 for循环)
            gen = (i for i in range(10))
            注意：
            1、列表推导式 []
            2、字典推导式 {}
            3、生成器表达式 ()
               没有-元组推导式

    6、特点
        1、生成器在内存中记录的是代码，而没有执行
        2、生成器取值
            1、单个取值: next()或者__next__()
            2、循环取值: for循环
        类比：
            生成器：母鸡
            生成器取值：下蛋


'''
















