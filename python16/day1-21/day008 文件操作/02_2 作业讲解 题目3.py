#!/usr/bin/env python
#-*- coding:utf-8 -*-

# 3.完成彩票36选7的功能. 从36个数中随机的产生7个数. 最终获取到7个不重复的数据作为最终的开奖结果.
# 随机数:

from random import randint
randint(1, 36) # 1 - 36 的随机数（包含1和36）
# Return random integer in range [a, b], including both end points.

set1 = set()  #不重复，就要用到集合
while len(set1)<7:  #0-6  #当长度是6个的时候，最后一次循环，如果添加重复的数字进入集合，集合还是6位，还会继续循环，
    #直到添加的是不重复的数字，长度是7个的时候，while的条件才会终止
    #总结：条件判断的时候，就只能用while；而不能用for
    random_num1 = randint(1, 8)  #1 产生随机数
    set1.add(random_num1) #2 给集合单个增加元素
    # print(set1)
print(set1)

# {6}
# {3, 6}
# {1, 3, 6}
# {8, 1, 3, 6}
# {8, 1, 3, 6}
# {8, 1, 3, 5, 6}
# {1, 2, 3, 5, 6, 8}
# {1, 2, 3, 5, 6, 8}
# {1, 2, 3, 5, 6, 7, 8}















