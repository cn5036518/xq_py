#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2019/12/25 6:47
#@author:wangtongpei
#@email: cn5036520@163.com

import random

# dic1 = {'name':'jack','age':18}
# for k,v in dic1.items():
#     pass
#     # print(k)
#     # print(v)
#     print(k,v)

a = '中国'
print('我的祖国是',a)
print('我的祖国是 %s 哈' % a)

course_li1 = [1,2,3,4]
ret = random.sample(course_li1,2)  #从列表中随机选择n个元素，组成新的列表
#参数1是原列表  参数2是n个元素的n
print(ret)










