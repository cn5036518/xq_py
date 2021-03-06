#!/usr/bin/env python
#-*- coding:utf-8 -*-

# 1，形参的接收顺序。
# 	2，什么是命名空间，什么是全局名称空间，什么是局部名称空间，什么是内置名称空间。
# 	3，什么是全局作用域，什么是局部作用域。
# 	4，名称空间的加载顺序，取值顺序。
# 	5，解释一下什么是global，什么是nonlocal。

''''''
'''
1、形参的接收顺序
    1、位置参数
    2、动态参数 *args 接收多个位置参数，聚合打包成元组
    3、默认值参数
    4、动态参数 **kwargs 接收多个关键字参数，聚合打包成字典

2、命名空间的概念和分类
    命名空间概念
        又叫名称空间
        python解释器开始执行的时候，就会开辟一个空间，每当遇到一个变量，就把变量名和值的对应关系记录下来，
          这个存放变量名字和值关系的内存空间就叫名称空间（也叫'命名空间'）
    命名空间分类
        内置名称空间：python解释器中，list，tuple，dict等都是在内置名称空间中开辟的内存
        全局名称空间：函数外，全局变量，函数（嵌套函数的父级函数）都是在全局名称空间中开辟的内存
        局部名称空间：函数内，局部变量是在局部名称空间中开辟的内存，函数执行完毕后，局部变量的内存空间就回收了
                     嵌套函数中，父级函数的局部名称空间和子级函数的局部名称空间是不同的

3、全局作用域和局部作用域的概念--作用范围
    全局作用域概念：内置名称空间+全局名称空间
    局部作用域概念：局部名称空间

4、名称空间的加载顺序：内置名称空间>全局名称空间>局部名称空间
   名称空间的取值顺序：局部名称空间>全局名称空间>内置名称空间

5、global关键字概念
        函数内，把局部变量升级成全局变量，用于访问和修改
        global a
        a = 10  #函数内，给全局变量a进行了重新赋值，全局变量a发生了修改
   nonlocal关键字概念
        函数内，引用其父级函数的变量，用于访问和修改
        nonlocal b   #把其父级函数的变量b，做了重新赋值，其父级函数的变量b也同步修改了
        b = 20
'''













