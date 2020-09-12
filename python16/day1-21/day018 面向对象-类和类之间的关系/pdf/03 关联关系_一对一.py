#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2019/12/17 7:58
#@author:wangtongpei
#@email: cn5036520@163.com

class Boy:
    def __init__(self,name,gril_friend= None):
        self.name = name
        self.gril_friend = gril_friend
    def meet(self,girl):
        self.gril_friend = girl   #这里的girl是女孩对象
    def have_dinner(self):
        if self.gril_friend:
            print('%s %s一起吃晚餐' % (self.name,self.gril_friend.name))
        else:
            print('单身狗，没饭吃，哈哈')

class Girl:
    def __init__(self,name):
        self.name = name

b1 = Boy('jack')   #男孩不是一出生就有女朋友的，男孩出生默认是没有女朋友的
b1.have_dinner()   #单身狗，没饭吃，哈哈
print('------------------1')

g1 = Girl('lucy')
b1.gril_friend = g1  #有女朋友了   1女孩对象在男孩类之外，直接赋值给男孩的成员变量
b1.have_dinner()  #jack lucy一起吃晚餐
print('------------------2')

g2 = Girl('lily')
b2 = Boy('tom',g2)     #2女孩对象在新建男孩对象的时候，传入男孩构造方法
# 一出生就有女朋友，娃娃亲
b2.have_dinner() #tom lily一起吃晚餐
print('------------------3')

g3 = Girl('kate')
b3 = Boy('bob')
b3.meet(g3)    #3女孩对象在男孩对象调成员方法的时候，作为参数传入男孩的成员方法
b3.have_dinner() #bob kate一起吃晚餐
print('------------------4')

b3.gril_friend = None  #男孩失恋了。又单身了
b3.have_dinner() #单身狗，没饭吃，哈哈
print('------------------5')
'''
小结：
关联关系-一对一关系的建立的3种方式：
1、赋值
    女孩对象在男孩类之外，直接赋值给男孩的成员变量
2、女孩对象传入男孩构造方法
    女孩对象在新建男孩对象的时候，传入男孩构造方法
3、女孩对象传入男孩成员方法
    女孩对象在男孩对象调成员方法的时候，作为参数传入男孩的成员方法

关联关系的本质
1、把另外一个类的对象作为当前类的属性（成员变量）来传递和保存

'''







