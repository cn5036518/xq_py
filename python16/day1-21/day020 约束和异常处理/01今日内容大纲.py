#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/5/5 9:06
#@author:wangtongpei


''''''
'''
一、昨日内容回顾
    1、issubclass type  isinstance
        1、issubclass：判断a是b的子类
        2、type：判断对象是由哪个类产生的
        3、isinstance：判断xxx是否是xxx类型的

    2、函数和方法
        1、类外面都是函数
        2、类里面
            1、静态方法：都是函数（不管是类名调，还是对象调）
            2、类方法：都是方法
            3、普通方法：类名调，就是函数；对象调，就是方法

        通过types中的FunctionType和MethodType来判断是函数还是方法
        用isinstance(xxx,FunctionType)
        用isinstance(xxx,MethodType)
        返回值是true或者false

    3、反射
        hasattr(obj,str):判断py文件或者类中，是否有该字符串命名的函数或者方法、变量
        getattr(obj,str)：如果有，获取该字符串命令的函数或者方法的内存地址，存入变量，变量()就是调用
                通过callable(变量)判断是函数还是变量
                通过isinstance(变量,FunctionType)判断是函数还是变量
        setattr(obj,str,value)：在内存层面，新增（或者修改）变量或者函数（方法）--不建议使用
        delattr(obj,str)：在内存层面，删除变量或者函数（方法）


二、作业讲解
三、今日主要内容
    1、异常处理
        1、处理异常         try  except
        2、抛出异常         raise 异常类(提示语)
        3、自定义异常       继承Exception
        4、获取主动抛出异常的堆栈信息
                            import traceback
                            traceback.format_exc()
    2、约束
        约束的概念：父类对子类进行约束
        方式1：--推荐（简单）
            父类主动抛出异常
                父类中定义一个方法，该方法的方法体是主动抛出异常
                子类继承父类，子类如果没有重写父类的方法，就会抛出异常NotImplementError
            重写的概念：
                父类和子类的方法名相同的时候，子类的方法会覆盖重写父类的方法
                （父类的方法，子类中如果有的话，子类的方法会覆盖重写父类的方法）
            继承的概念：
                父类的方法，子类中如果没有的话，子类会继承父类的方法
        方式2：--主要是java c#的写法
            抽象类和抽象方法
            导包   from abc import ABCMeta,abstractmethod
            抽象方法
                @abstractmethod
                抽象方法不用写方法体，给个pass就可以
            抽象类
                语法
                    类名(metaclass=ABCMeta)
                概念
                    如果类中包含了抽象方法，那么这个类肯定是抽象类
                特点
                    1、抽象类一般不创建对象
                    2、抽象类中可以有普通方法
                作用
                    1、对子类进行约束
                    2、子类必须重新父类的抽象方法，这个就是对子类的约束

            接口
                概念：类中全部是抽象方法，这个抽象类就叫接口

    3、md5加密
        特点：不可逆

    4、日志处理






'''





























