#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2019/10/30 7:56
#@author:wangtongpei

#len()
s1 = 'jack'
print(len(s1))  #4  字符串中字符的个数

li1 = [1,2]
print(len(li1)) #2  列表中元素的个数
print('----------------1 len()')

#2 sorted()
li2 = [1,3,2]
li3 = sorted(li2)  #reverse不写默认是False 升序
print(li3)  #[1, 2, 3]

li4 = sorted(li2,reverse = True) #倒序
print(li4)  #[3, 2, 1]

li2 = [1,3,2]
li5 = sorted(li2,key=lambda x:x*-1)  #通过参数key 进行倒序
#key参数还可以用于指定对象中的一个元素进行排序
print(li5)  #[3, 2, 1]

li6 = sorted(li2,key=lambda x:x)
print(li6)  #[1, 2, 3]  #通过参数key 进行升序

li2 = [1,3,2]
li2.sort()  #这里返回值是None  注意
print(li2)  #[1, 2, 3]
'''
sort()和sorted（）的区别
1 sort()是列表的内置方法，排序的同时，将原列表修改了
2 sorted（）的参数不仅仅是列表，还可以是字符串等其他Iterable的对象
  排序的同时，新产生了一个新的排序后的对象，原对象没有任何改变
'''
print('----------------2 sorted()')

#3 enumerate()
li3 = ['jack','tom','bob']
print(enumerate(li3))  #枚举对象<enumerate object at 0x0000006A5A37AB38>
print(list(enumerate(li3))) #[(0, 'jack'), (1, 'tom'), (2, 'bob')]
# 将枚举对象转换成列表  （列表的元素是元组，元组有索引号和原列表元素组成）

#输出列表的索引号和元素
#方法1
for i in enumerate(li3):  #循环遍历枚举对象
    print(i)
# (0, 'jack')
# (1, 'tom')
# (2, 'bob')

#方法2
li3 = ['jack','tom','bob']
for i in range(len(li3)):
    print(i,li3[i]) #默认分隔符是空格
    # print(i,li3[i],sep=',')
# 0 jack
# 1 tom
# 2 bob
print('----------------3 enumerate()')

#4 all()函数
#参数是可迭代对象，可迭代对象中的元素除了0 空字符串'' None False外，其余都是True
#所有元素都是True，结果才是True；有一个元素是False,结果就是False
# 注意：列表或者元组的元素是空白，返回是True   特殊点
li1 = []
tu1 = ()
s1 = ''
print(all(li1))  #True  空列表是True
print(all(tu1))  #True  空元组是True
print(all(s1))   #True  空字符串是True
print('----------------4-1 all()')

print(all([0])) #False  列表中的元素0是False
# print(all(0)) #报错 TypeError: 'int' object is not iterable
print(all([None])) #False 列表中的元素None是False
print(all([False])) #False 列表中的元素False是False
print(all([''])) #False 列表中的元素--空字符串''是False
print('----------------4-2 all()')

print(all([[]])) #False 列表中的元素--空列表''是False
print('----------------4-3 all()')

#all()函数的算法
def all1(iterable):
    for i in iterable:
        if not i:  #有一个元素是False就是False
            return False
    return True
li1 = [0,1,2]
ret = all1(li1)
print(ret)  #False 列表的元素含有0，返回False

li2 = ['',1,2]
ret = all1(li2)
print(ret)  #False 列表的元素含有''，返回False
print('----------------4-4 all()')

#5 any()函数
#参数是可迭代对象，iterable中的元素只要有一个是True，结果就是True
#元素中0 空字符串'' None False是False，其余的都是True
#注意：空列表（列表的元素是空白）和空元组也是False
print(any([])) #False 空列表是False
print(any(())) #False 空元组是False
print(any('')) #False 空字符串是False
print('----------------5-1 any()')

print(any([0,'',None,False,[],()]))  #False 全部是False，结果就是False
print('----------------5-2 any()')

#any() 函数的算法
def any1(iterable):
    for i in iterable:
        if i:
            return True
    return False
ret1 = any1([0,1])
print(ret1)  #True

li1 = [0,None,False,'',[],()]
ret2 = any(li1)
print(ret2) #False
print('----------------5-3 any()')

'''
all()和any()的区别
1 前者是iterable中的元素全部是True，结果才是True
2 后者是iterable中的元素只要有一个是True，结果就是True
3、元素中0 '' None False是False，其余都是True
4、注意点
    空列表（列表中的元素是空白）、空元组、空字符串，all()函数返回True--特殊点
    空列表（列表中的元素是空白）、空元组、空字符串，any()函数返回False
'''

#zip（） 函数
li1 = [1,2]
li2 = [3,4]
ret1 = zip(li1,li2)
print(ret1)  #<zip object at 0x00000021A24E4788>
print(type(ret1)) #<class 'zip'>
print('__iter__' in dir(ret1))  #True  说明是一个迭代器
print(list(ret1))  #[(1, 3), (2, 4)]
print('----------------6-1 zip()')

li1 = [1,2]    #2个元素
li2 = [3,4,5]  #3个元素
ret1 = zip(li1,li2)
print(ret1)  #<zip object at 0x00000021A24E4788>
print(list(ret1))  #[(1, 3), (2, 4)]  #以最短的iterable为准
print('----------------6-2 zip()')

a1,a2 = zip(*zip(li1,li2))  #zip()类比：压缩打包  zip(*)类比：解压解包
print(list(a1)) #[1, 2]
print(list(a2)) #[3, 4]
print('----------------6-3 zip()')






















