#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/6/27 15:37

''''''
'''
栈  类比：装馒头的桶
1、入栈
2、出栈
属性：   列表（容器） 大小（容器的大小） 栈顶指针（指向下一个入栈的地方）

需求：队列有专门的模块queue，栈是没有专门的模块的，需要手写
思路：
1、定义个类
2、构造方法
    参数：大小size
    空列表-容器
    栈顶指针

3、入栈方法--push
    异常：栈满了

4、出栈方法--pop  （先进后出，后进先出）
    异常：栈的元素空了
'''
class StackFullError(Exception):
    pass

class StackEmptyError(Exception):
    pass


class Stack:
    def __init__(self,size):
        self.size = size   #容器大小
        self.li1 = []      #空列表（容器）
        self.index = 0    #栈顶指针  刚刚开始，栈顶指针在列表的索引号是0的位置

    def push(self,el):   #1往栈中放元素
        if self.index < self.size:
            self.li1.insert(self.index,el)   #1先在索引号是0的位置，插入一个新元素
            # self.li1[self.index] = el #  IndexError: list assignment index out of range
            #  上面行是字典的写法，列表这么写会报错
            self.index += 1  #2再在索引号是1的位置，插入下一个新元素；接着在索引号是2的位置，继续插入一个新元素。。。
        else:  #当栈顶指针等于容器大小的时候
            raise StackFullError('stack is full')

    def pop(self):   #从栈中取出元素--后进先出
        if self.index >0:
            self.index -= 1   #1 栈顶自减1
            return self.li1[self.index]  #2 将栈顶指针指向的元素return
        else:   #当大小是0的时候，抛出异常
            raise StackEmptyError('stack is empty')

    def clear(self):  #将栈清空
        self.li1 = []    #1列表容器清空
        self.index = 0   #2栈顶指针的位置归零，初始化

    def pointer_of_stack(self):
        print(self.index)  #返回栈顶指针的位置
        return self.index

    def size_of_stack(self):
        print(self.size)  #返回栈的容器大小
        return self.size

s1 = Stack(3)
s1.push(1)   #往栈中添加3个元素，分别是1,2,3
s1.push(2)
s1.push(3)
# s1.push(4)  #StackFullError: stack is full

print(s1.pop())  #3 #从栈中取出3个元素，分别是3,2,1  （后进先出）
print(s1.pop())  #2
print(s1.pop())  #1
# s1.pop()  #StackEmptyError: stack is empty
print('-------------------------1   先把1 2 3依次放进去，然后3 2 1取出来')

s1.push(4)   #往栈中添加3个元素，
print(s1.pop())  #4

s1.push(5)
print(s1.pop())  #5

s1.push(6)
print(s1.pop())   #6
print('-------------------------2   放一个到栈中，从栈中取一个')














