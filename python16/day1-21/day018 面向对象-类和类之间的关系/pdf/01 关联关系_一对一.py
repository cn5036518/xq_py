#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2019/12/17 7:58
#@author:wangtongpei
#@email: cn5036520@163.com

class Boy:
    def __init__(self,name,girl_friend = None):
        self.name = name
        self.girl_friend = girl_friend

    def meet(self,g):
        self.girl_friend = g

    def hava_dinner(self):
        if self.girl_friend:
            print('%s和%s在吃晚饭' % (self.name,self.girl_friend.name))
        else:
            print('单身狗，没饭吃，哈哈')

class Girl:
    def __init__(self,name):
        self.name = name

g1 = Girl('lucy')
b1 = Boy('jack')

# b1.meet(g1)
b1.hava_dinner()  #单身狗，没饭吃，哈哈
print('------------------1')


g1 = Girl('lucy')
b1 = Boy('jack')

b1.meet(g1)
b1.hava_dinner()  #jack和lucy在吃晚饭
print('------------------2')









