#!/usr/bin/env python
#-*- coding:utf-8 -*-

li1 = [1,2,3,4]
#需求：请删除列表中的奇数项
#方法1
li2 = []
for i in range(len(li1)):
    if i%2 == 1:
        li2.append(li1[i])
print(li2)  #[2, 4]

#二、列表在循环遍历的过程中，一边循环一边删除是有问题的
#方法1--错误1
li1 = [1,2,3,4]
for i in li1:
    li1.remove(i)  #只能删除奇数项  remove是指定元素名称删除
 # L.remove(value) -> None -- remove first occurrence of value.
 #        Raises ValueError if the value is not present.
print(li1)  #[2, 4]
# 分析原因:
# for的运行过程. 会有⼀个指针来记录当前循环的元素是哪一个, 一开始这个指针指向第0
# 个. 然后获取到第0个元素. 紧接着删除第0个. 这个时候. 原来是第一个的元素会自动的变成
# 第0个. 然后指针向后移动⼀一次, 指向1元素. 这时原来的1已经变成了0, 也就不会被删除了.
# ---所以最终只删除了奇数项，偶数项留了下来

#方法2--错误2
li1 = [1,2,3,4]
for i in li1:
    li1.pop()  #pop是按照索引号进行删除，不写默认是删除最后一个，并且返回
    # li1.pop(i)  #报错 IndexError: pop index out of range
       # L.pop([index]) -> item -- remove and return item at index (default last).
       #  Raises IndexError if list is empty or index is out of range.
print(li1)  #[2, 4]
print("------------pop1")

##方法2-2--正确1
li1 = [1,2,3,4]
for i in range(len(li1)):   #循环len(li)次, 然后从后往前删除
    li1.pop()  #pop是按照索引号进行删除，不写默认是删除最后一个，并且返回
    # li1.pop(i)  #报错 IndexError: pop index out of range
       # L.pop([index]) -> item -- remove and return item at index (default last).
       #  Raises IndexError if list is empty or index is out of range.
print(li1)  #[2, 4]

#方法3--错误3
# li1 = [1,2,3,4]
# for i in range(len(li1)):
#     del li1[i]  #报错 IndexError: list assignment index out of range

#方法4--正确2   推荐 必须掌握
li1 = [1,2,3,4]
li2 = []
for i in li1:  #1 循环遍历列表1
    li2.append(i)  #2 把列表1符合条件的元素依次添加到空列表2
print(li2)   #[1, 2, 3, 4]

for i in li2:   #3遍历循环列表2
    li1.remove(i) #4遍历循环列表2的过程中，删除列表1的元素
print(li1)  #[]

"""
范围：对于列表、字典、集合等可迭代对象，可变对象 (元组和字符串本事是不可修改的)
注意: 由于删除元素会导致元素的索引改变, 所以容易出现问题.
 尽量不要在循环中直接去删除元素. 可以把要删除的元素添加到另一个集合中
 然后再批量删除.
"""









