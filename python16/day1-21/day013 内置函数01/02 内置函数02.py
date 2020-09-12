#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2019/10/13 8:21
#@author:wangtongpei

li1 = ['a','b','c']
for i in li1:  #简洁
    print(i)
print('------------------1')

for i in range(len(li1)):
    print(li1[i])   #循环的是索引，列表根据索引取值  （间接取值）
print('------------------2')

for i in range(len(li1)):
    print(i,li1[i])
print('------------------3')
# 0 a
# 1 b
# 2 c

for i in enumerate(li1):
    print(i)  #元组（索引号和元素组成）
# (0, 'a')
# (1, 'b')
# (2, 'c')
print('------------------4')

for k,v in enumerate(li1):
    print(k,v) #这里k v是对上述元组的解构
# 0 a
# 1 b
# 2 c
print('------------------5')

for k,v in enumerate(li1,1):  #参数2是对索引号的修正，偏移
    print(k,v) #这里k v是对上述元组的解构
# 1 a
# 2 b
# 3 c
print('------------------6')

#排序
#sorted(iterable, cmp=None, key=None, reverse=False)
li1 = [1,3,5,6,2]
li2 = sorted(li1)  #reverse参数不写，默认是False（升序），li2是新产生的列表，原列表没有变化
print(li2)  #[1, 2, 3, 5, 6]
print('------------------排序1 默认升序')

li1 = [1,3,5,6,2]
li3 = sorted(li1,reverse = True)  #reverse参数不写，默认是False（升序），这里True是-降序（而不是倒序）
print(li3)  #[6, 5, 3, 2, 1]
print('------------------排序2 降序')

li31 = [('b',1),('a',3),('e',2)]
#如何将上述列表，按照其元素-元组的第二项进行降序排列
li32 = sorted(li31,key=lambda x:x[-1],reverse=True)
#key 主要是用来进行比较的元素，只有一个参数，
# 具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
print(li32)  #[('a', 3), ('e', 2), ('b', 1)]
print('------------------排序3 指定可迭代对象中的一个元素来进行排序 key参数')

li1 = [1,'']
li2 = ['',False]
li3 = []
print(any(li1))  #True
print(any(li2))  #False
print(any(li3))  # False
# print(any())  #会报错  TypeError: any() takes exactly one argument (0 given)
'''
any相等于or
1、其参数中的元素有一个是True，结果就是True；
2、只有全部元素都是False，才是False；
3、0 None '' [] () {} set() False是False；其余都是True
4、any的参数是可迭代的对象-Iterable
'''
def any1(iterable):
    for i in iterable:
        if i:  #可迭代对象中的元素，如果有一个是True，any的返回就是True
            return True
    return False #当可迭代对象的元素全部是False，any的返回才是False
ret1 = any1(li1)
print(ret1)  #True
print('----------------any')

li11 = [1,'']
li22 = ['',False]
li33 = []
print(all(li11))  #False
print(all(li22))  #False
print(all(li33))  #True   特殊点
# print(all())  #会报错 TypeError: all() takes exactly one argument (0 given)
'''
all相等于and
1、其参数中的全部元素都是True，结果才是True；有一个是False，结果就是False
2、0 None '' [] () {} set() False是False；其余都是True
3、all的参数是可迭代的对象-Iterable
4、参数是空列表或者空元组，返回是True--特殊点
'''

def all1(iterable):
    for i in iterable:
        if not i:#只要其中一个元素是False，结果就是False
            return False
    return True  #当可迭代对象中的每个元素都是True的时候，all的返回才是True
ret2 = all1(li11)
print(ret2)  #False
print('----------------all')

li1 = ['中国','美国']
li2 = ['北京','华盛顿']
a = zip(li1,li2)  #<zip object at 0x0000005B119BFA08>
#参数是可迭代的-Iterable
print(a)
print(list(a))  #[('中国', '北京'), ('美国', '华盛顿')]
#将迭代器转换成列表
print('__iter__' in dir(a)) #True
for i in a:  #循环遍历迭代器
    print(i)
# ('中国', '北京')
# ('美国', '华盛顿')

a1,a2=zip(*zip(li1,li2))  ## 与 zip 相反，zip(*) 可理解为解压，返回二维矩阵式  还原
print(a1)
print(a2)
# ('中国', '美国')
# ('北京', '华盛顿')
print('----------------zip')









