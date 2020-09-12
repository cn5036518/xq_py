#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2019/12/9 6:21
#@author:wangtongpei
#@email: cn5036520@163.com

with open('acount2.txt', mode='w+', encoding='utf-8') as f:  #写读模式
    f.write('jack|123\n')
    f.write('jack2|123\n')
    f.seek(0,0)   #光标回到文件开头
    # ret = f.read()
    for i in f:
        print(i.split('|')[0])
        print(i.split('|')[1].strip())  #去掉空行


# ret = f.read() #报错
# # ValueError: I/O operation on closed file.
# print(ret.plit('|')[0])










