#!/usr/bin/env python
#-*- coding:utf-8 -*-

# 10,写函数，传入n个数，返回字典{‘max’:最大值,’min’:最小值}
# 例如:min_max(2,5,7,8,4) 返回:{‘max’:8,’min’:2}(此题用到max(),min()内置函数)

#方法1
def func(*args,**kwargs):  #形参 *args和**kwargs 将多个位置参数和多个关键字参数 聚合打包成元组和字典
    # print(args)
    print(kwargs)  #{'max': 3, 'min': 1}

li1 = [1,2,3]
dic1 = {}
max1 = max(li1)  #1 计算列表中元素的最大值
min1 = min(li1)  #2 计算列表中元素的最小值
dic1['max'] = max1 #3 添加元素-键值对到字典
dic1['min'] = min1
# print(dic1)
func(*li1,**dic1)  #实参 *args和**kwargs 将列表或者字典解包打散，变成多个位置参数和多个关键字参数
print('---------------------1')

#方法2
def func2(*args):
    dic1 = {'max':max(args),'min':min(args)}
    print(dic1)
    return dic1

li2 = [1,3,7]
func2(*li2)
{'min': 1, 'max': 7}











