#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/5/24 8:41

#需求：删除列表中元素是2开头的元素

''''''
'''
思路1：
1、列表在循环的过程中，不能一边循环，一边删除列表中的元素
    列表的remove只能一次删除一个元素，无法一次删除多个元素
2、把要删除的元素，添加到一个新列表中
3、循环新列表，循环体中，老列表.remove(新列表的元素)

思路2：
用filter函数
'''

#方法1
li = ['jack1','tom','bob','jack2']

li2 = []

#1把要删除的元素，添加到一个新列表中
for i in li:
    if i.startswith('j'):
        li2.append(i)

#2循环新列表，循环体中，老列表.remove（新列表中的元素）
for i in li2:
    li.remove(i)

print(li)
#['tom', 'bob']
print('-----------------1')

#方法2 filter函数

li = ['jack1','tom','bob','jack2']

result = filter(lambda x:x.startswith('j'),li)
print(result)  #<filter object at 0x0000028E9208C1D0>   返回值是一个filter对象
print(type(result)) #<class 'filter'>
print(list(result))  #['jack1', 'jack2']
print('-----------------2')

#方法2-2 filter函数

li = ['jack1','tom','bob','jack2']

result = filter(lambda x:not x.startswith('j'),li)
print(result)  #<filter object at 0x0000028E9208C1D0>   返回值是一个filter
print(type(result)) #<class 'filter'>
print(list(result))  #['tom', 'bob']
print('-----------------2-2')

# li.remove('jack1','jack2') #TypeError: remove() takes exactly one argument (2 given)
# print(li)

'''
小结：
需求：删除列表中符合指定条件的元素，返回值是一个新的列表

1、filter的用法--推荐
参数1：函数名或者lamdba表达式
参数2：列表等可迭代对象
返回值：filter对象
        要转换成列表，需要用list(filter对象)进行转换

2、列表在循环遍历自身元素的时候，是不能一边遍历，一边删除的--算法
   思路：遍历老列表的时候，把需要删除的元素添加到新的空列表
         循环新的列表，循环体中，老列表.remove(新列表的元素)

'''


















