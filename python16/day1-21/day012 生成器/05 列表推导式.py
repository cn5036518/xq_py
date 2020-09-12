#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2019/10/6 18:26
#@author:wangtongpei

#题目3 获取1-100内能被3整除的数，放在一个列表中
li1 = [i for i in range(1,101) if i%3==0]
print(li1)  #[3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33,
#  36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99]
print('-------------1')
"""
写列表推导式的通用步骤--归纳总结
1、创建空列表  []
2、for循环遍历放入空列表 [for i in range(1,101)]
    注意点：如果是嵌套列表，就需要写2个for循环
    嵌套列表的列表推导式写法:
    [j for i in li1 for j in i if条件筛选]   #注意点：结果是j，而不是i

3、结果变量放入空列表内前半部分  [i for i in range(1,101)]
    结果变量：指的是append（）小括号中的
4、if条件筛选放入空列表内最后部分  [i for i in range(1,101) if i%3==0]
5、用变量名保存整个列表  li1 = [i for i in range(1,101) if i%3==0]

列表推导式
1、适用场景：等差数列相关的数，存入一个列表  （奇偶、整除等）
2、两层嵌套的for循环，建议用for循环，不建议用列表推导式
"""

#题目4 获取1-100内能被3整除的数的平方(结果)，放在一个列表中
li2 = [i**2 for i in range(1,101) if i%3==0]  #这里i**2就是结果，即append()小括号中的
# li2 = [i*i for i in range(1,101) if i%3==0]  #这里i*i和i**2是等效的
print(li2)  #[9, 36, 81, 144, 225, 324, 441, 576, 729, 900, 1089, 1296, 1521, 1764, 2025,2304, 2601,
#  2916, 3249, 3600, 3969,#  4356, 4761, 5184, 5625, 6084, 6561, 7056, 7569, 8100, 8649, 9216, 9801]
print('-------------2 列表推导式，结果有变化')

#题目5 筛选下属列表中名字带有1个o的人的名字
li3 = ['jack','tom','bob']
li4 = [i for i in li3 if 'o'in i]
print(li4) #['tom', 'bob']
print('-------------3 列表推导式，条件筛选 in')

#题目6 筛选下属列表中名字带有2个b的人的名字
li3 = ['jack','tom','bob']
li4 = [i for i in li3 if i.count('b') == 2]  #count('b') 统计字符串中b这个字符出现的次数
print(li4) #[''bob']
print('-------------4 列表推导式，条件筛选 in')

#题目7 筛选下属列表中名字带有2个b的人的名字
li6 = [['jack','tom','bob'],['jack2','tom2','bob2']]
#方法1  列表推导式--列表嵌套
li6 = [name for first in li6 for name in first if name.count('b') ==2]  #好理解
##注意点：结果是name，而不是first
# li6 = [j for i in li6 for j in i if j.count('b') ==2]
print(li6)  #['bob', 'bob2']
print('-------------7-1 列表推导式，列表嵌套')

#方法2 常规思路，列表嵌套
li6 = [['jack','tom','bob'],['jack2','tom2','bob2']]
li61 = []
for i in li6:
    for j in i:
        if j.count('b')==2:
            li61.append(j)
print(li61)
# ['bob', 'bob2']
print('-------------7-1 非列表推导式，常规写法，列表嵌套')


