#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2019/12/15 17:31
#@author:wangtongpei
#@email: cn5036520@163.com

''''''
'''
特殊成员
1、写法
   双下划线开头，双下划线结尾的方法
2、作用
    特殊场景下，会自动执行
3、例子
    __init__()

一、构造方法
   1、创建对象的时候，会自动执行构造方法 __init__()

二、__call__()方法
    1、用法
        新建对象()，就会自动调用__call__()方法
    2、对象后面加小括号  对象()是python特有的

三、__getitem__()方法
    1、用法
        对象名[key],就会自动调用__getitem__(key)方法
        参数就是key
    2、类似字典，可以从对象中获取key

四、__setitem__()方法
    1、用法
        对象名[key]=value,就会自动调用__setitem__(key,value)方法
        参数是key,value
    2、类似字典，相当于给对象添加一个键值对

五、__delitem__()方法
    1、用法
        del 对象名[key],就会自动调用__delitem__(key)方法
        参数是key
    2、类似字典，相当于给对象删除一个键值对

六、__enter__()方法
        return var1
    __exit__()方法
    with 对象 as 变量:
        print var1   #这里的var1是__enter__方法的返回值
    1、说明：
        with的执行过程
        1、先执行__enter__方法
        2、再执行with中的代码块
        3、最后执行__exit__方法

七、__hash__()方法
    1、类名和对象名默认都是可哈希的，不可变的，可以作为字典的key
       原因是：万事万物都是对象，类名是object的子类
              object这个类中有__hash__（）方法
              这个方法的存在，就表示可以哈希
    2、__hash__ = None
       在类中加上上面一行，类名就不可哈希，可变的，不能作为字典的key
       注意点:这里是 =赋值 而不是==值的判断

八、__str__() 方法
    1、__str__() 方法是Boy的父类object的方法，如果子类不重写的话
       打印对象，就是打印对象的内存地址
    2、子类重写__str__() 方法后
        再次打印对象，就可以不输出对象的内存地址，而是自定义输出了
    3、注意点：
        __str__() 方法的返回值的类型必须是字符串，而不能是元组，否则会报错

九、__new__(cls)方法
    创建对象的步骤
    1、加载类
    2、开辟内存空间：通过__new__(cls)方法
    3、创建对象：    通过__new__(cls)方法的返回值
                     object.__new__(cls)来创建对象
                     注意点：__new__（）的参数是cls类，而不是对象（因为现在对象还没有创建出来）
    4、初始化对象：
                    创建对象的过程中，自动调构造方法__init__()，初始化对象
                    把成员变量封装到对象中，就是初始化对象
    5、使用对象：
                    1、打印对象
                    2、对象调成员方法
                    3、对象调成员变量

'''

class Foo:
    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):
        print('我是__call__方法')

    def __getitem__(self, item):
        print('我是__getitem__方法',item)

    def __setitem__(self, key, value):
        print('我是__setitem__方法',key,value)

    def __delitem__(self, key):
        print('我是__delitem__方法',key)

    def __enter__(self):
        print('开始__enter__')
        return '周润发'

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('开始__exit__')

    # __hash__ = None  #加上这个后，类就是不可哈希，可变的，不能作为字典的key
    # 注意点:这里是=赋值 而不是==值的判断


f1 = Foo() #新建对象，自动执行构造方法
f1() #我是__call__方法  新建对象()，会自动调用__call__()方法

f1['name']  #我是__getitem__方法 name

f1['name'] = 'jack'  #我是__setitem__方法 name jack

del f1['name']  #我是__delitem__方法 name
print('-----------------------------------1')

with f1 as temp:  #用法：在打开文件的时候，自动关闭文件对象
    print(temp)  #周润发 这里是__enter__方法中的return值
    print('我是with')
print('-----------------------------------2 with')
# 开始__enter__
# 周润发
# 我是with
# 开始__exit__

#类或者对象默认是可哈希的，不可变的，可以作为字典的key
object
dic1 = {}
dic1[Foo] = '我是类名'
dic1[f1] = '我是对象名'
print(dic1)
#{<class '__main__.Foo'>: '我是类名', <__main__.Foo object at 0x000000E7DA8F9B88>: '我是对象名'}
print('-----------------------------------3 __hash__() 类名和对象名是可哈希的，不可变的')

class Boy:
    def __init__(self,name,age,hobby):
        self.name = name
        self.age = age
        self.hobby = hobby
    def __str__(self):
        # return self.name,self.age,self.hobby #报错
        # TypeError: __str__ returned non-string (type tuple)  返回值必须是字符串，而不能是元组
        return '%s %s %s' % (self.name,self.age,self.hobby) #报错

b1 = Boy('jack',16,'run')
print(b1)  #<__main__.Boy object at 0x000000129811DAC8>  默认打印对象的内存地址
print(b1) #jack 16 run
print('-----------------------------------4 __str__() 对象的自定义输出')

'''
__str__() 方法 小结
1、__str__() 方法是Boy的父类object的方法，如果子类不重写的话
打印对象，就是打印对象的内存地址
2、子类重写__str__() 方法后
    再次打印对象，就可以不输出对象的内存地址，而是自定义输出了
3、注意点：
    __str__() 方法的返回值的类型必须是字符串，而不能是元组，否则会报错
'''

class Girl:
    def __init__(self,name,age,hobby):  #构造方法
        self.name = name
        self.age = age
        self.hobby = hobby
    def __new__(cls, *args, **kwargs):
        print('准备开辟内存空间')
        return object.__new__(cls) #这里的cls表示类名Girl本身
        #这句话才是创建对象

g1 = Girl('lucy',15,'read')
print(g1)
# 准备开辟内存空间
# <__main__.Girl object at 0x000000507EAC14C8>
print('-----------------------------------5 __new__() 创建对象')

'''
创建对象的步骤
1、加载类
2、开辟内存空间：通过__new__(cls)方法
3、创建对象：    通过__new__(cls)方法的返回值
                 return object.__new__(cls)来创建对象
                 注意点：__new__（）的参数是cls类，而不是对象（因为现在对象还没有创建出来）
4、初始化对象：
                创建对象的过程中，自动调构造方法__init__()，初始化对象
                把成员变量封装到对象中，就是初始化对象
5、使用对象：
                1、打印对象
                2、对象调成员方法
                3、对象调成员变量
'''









