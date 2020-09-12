#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/5/24 10:35

''''''
'''
需求：把类中的成员变量的名字和值，作为键值对，打印出来

'''

class Foo:
    def __init__(self,name,age):
        self.name = name
        self.age = age   #注意：这里的self表示对象本身，self实质是对象名.__dict__  即是{'name': 'jack', 'age': 18}

f1 = Foo('jack',18)
print(f1.__dict__)
#{'name': 'jack', 'age': 18}
print('-----------------------1')

'''
小结：
1 类中的self表示对象本身
2 self实质是对象名.__dict__
  即是{'name': 'jack', 'age': 18}
3 self.name就等价于取字典{'name': 'jack', 'age': 18}的key是name的value值


'''

dic1 = {}   #这里的dic1就等价于self
dic1['name'] = 'jack'
dic1['age'] = 18
print(dic1)  #{'name': 'jack', 'age': 18}
print('-----------------------2')

class Foo2:
    def __init__(self):
        self.name = 'jack'
        self.age = 18   #注意：这里的self表示对象本身，self实质是对象名.__dict__  即是{'name': 'jack', 'age': 18}

f2 = Foo2()   #这里没有传递参数，而是在构造方法中，将变量写死了，不推荐
print(f2.__dict__)
print('-----------------------3')




















