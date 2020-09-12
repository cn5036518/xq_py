#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/6/25 17:30

''''''
'''
一、回顾上周内容
    面向对象：
        1、对象和类的概念
            对象：
                概念：万事万物都是对象。对象是一组特征、动作的组合。
                如何创建对象：通过类来创建
                        写法：类名()
            类:
                概念：类是对象的描述、概括、约束。

        2、对象和类的关系
            对象是个例,具体的事物   （比如：我家的一只猫就是对象）
            类是统称                （比如：猫类就是类）

        3、三大特征
            1、封装
                将数据或者方法封装到类或者对象中

            2、继承
                子类可以继承父类除了私有内容之外的所有内容（包含成员变量和方法），包括抽象方法

            3、多态
                python原生就是多态。同一个对象，不同的形态

        4、成员
            1、变量
                类变量
                    各个实例共同拥有的，一般用类名来调用
                    如果用实例名调用类变量，然后给赋值的话，就相当于给实例添加了一个实例变量，该实例变量的名字和类变量同名

                实例变量
                    属于具体实例特有，实例来调用

            2、方法
                普通方法（实例方法）
                    调用：对象来调用
                    self：表示对象本身

                静态方法
                    写法：@staticmethod
                            静态方法名()   #参数是空
                    调用：一般是类名来调用

                类方法
                    写法 @classmethod
                            类方法名(cls)
                    调用：一般是类名来调用

            3、属性
                概念：用方法的形式来描述属性
                写法：
                @property
                def age(self):
                    return

        5、类和类之间的关系
            1、依赖
                概念：把一个类的对象作为参数传递到另外一个类，在另外一个类的对象调方法的时候
                特点：关系最弱，松耦合
                例子：你坐出租回家，你不需要拥有出租车，只需要支付车费即可
                    可以随时换不同的出租车。--不持有（无所有权，有使用权）

            2、关联  组合 聚合
                概念：把一个类的对象传递到另外一个类的构造方法中
                特点：关系紧密，紧耦合
                例子：你和手机的关系，你拥有手机（所有权）
                缺点：人要是挂了，手机的所有人就没有了

                组合的例子：
                    电脑坏了，电脑的cpu、内存等硬件都可以拆出来卖或者使用
                    电脑和cpu、内存等硬件的关系就是组合
                聚合的例子
                    人要是挂了，他的五官就随之无用了，五官和人的关系就是聚合

                class Phone:
                    def __init__(self,person):
                        self.owner = person   #这里的person就是类Person的一个对象

                class Person:
                    pass


            3、继承、实现
                继承：子类继承父类
                实现：父类是抽象类，子类必须把父类的抽象方法全部实现（重写）了
                      接口：父类里面全部是抽象方法，父类就叫接口
                约束：
                    1、主动抛异常
                        父类的方法
                            raise NotImplementError(提示语)

                    2、抽象类
                        导包
                        from abc import ABCMeta,abstractmethod
                        类名（metaclass = ABCMeta）
                            @abstactmethod
                            抽象方法名

                    抽象类不能创建对象（类比：抽象派的画在实际生活中找不到具体例子）

                MRO  method resolution order(方法解析顺序)
                经典类
                    深度优先
                新式类
                    如果没有菱形继承，就是深度优先遍历
                    如果有菱形继承，就是c3算法  merge  print(类名.__mro__)
                        如果是简单的菱形继承，只有1个菱形，就采用深度优先，最后是这个头
                    步骤：第一步先画图，看有没有菱形继承

                super
                    写法  super().方法()
                    概念：执行mro列表中下一个类的方法（离当前类最近的父类的方法）

        6、反射
            概念：在对象中查找字符串，找到后，加小括号，当方法来调用
            hasattr(obj,str)
            getattr(obj,str)
            setattr(obj,str,value)
            delattr(obj,str)

        7、issubclass  type isinstance
            issubclass   判断子类
            type         精确判断对象是哪个类的对象
            isinstance   判断xxx是否是yyy类型的

        8、判断方法和函数
            FunctionType    判断对象是否是函数
            FunctionMethod  判断队形是否是方法

        9、异常处理
            1、主动抛出异常
                raise Exception(提示语)

            2、处理异常
                try except else finally

            3、堆栈报错信息
                import traceback
                val = trackback.format_exec()
                print(val)

            4、自定义异常
                概念：继承Exception类
                写法：
                class Custom_error(Exception):
                    pass

二、作业
三、今日主要内容
    collections
        deque   #双向队列
    queue stack #栈   heap（堆）
        queue 队列  先进先出  类比：肯德基窗口排队点餐，先到先点餐
        stack 栈    后进先出  类比：坐电梯（最后上电梯的同学，到站后，第一个离开电梯）

    radom
    time
    os sys




'''





















