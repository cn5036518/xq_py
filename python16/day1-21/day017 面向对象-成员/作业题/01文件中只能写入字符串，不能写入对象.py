#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2019/12/9 6:15
#@author:wangtongpei
#@email: cn5036520@163.com


class User:
    def __init__(self,user,pwd):
        self.user = user
        self.pwd = pwd

with open('acount1.txt', mode='w', encoding='utf-8') as f:
    u1 = User('jack','123')
    # u1 = str(u1)
    f.write(u1)  #报错，文件中只能写入字符串，不能写入对象
    #TypeError: write() argument must be str, not User















