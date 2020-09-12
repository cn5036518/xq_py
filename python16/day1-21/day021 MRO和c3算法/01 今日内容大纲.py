#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/6/23 8:33

''''''
'''
一、昨日内容回顾
    1、异常处理
        1、主动抛出异常  raise
        2、异常处理
            try:
                pass
            except:
                pass
            else:   #没有异常的时候，执行这里
                pass
            finally:   #收尾
                pass
        3、自定义异常
            定义一个类，继承Exception，类里面写pass，就是自定义异常类

    2、约束
        1、父类抛出异常
            1、父类的方法中，方法体是raise NotImplementError('提示语')
            2、子类继承父类的时候，如果没有重写父类的方法，就会报错

        2、抽象类和抽象方法
            1、抽象类的概念：包含抽象方法的类是抽象类
               抽象方法的概念：抽象类中，方法名上面是@abstractmethod的方法就是抽象方法
            2、抽象类和抽象方法的写法
                1、导包  from abc import ABCMeta,abstractmethod
                2、父类(metaclass = ABCMeta)
                    @abstractmethod
                    抽象类的名字
            3、抽象类的特点
                1、抽象类不能新建对象
                2、抽象类可以包含普通方法
            4、抽象类约束
                1、子类在继承父类抽象类的时候，必须重写父类的抽象方法
                   如果子类没有重写父类的抽象方法，那么子类也是抽象类，子类也不能新建对象
            5、抽象类和接口的区别
                1、接口的概念：
                    类中的所有方法全部都是抽象方法
                2、抽象类可以包含普通方法
                    接口不能包含普通方法
                3、接口是抽象类的一个特例
                   接口属于抽象类
                   抽象类包含接口
                4、接口是java和c#的概念，py里面没有单独定义接口的概念

    3、md5加密
        1、引入模块
        2、生成md5对象
        3、把要加密的字符串转换成字节，给到md5对象
        4、产生密文

        import hashlib
        md5 = hashlib.md5(b'dhaha')   #小括号内是盐
        md5.update('jack'.encode('utf-8'))
        ciphertext = md5.hexdigest()
        print(ciphertext)

    4、日志处理
        导入模块 logging
        日志格式配置
        basicConfig(filename,
                    format,
                    datefmt,
                    level,
                    )
        日志级别（大写）
            CRITICAL  50
            FATAL     50
            ERROR     40
            WARNING   30
            WARN      30
            INFO      20
            DUBUG     10
            NOTSET     0
            自定义日志级别


二、作业讲解

三、今日主要内容
    super
    作用：可以访问mro列表中下一个类的方法。找父类

    python支持多继承


'''



















