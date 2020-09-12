#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2019/11/29 6:53
#@author:wangtongpei
#@email: cn5036520@163.com

class Car:
    def run(self,speed):   #这里的self表示当前对象本身，正在执行这个动作的对象
        print('车的速度是 %s' % speed)

c1 = Car()  #新建对象
# Car.run(c1,40)  #车的速度是 40 #类名.方法名(对象名,实际参数)
c1.run(50)  #车的速度是 50   #这里和上面一行是等效的，在理解上
#2 对象调方法，传参数

'''
小结：
类名.方法名(对象名,实际参数)
对象名.方法名(实际参数)

上面2种调方法，是等效的
'''














