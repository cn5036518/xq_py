#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2019/12/15 9:35
#@author:wangtongpei
#@email: cn5036520@163.com

""""""
'''
关联关系的分类：
一对一关系：男朋友和女朋友
一对多关系：学校和老师
            你，订单，明细，商品
'''

# 一对一关系：男朋友和女朋友
class Boy:
    # def __init__(self,name,girl_friend=None):  #默认参数是None，表示男孩不是天生就有女朋友
    def __init__(self,name):  #默认参数是None，表示男孩不是天生就有女朋友
        self.name = name
        # self.girl_friend = girl_friend

    def meet(self,girl):  #参数是女孩对象  女孩对象传递给男孩的女朋友这个成员变量
        self.girl_friend = girl  #关键点
        #男孩对象的成员变量-girl_friend就是女孩对象
        #注意点：self.girl_friend可以不用先在构造方法中定义，也能使用

    def eat(self):
        if self.girl_friend:  #不是None，就是True
            print('%s和%s一起吃大餐' % (self.name,self.girl_friend.name) )
        else: #None
            print('单身狗，没饭吃了，哈哈')

class Girl:
    # def __init__(self, name,boy_friend):
    def __init__(self, name):
        self.name = name
        # self.boy_friend = boy_friend
    def eat(self):
        print('%s在吃饭'% self.name)

g1 = Girl('lucy')  #1 创建女孩对象，自动调构造方法
b1 = Boy('jack')   #2 创建男孩对象，自动调构造方法

b1.meet(g1)  #3 男孩对象，调成员方法-相遇  参数是女孩对象  关键点
b1.eat()  #jack和lucy一起吃大餐

print(b1.girl_friend.name)  #lucy  这里b1.girl_friend就是girl对象-g1
print(b1.girl_friend.eat()) #lucy在吃饭 这里b1.girl_friend就是girl对象-g1

'''
小结：
关联关系：一对一
1、在类1的成员方法中，把类2的对象作为形式参数，传递给类1的成员变量
    self.类1的成员变量 = 类2的对象
    左边就可以等价于右边（即类2的对象的地方，可以用类1的对象.成员变量表示

依赖关系和关系关系的区别
一、写法不同：
1、前者
    在类1的成员方法中，把类2的对象作为形式参数
    写法:
    类1的成员方法(类2的对象)：  #这里类2的对象可以是冰箱，也可以是高压锅，多态
        类2的对象.类2的成员方法()
2、后者
    在类1的成员方法中，把类2的对象作为形式参数,传递给类1的成员变量
    写法:
    类1的成员方法(类2的对象)：
        self.成员变量=类2的对象
    说明：后面凡是用到类2对象的地方，可以用类1对象.成员变量代替

二、例子
1、前者的例子是大象装冰箱，打车（今天打这个车，明天打那个车）
                     --（类比：关系比较轻，大象可以装不同的冰箱，你可以打不同的车）
   后者的例子是男女朋友--（类比：关系更紧密）


'''














