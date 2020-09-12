#!/usr/bin/env python
#-*- coding:utf-8 -*-

li = []   #空列表必须放在for外面，如果放在for里面的话，每次循环就会置为空
for i in range(2):
    # li = []  #错误写法
    print(i)
    li.append(i)    #append必须写在for里面
print(li)  #[0, 1]






















