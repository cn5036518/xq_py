#!/usr/bin/env python
#-*- coding:utf-8 -*-

def eat(*args): #*表示的是动态参数（不定长参数，参数个数可以一个或者多个），接收到的是元组
    #args是参数名
    print('我要吃',args)

tu1 = 'rice'
tu2 = ('rice','apple','cherry')
li1 = ['apple','orange','banana']
eat(tu1)  #我要吃 ('rice',)  #
eat(tu2)  #我要吃(('rice', 'apple', 'cherry'),)   #元组嵌套元组，一般不是想要的
eat(*tu2)  #我要吃('rice', 'apple', 'cherry')
eat(li1)  #我要吃 (['apple', 'orange', 'banana'],)  #元组嵌套列表，一般不是想要的
eat(*li1)  #我要吃 ('apple', 'orange', 'banana')
# #注意：实参 *li1会把列表中的每一个元素，打包成一个元组，传递给形参
print('--------------1')

'''
一、形参-位置的动态参数  *args
1、 *表示接收位置参数的动态参数
2、传参顺序
    位置 *args 默认值 **kwargs   #关键点 记住
    1、如果默认值参数在*args前面。如果想让默认值生效。
        *args将永远接不到值
def func(a,b,*args,c=5): #arguments参数
    print(a,b,c,args)

func(1,2,3,4,5,6,8,c=10)

二、形参-关键字的动态参数 **kwargs
1、*args 位置参数，接收到的是元组
2、**kwargs 关键字的动态传参，接收到的是字典
def func(**kwargs):   #key word arguments
    print(kwargs)

func(a=10,b=20,jay='周杰伦',jj='林俊杰')

三、无敌模式-所有的参数都能接收
def func(*args,**kwargs): #一个或者多个位置参数，一个或者多个关键字参数
    print(args)
    print(kwargs)

func(1,2,5,jj='陶喆',jay='周杰伦')

四、*args位置参数
def func(*args):#在这里，*其实相当于把传进来的参数做了一次聚合，聚合成元组
    print(args)

li1 = '娃哈哈'
func(*li1) #在实参位置，*表示打散，打散的是可迭代对象(字符串、列表、元组)-不包含字典

五、**kwargs关键字参数
def func(**kwargs): # ** 把接收到的关键字参数打包（聚合）成字典
    print(kwargs) #一定是字典

dic1 = {'张无忌':'明教教主','谢逊':'金毛狮王'}

func(张无忌=dic1['张无忌'],谢逊=dic1['谢逊'])  #这么写不方便
func(**dic1) #这里的 **是把字典打散，字典的key作为参数的名字
    字典的value作为参数的值 传递给形参**kwargs

六、形参小结
1、位置参数
2、默认值参数
3、动态参数
    1、*args 位置参数的动态传参。
        系统会自动的把所有的位置参数聚合成元组
    2、**kwargs 关键字参数的动态传参。
        系统会自动的把所有的关键字参数聚合成字典
    3、def func(*args,**kwargs):  #无敌参数
           pass
    4、顺序： 位置参数，*args,默认值，**kwargs   关键点
    5、上述顺序，在使用的时候，可以任意的进行搭配
4、在实参上，*,**表示的是打散（位置参数或者关键字参数）
   在形参上，*,**表示聚合（元组或者字典）
5、例子
    def func1(*args):
        print(args)
    func1(1,2,4,6)

    def func2(*args):   #推荐1：将多个位置参数作为列表的元素，通过*li1-实参传入到形参*args
        print(args)
    li1 = [1,5,7]
    func1(*li1)

    def func3(**kwargs):
        print(kwargs)
    func3(name='jack',age=18)

    def func4(**kwargs):  #推荐2:将多个关键字参数作为字典的元素（键值对），通过**dic1-实参传递给形参**kwargs
        print(kwargs)
    dic1 = {'name':'jack','age':19}
    func4(**dic1)
'''
#一、动态参数-位置参数  *args  实参是多个位置参数
def func1(*args): #*接收多个位置参数，接收的是元组
    print(args)  #(1, 2, 4, 6)
func1(1,2,4,6)  #将4个位置参数作为元组的元素，打包成元组，传递给形参args
print('--------------1 将多个位置参数作为实参传入')

#二、动态参数-位置参数 *args 实参是*列表、元组、字符串等可迭代对象（不包含字典）--推荐1
#适用场景：当位置参数比较多的时候，比如超过5个，可以将位置参数作为列表的元素，通过*列表名-实参传入
def func2(*args): #形参 *表示，将多个位置参数聚合成元组
    print(args)  #(1, 5, 7)
li1 = [1,5,7]
func1(*li1)  #实参，列表前面的*，表示将列表打散（解包-解构）
print('--------------2 将多个位置参数-用*列表的方式作为实参传入')

#三、动态参数-关键字参数 **kwargs 实参是多个关键字参数
def func3(**kwargs):  #形参 **kwargs 把接收到到关键字参数，聚合成字典，关键字参数的名字作为字典的key
    #关键字参数的值作为字典的value
    print(kwargs)  #{'age': 18, 'name': 'jack'}
func3(name='jack',age=18) #实参是关键字参数
print('--------------3 将多个关键字参数作为实参传入')

#四、动态参数-关键字参数 **kwargs 实参是**字典   --推荐2
def func4(**kwargs): #**在形参，表示把关键字参数聚合成字典
    print(kwargs)  #{'name': 'jack', 'age': 19}
dic1 = {'name':'jack','age':19}
func4(**dic1)  #** 在实参，表示将字典打散（解构成键值对）
print('--------------4 将多个关键字参数-用**字典的方式作为实参传入')








