#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2019/12/14 17:14
#@author:wangtongpei
#@email: cn5036520@163.com

#分页 方法2  推荐
class Page:
    def __init__(self,lst,pagesize): #参数1是列表  参数2是每页显示的元素个数
        self.lst = lst
        self.pagesize = pagesize

    def start(self,page_num): #参数1 实参传入首页页码1
        '''
        返回第一页的内容
        '''
        #调用私有方法，显示一页的元素（这里显示第一页的元素，返回）
        content = self.__calculate_content(page_num)
        return  content

    def end(self,page_num): #实参需要传入末页的页码
    # def end(self,last_page_num): #实参需要传入末页的页码
        '''
        返回最后一页的内容
        '''
        # 调用私有方法，显示一页的元素（这里显示最后一页的元素，返回）
        content = self.__calculate_content(page_num)  #关键点
        return content

    def index(self):
        '''
        返回指定页的内容  这里是包含第一页和最后一页的
        '''
        # self.total_page_num = len(self.lst)//self.pagesize #地板除
        while 1:
            try:
                page_num = input('请输入你要查询的页码,输入q退出:')
                if page_num.upper() == 'Q':
                    print('主动退出了')
                    break
                elif int(page_num) <= self.total_page_num+1:  #self.total_page_num
                    # 在类中的属性已经定义了这个成员变量self.total_page_num，成员变量可以在类中不同的成员方法间使用
                    page_num = int(page_num)
                    content= self.__calculate_content(page_num)  #调私有方法，参数是用户输入的页码
                    print(content) #打印指定页面的元素内容
                    # return content   #这里一旦返回，就退出整个while循环了   注意点1
                    # any_page = self.lst[self.pagesize*(page_num-1):self.pagesize*page_num] #关键点
                    #把上一行作为共同点提取-抽象出来
                    # print(any_page)
                else:
                    print('你输入的页码超出范围了')
            except ValueError as e:  #输入非数字的异常处理
                print('请输入数字',e)
        # return content

    #输出每页的内容，首页，末页，指定页都会用到，封装成私有方法--共同点提取（抽象）出来，就是封装的思想   关键点3
    def __calculate_content(self,page_num):  #定义私有方法 输出每页的内容
        content = self.lst[self.pagesize * (page_num - 1):self.pagesize * page_num]  # 关键点1
        # print(content)
        return content

    #计算最后一页的页码  --用属性  页码是名词  推荐
    @property
    def last_page_num(self):   #关键点4
        self.total_page_num = len(self.lst)//self.pagesize #地板除
        if len(self.lst)%self.pagesize == 0:  #1 如果可以整除，余数是0，商就是最后一页的页码
            last_page = self.total_page_num
        else:  #2 如果不可以整除，余数不是0，商+1就是最后一页的页码
            last_page = self.total_page_num+1
        return last_page  #3返回最后一页的页码

    ##计算最后一页的页码  --用成员方法
    def last_page_num2(self):
        self.total_page_num = len(self.lst) // self.pagesize  # 地板除
        if len(self.lst) % self.pagesize == 0:  # 1 如果可以整除，余数是0，商就是最后一页的页码
            last_page = self.total_page_num
        else:  # 2 如果不可以整除，余数不是0，商+1就是最后一页的页码
            last_page = self.total_page_num + 1
        return last_page  # 3返回最后一页的页码

# li1 = [0,1,2,3,4]
li1 = [i for i in range(99)]  #列表推导式
pagesize = 2  #定义每页多少个元素

p1 = Page(li1,pagesize)  #1新建对象，自动调构造方法
first_page = p1.start(1) #2调首页成员方法，实参是1
print(first_page)
print('-------------------1 首页')

last_page_num = p1.last_page_num  # 对象调属性，得到末页的页码  last_page_num是属性名
last_page = p1.end(last_page_num)  #3 调末页成员方法，实参是对象的属性  #关键点2
#这里用p1.laset_page_num  对象名.属性
print(last_page)  #末页 对象先调属性，后调成员方法
print('-------------------2 末页1')

last_page_num = p1.last_page_num2() #对象调成员方法，得到末页的页码  last_page_num2是成员方法名
last_page = p1.end(last_page_num)  #3 调末页成员方法，实参是对象的成员方法  #关键点3
#这里用p1.laset_page_num2()  对象名.成员方法
print(last_page)  # 末页 对象先调成员方法-计算末页页码数，后调成员方法end，显示末页的元素内容
print('-------------------3 末页2')

any_page = p1.index()
print(any_page)
print('-------------------4 指定页')

'''
小结：
1、首页、末页、指定页都用到的显示某一页的元素内容，提取抽象出来，成一个私有方法
   --封装思想
2、计算末页的页码数，页码数是名词，用属性
3、在对象调末页成员方法的时候，实参是页码数
   01先用对象.属性名的方法，得到页码数，然后把页码数当做实参传入--推荐这个，更好理解
   02也可以把对象.属性名直接作为实参（类比：连读）
4、列表推导式来造数
5、异常处理-页码不是数字
6、页码是数字，超出范围的处理--条件判断

用到的知识点：
1、私有方法
      类中可见，不对外暴露
2、封装：
      共同点提取和抽象的思想--重点
3、属性：
      计算末页页码数
4、列表推导式：
      列表多元素造数
5、异常处理：
      页码输入不是数字
6、条件判断：
    页码输入超出页码范围
7、面向对象
    分步：     推荐 好理解
        1、对象先调属性，得到末页页码数
        2、对象再调末页成员方法，传入实参末页页码数
    一步      不推荐（类比：连读）
        1、对象调末页成员方法，实参是对象调属性（即末页页码数）

注意点：
1、在类中，成员变量和成员属性是一个东西
2、不管是构造方法中前缀是self的成员变量（数据库字段）
   还是定义的时候，加上@property，调用的时候，不加小括号-成员属性 都是一个东西
3、一般来说
   类外面，叫变量和函数
   类里面，叫成员变量(成员属性)和成员方法
'''












