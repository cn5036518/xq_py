#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2019/12/11 7:23
#@author:wangtongpei
#@email: cn5036520@163.com

''''''
'''
一、昨日内容回顾
成员
1、变量
    1、成员变量--最常见
        1、写法：
            变量前面加了self就是成员变量
            这里的self表示当前对象
            一般是在构造方法中定义
        2、调用：
            对象.成员变量
        3、作用：
            可以在类中的不同方法间使用
            有点局部的意思（每个对象的成员变量可以不同）

    2、类变量（静态变量）
        1、写法
            写在类中，方法外的变量
        2、调用
            类名.类变量
        3、作用
            全局的意思

    注意点：
    1、如果用对象.类变量，就相当于给对象新增了一个和类变量同名的成员变量
       原来的类变量不会有任何变化

2、方法
    1、成员方法--最常见
        1、范围：
            构造方法：
                创建对象的时候，自动调用构造方法
            普通方法
        2、写法：
            1、第一个参数是self，表示当前对象本身
        3、调用
            对象.成员方法
            内部原理：类名.成员方法(对象名)

    2、静态方法
        1、写法
            1、方法上面加上@staticmethod
            2、参数没有self
        2、调用
            类名.静态方法
        3、作用
            把静态方法理解成类中的函数就可以

    3、类方法
        1、写法
            1、类方法名字上面加上@classmethod
            2、第一个参数是cls
        2、调用
            类名.类方法
        3、作用
            用于在类中创建对象，设计模式

3、属性
    1、概念
            通过方法的形式来表示一个属性信息（变量-名称）
    2、引入原因-由来
        1、成员变量或者数据库字段一般不保存人的年龄，而是保存人的生日
        2、因为年龄的话，每年都会变化，生日是不会变化的，易于维护
        3、根据出生日期计算年龄，做成一个成员方法的，但是年龄是一个名词属性
           用方法-动作来计算，稍有点不妥
        4、于是，就引入了属性
    3、写法
        1、成员方法的定义上面加上一行@property
    4、调用
        对象名.属性名--调属性
        对象名.方法名()--调成员方法

4、私有
    1、私有变量
        1、写法
            类中，变量名字前面加上双下划线__
        2、调用
            1、不能用对象进行调用
            2、可以在类中的成员方法中使用
        3、对象如何间接调用私有变量
            1、把私有变量写在类中的成员方法中
            2、对象通过调成员方法，从而间接调用私有变量

    2、私有方法
        1、写法
            类中，成员方法名字前面加上双下划线__
        2、调用
            1、不能用对象进行调用
            2、可以在类中的成员方法中使用
        3、对象如何间接调私有方法
            1、把私有方法的调用，写在类中的成员方法中
            2、对象通过调成员方法，从而间接调用私有方法

    3、注意点：
        1、子类继承父类的时候，无法继承父类的私有变量和私有方法


二、作业讲解
三、今日主要内容
    1、依赖关系
        1、比较轻的关系
            1、如何和陌生人打交道
            2、受陌生人欢迎的程度，决定你的赚钱能力
        2、例子：
            大象装冰箱--大象可以装任何一个冰箱，也可以装高压锅（关系不紧密，可以随时换）
            大象装高压锅--多态
            你打车(你和车之间的关系，你用车，但车不属于你，就是依赖关系-弱关系)
        3、写法
            1、类2的对象作为参数传入到类1的成员方法中
            2、在类1的成员方法中，通过类2的对象调类2的成员方法

    2、关联关系（组合、聚合）
        1、一对一
            1、例子：男女朋友
            2、写法
                1、类2的对象作为参数传入到类1的成员方法中
                2、在类1的成员方法体中，把类2的对象赋值给类1的成员变量
                3、类1的成员变量就可以指代类2的对象了
                4、可以通过类1的成员变量调类2的成员变量，或者类2的成员方法

        2、一对多
            1、例子：学校和老师
            2、写法
                类1-学校类的定义
                1、类1-学校类中定义一个成员变量，赋值空列表
                2、把类2的对象作为参数传入到类1的成员方法1中
                3、在类1的成员方法体中，把类2的对象添加到空列表
                4、在类1的成员方法2中，循环遍历这个列表，列表的每个元素就是类2的对象
                   通过类2的对象调类2的成员变量

                类1的成员方法调用
                1、类1的对象每调用一次成员方法1，就新增加一个老师对象到列表中

    3、继承关系，实现关系
        1、self：当前执行这个方法的对象
        2、子类继承父类
            1、新建的是子类对象，那么self就是子类对象
            2、新建的是父类对象，那么self就是父类对象

    4、类中的特殊成员
        1、重点是：
            __str__()  #打印对象，默认是打印对象的内存地址；
                         重写__str__（）后，打印对象的时候，可以打印对象的成员变量
                         例子：
                            def __str__(self):
                                # return self.name,self.age,self.hobby #报错
                                # TypeError: __str__ returned non-string (type tuple)
                                # 返回值必须是字符串，而不能是元组
                                return '%s %s %s' % (self.name,self.age,self.hobby)

            __new__()  #创建对象的过程
                1、加载类
                      calss 类名 定义类

                2、开辟内存空间
                        __new__(cls)方法，此时内存空间没有对象，需要下一步创建

                3、创建对象
                        通过__new__(cls)的返回值
                        return object.__new__(cls)  来创建对象
                        注意点：这里参数是cls类，而不是self对象，因为此时只有类，对象还没有被创建出来

                4、初始化对象
                        构造方法 __init__()

                5、使用对象
                        对象调成员变量，或者对象调成员方法


        2、常见特殊成员
            1、__init__() 构造方法

            2、__hash__()
                类和对象默认是可哈希的，不可变，可以作为字典的key
                __hash__ = None  #就变成不可哈希，可变的，不能作为字典的key

            3、__getitem__(value)
                对象[key]就是调用__getitem__（value）方法，参数是value
                通过key获取value，类似字典

            4、__setitem__()
                对象[key] = value 就是调用__setitem__（key,value）方法，参数是key,value
                添加键值对，类似字典

            5、__delitem__(key)
                del 对象[key]就是调用__delitem__（key）方法，参数是key
                通过key删除键值对，类似字典

            6、__enter__()
                  return 字符串
            7、__exit__()
            with 对象 as 变量:
                pass
                print(变量)
            过程如下:
                1、先调__enter__()方法进入
                2、其返回值，被with后面的变量接收
                3、再调__exit__()方法退出
            例子：打开文件









'''















