#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/2/13 7:23
#@author:wangtongpei
#@email: cn5036520@163.com


''''''
'''
第10题
背写你了解的所有特殊方法，并附示例
'''

#callable
# 用于判断是否是可调用的（方法和函数，是可调用的；变量是不可调用的）
'''
伪代码
if callable(args):
    args()   #方法或者函数
else:
    print(args)  #变量

2 构造方法
  __init__()
  用于把传递进来的参数转换成成员变量（方便在不同的方法间使用）

3 __str__()
   打印对象，默认是输出对象的内存地址
   可以用这个方法打印对象，让不输出内存地址，而输出自定义的内容，比如：对象的姓名

4 __call__()
    新建对象，会自动调用__call__()方法

5 __getitem__()
    对象名['name'] 会把name作为参数，传递到__getitem__()的参数中

6 __setitem__()
    对象名['name']='kevin2' 会把key是'name'，value是'kevin2'作为参数
    传递到__getitem__()的参数中

7 __delitem__()
    del 对象名['name'] 会删除刚刚设置的name kevin2键值对

8 __enter__()
    with打开文件，就是先调__enter__()方法，最后调__exit__()方法

9 __exit__()
    with打开文件，就是先调__enter__()方法，最后调__exit__()方法

10 __hash__
    类名及其对象，默认是可哈希的--可变的，可以作为字典的key
    如果在类的定义中，加上__hash__ = None后，类名及其对象名

11 __new__()
   创建对象的过程：
   1、加载类
   2、开辟内存空间
      通过__new__(cls)
   3、创建对象
      通过__new__(cls)方法的返回值
         return object.__new__(cls)来创建对象
         注意点：__new__（）的参数是cls类，而不是对象（因为现在对象还没有创建出来）
   4、初始化对象
      通过__init__()
      把成员变量封装到对象中，就是初始化对象
   5、使用对象
      对象调成员变量
      对象调成员方法

'''

#3 __str__()
class Person:
    def __init__(self,name):
        self.name = name

    # def __str__(self):
    #     return '%s' % self.name   #这里必须返回的是字符串

p1 = Person('jack')
print(p1) #<__main__.Person object at 0x00000060C806D348>


class Person2:
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return '%s' % self.name   #这里必须返回的是字符串

p2 = Person2('jack')
print(p2)  #jack
print('-------------------1 __str__()方法')

#4 __call__()方法
class Person:
    def __init__(self,name):
        self.name = name

    def __call__(self, *args, **kwargs):
        print('我是call方法')

p4 = Person('tom')
p4() #我是call方法
# 对象后面加小括号，调对象--python特有
#一般是对象调方法，很少有调对象的情况
print('-------------------2 __call__()方法')

#5 __getitem__（）方法
class Person:
    def __init__(self,name):
        self.name = name

    def __getitem__(self, item):
        print('我是__getitem__()方法，%s' % item)

p5 = Person('bob')
p5['name']  #相当于把中括号中的'name'传入到了__getitem__()的参数中了
#我是__getitem__()方法，name
print('-------------------3 __getitem__()方法')

#6 __setitem__()方法
class Person:
    def __init__(self,name):
        self.name = name

    def __setitem__(self, key, value):
        print('我是__setitem__()方法',key,value)

p6 = Person('kevin')
p6['name'] = 'kevin2' #把对象看成是字典，key是'name' value是'kevin2'
#我是__setitem__()方法 name kevin2
print('-------------------4 __setitem__()方法')

#7 __delitem__()方法
class Person:
    def __init__(self,name):
        self.name = name

    def __delitem__(self, key):
        print('我是__delitem__()方法',key)

p7 = Person('kate')
del p7['kevin2']
print('-------------------5 __delitem__()方法')

#8 __enter__()方法
class Person:
    def __init__(self,name):
        self.name = name

    def __enter__(self):
        print('我是__enter__()方法')
        return '周润发'

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('我是__exit__()方法')

p8 = Person('lucy')
with p8 as temp:   #和打开文件对象类似（把p8对象换成open(文件名字)）
    print(temp)
    print('我是with')

# 我是__enter__()方法
# 周润发  #是__enter__()方法的返回值
# 我是with
# 我是__exit__()方法
print('-------------------6 __enter__()方法')

#9 __hash__ 方法
# 类和对象都是可哈希的-不可变的，可以作为字典的key
class Person:
    def __init__(self):
        pass

    # __hash__ = None
    #加上这行后，类名及其对象就不能作为字典的key了（因为变成了不可哈希-可变的）
    #TypeError: unhashable type: 'Person'

p1 = Person()

dic1 = {Person:'我是类',p1:'我是对象'}
# dic1 = {p1:'我是对象'}
print(dic1)
#{<class '__main__.Person'>: '我是类',
# <__main__.Person object at 0x0000001C07232B48>: '我是对象'}
print('-------------------9 __hash__()方法')

#10 __new__(cls)方法
class Person:
    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        print('2准备开辟内存空间')
        return object.__new__(cls)

p10 = Person()
print(p10)
# 2准备开辟内存空间
# <__main__.Person object at 0x000000737F2961C8>
print('-------------------10 __new__()方法  创建对象')

'''
创建对象的过程
1、加载类
2、开辟内存空间
    通过__new__(cls)
3、创建对象
    通过__new__(cls)的返回值
        return object.__new__(cls)
4、初始化对象
    通过__init__()构造方法
    将成员变量封装到构造方法中
5、使用对象
    对象调成员变量
    对象调成员方法

'''









