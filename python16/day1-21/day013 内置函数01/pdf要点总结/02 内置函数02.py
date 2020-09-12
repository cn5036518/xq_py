#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2019/10/20 8:47
#@author:wangtongpei

#一、作用域相关的
def func1():
    a = 1
    print('哈哈')
    print(locals())  #{'a': 1}  返回的局部变量，在字典中
func1()

print(locals())  #函数外，locals()和globals()是一样的返回结果
print(globals())
print('-----------------作用域相关的1')

#二、迭代器相关
#1 range()
for i in range(2):
    print(i)
print('-----------------2-1迭代器相关 range()')

#2 next()  #迭代器向下取一个值
li1 = [1,2]
# next(li1)  #TypeError: 'list' object is not an iterator
#注意：列表不是迭代器-Iterator，列表是可迭代类型的-Iterable
#列表作为参数传入iter()中，返回值是迭代器；列表调__iter__()方法后，返回值是迭代器
print('__iter__' in dir(li1))  #True  列表是Iterable，返回True
print('__iter__' in dir(3))  #False   int不是Iterable，返回False

it1 = iter(li1)
print(it1)  # #<list_iterator object at 0x0000002B0451B548>
print(next(it1))  #1  #迭代器向下取一个值
print(it1.__next__())  #2  #迭代器向下取一个值
print('__iter__' in dir(it1)) #True  it1是迭代器-Iterator，返回True
print('-----------------2-2迭代器相关 next()')

#3 iter()  #参数是列表等可迭代类型的-Iterable，返回的是迭代器-Iterator
it1 = iter(li1)
print(it1)  #<list_iterator object at 0x0000002B0451B548>

it2 = li1.__iter__()
print(it2)  #<list_iterator object at 0x0000002B0451B548>
print('-----------------2-3迭代器相关 iter()')

'''
可迭代类型的（可迭代的）：Iterable
    包括：str list tuple dict set range() open()
迭代器：Iterator
    Iterator = iter(Iterable)  或者
    Iterator = Iterable.__iter__()
'''

#三、其他
#1 字符串类型代码的执行
#01 eval（）
s1 = '1+3'
print(eval(s1))  #4
print('-----------------3-1 其他-字符串类型代码 eval()')

s31 = '[1,2]'
print(eval(s31))  #[1, 2]
print('-----------------3-1-1 其他-字符串类型代码 eval() 列表去掉引号')

s32 = "{'name':'jack'}"   #重点
print(eval(s32))  #{'name': 'jack'}
print('-----------------3-1-2 其他-字符串类型代码 eval() json字符串去掉引号转成字典')

#02 exec()
s2 = '''
for i in range(2):
    print(i)
'''
s3 ='''
def func():
    print('我是函数1')
func()
'''
print(exec(s2))  #None  #因为exec()只是执行代码，但是没有返回值，所以是None
print(exec(s3))  #None
print('-----------------3-2 其他-字符串类型代码 exec()')

#03 compile()
s1 = '1+3'
s2 = "{'name':'jack'}"
c1 = compile(s1,'','eval')  #编译字符串形式的代码
print(eval(c1))  #4

c2 = compile(s2,'','eval')  #编译字符串形式的代码
print(eval(c2)) #{'name': 'jack'}
print('-----------------3-3-1 其他-字符串类型代码 compile()+eval() ')

s3 = '''
for i in range(2):
    print(i)
def func2():
    print('我是函数2')
func2()
'''
c3 = compile(s3,'','exec')
exec(c3)
print(exec(c3)) #None  exec（）没有返回值，就返回None
print('-----------------3-3-2 其他-字符串类型代码 compile()+exec() ')

# s4 = '''
# #content = input('请输入你的名字：')
# #print(content)  #会报错SyntaxError: multiple statements found while compiling a single statement
# '''
# #single这个模式只能用于input，不能在input之外加上其他任何语句，比如：有print不行，否则报错
# c4 = compile(s4,'','single')
# exec(c4)
print('-----------------3-3-3 其他-字符串类型代码 compile()+single+exec() ')

# content = input('请输入数字：')
# print(content)  #1  这里的数字1,，输入后，返回的是字符串'1'
# #注意：这里的字符串'1'如果需要用于计算，就需要先转换成int，否则报错
# print(type(content))  #<class 'str'>
# print('-----------------4-1 输入 ')

a = 1
print(a)  #打印变量
print('-----------------4-2 输出打印 ')

a1 = 555577777
a2 = 555577777
print(id(a1))
print(id(a2))
print(a1 is a2) #True
#这里a1和a2都指向了同一个内存空间，a1和a2分别是同一个内存空间的不同别名
#这里a1和a2并没有在内存中开辟2个不同的内存空间
print('-----------------5-1 id（）')

li1 = [1,2]
# print(hash(li1))  #报错TypeError: unhashable type: 'list'

str = 'jack'
print(hash(str))  #-8203720448203180971
print(type(hash(str)))  #<class 'int'>

'''
可变对象（不可哈希的）：list dict set
不可变对象（可哈希的）：int str bool tuple frozenset

只有不可变对象才有哈希值，可变对象是没有哈希值的（给可变对象取哈希值，会报错）
'''
print('-----------------5-2 hash（）')

# # path1 = r'..\code1.py'  #上级目录  ..是错误的写法  ..后面要加上\才对  ..\是正确的写法
# path1 = r'..\code1.py'  #这里的..\ 表示上一级目录  ..\..表示上上级目录
# # path1 = r'../code1.py'  #这里的../ 表示上一级目录  ../..表示上上级目录  和上面等效
# f = open(path1,mode='r',encoding='utf-8')
# ret1 = f.read()
# print(ret1)
# print('-----------------6-1 open（）函数 上一级目录 ')

# path2 = r'..\..\test.py'  #这里的..\ 表示上一级目录  ..\..\表示上上级目录-正确  ..\..是不对的，后面缺少\
# # path2 = r'..\..test.py'  #这里的..\..是不对的，..\..\是对的
#
# f = open(path2,mode='r',encoding='utf-8')
# ret1 = f.read()
# print(ret1)
# print('-----------------6-2 open（）函数 上上级目录 ')
#
# path3 = r'..\..\..\zuoye.py'  #这里的..\ 表示上一级目录  ..\..\表示上上级目录-正确
# f = open(path3,mode='r',encoding='utf-8')
# ret1 = f.read()
# print(ret1)
# print('-----------------6-3 open（）函数 上3级目录 ')

'''
相对路径小结
..\ 表示上一级目录     例如：path1 = r'..\code1.py'
..\..\表示上上级目录   例如：path2 = r'..\..\test.py'   这里的r是去掉转义
..\..\..\表示上3级目录 例如：path3 = r'..\..\..\zuoye.py'
'''

#7 callable() 函数  用于检查一个对象是否是可以被调用的
print(callable('a'))  #False
print(callable(123))  #False
def func():
    print('我是函数7')
print(callable(func))  #True

class A:
    def method(self):
        return 0
a1 = A()
print(callable(A))  #True
print(callable(a1)) #False
'''
str int和类的对象是不可被调用的，返回False
函数、类是可被调用的，返回True
'''
print('-----------------7 callable()函数 ')

#8 dir() 函数
li1 = [1,2]
print(dir(li1))  #返回参数-比如列表的属性，方法列表 返回的是一个列表
# ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__',
#  '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__',
#  '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__',
#  '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
# '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__',
#  'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
print('-----------------8 dir()函数 ')












