#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2019/12/14 12:03
#@author:wangtongpei
#@email: cn5036520@163.com

#分页 方法1
class Page:
    def __init__(self,lst,pagesize):
        self.lst = lst
        self.pagesize = pagesize

    def start(self):
        '''
        返回第一页的内容
        '''
        first_page = self.lst[:self.pagesize]
        return first_page  #注意这里的返回

    def end(self):
        '''
        返回最后一页的内容
        '''
        self.total_page_num = len(self.lst)//self.pagesize #地板除
        if len(self.lst)%self.pagesize == 0:
            last_page = self.lst[self.pagesize*(self.total_page_num-1):self.pagesize*self.total_page_num]
        else:
            last_page = self.lst[self.pagesize*self.total_page_num:]
        return last_page

    def index(self):
        '''
        返回指定页的内容  这里是包含第一页和最后一页的
        '''
        while 1:
            try:
                page_num = input('请输入你要查询的页码,输入q退出:')
                if page_num.upper() == 'Q':
                    print('主动退出了')
                    break
                elif int(page_num) <= self.total_page_num+1:
                    page_num = int(page_num)
                    any_page = self.lst[self.pagesize*(page_num-1):self.pagesize*page_num] #关键点
                    print(any_page)
                else:
                    print('你输入的页码超出范围了')
            except ValueError as e:  #输入非数字的异常处理
                print('请输入数字',e)
        return any_page

# li1 = [0,1,2,3,4]
li1 = [i for i in range(99)]  #列表推导式
pagesize = 2  #定义每页多少个元素

p1 = Page(li1,pagesize)
first_page = p1.start()
print(first_page)

last_page = p1.end()
print(last_page)

any_page = p1.index()
print(any_page)










