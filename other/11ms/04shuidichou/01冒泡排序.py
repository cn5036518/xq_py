#!/usr/bin/env python
#-*- coding:utf-8 -*-

#一、从小到大排序 -冒泡排序
#方法1，直接互换位置，不引入临时变量
li1 = [1,3,2,4,1]   #冒泡排序主要针对列表
# s1 = "1324"  #不适合字符串
def bobble_sort(li1):
    for i in range(0,len(li1)):  #0-3  限定范围-外循环
        #1外循环的过程，
        #第一次循环，先拿元素1依次和后面的元素2，元素3，元素4进行对比后，把大数放在最右边
        #第二次循环，再拿元素2依次和后面的元素3、元素4进行对比后，把大数放在最右边
        #第三次循环，再拿元素3依次和后面的元素4进行对比后，把大数放在最右边
        for j in range(i+1,len(li1)):  #1-3，限定范围-内循环
            if li1[i] > li1[j]:  # 从小到大排序，大数都放在右边（如果是从大到小排序，就是小的数放右边，大于号改成小于号）
                #2内循环过程
                # 第一次循环，元素1和元素2对比，
                # 第二次循环，元素1和元素3对比，
                # 第三次循环，元素1和元素4对比--
                #把两两对比中大的数，放在右边（交换位置）
                li1[i],li1[j] = li1[j],li1[i]  #a,b = b,a（交换位置方法1 直接互换位置，不引入临时变量，简洁）
    print(li1)  #[1,1, 2, 3, 4]
bobble_sort(li1)
# bobble_sort(s1)  #TypeError: 'str' object does not support item assignment

#方法2，互换位置，引入临时变量--互换的思想理解
li1 = [1,3,2,4,1,22]   #冒泡排序主要针对列表
# s1 = "1324"  #不适合字符串
def bobble_sort2(li1):
    for i in range(0,len(li1)):  #0-3  限定范围-外循环
        #1外循环的过程，
        #第一次循环，先拿元素1依次和后面的元素2，元素3，元素4进行对比后，把大数放在最右边
        #第二次循环，再拿元素2依次和后面的元素3、元素4进行对比后，把大数放在最右边
        #第三次循环，再拿元素3依次和后面的元素4进行对比后，把大数放在最右边
        for j in range(i+1,len(li1)):  #1-3，限定范围-内循环
            if li1[i] > li1[j]:  #
                #2内循环过程
                # 第一次循环，元素1和元素2对比，
                # 第二次循环，元素1和元素3对比，
                # 第三次循环，元素1和元素4对比--
                #把两两对比中大的数，放在右边（交换位置）
                # li1[i],li1[j] = li1[j],li1[i]  #a,b = b,a（交换位置方法1 直接互换位置，不引入临时变量，简洁）
                temp = li1[i]  #1大的数存入临时变量
                li1[i] = li1[j] #2小的数赋值给大的数
                li1[j] = temp    #3把临时变量赋值给小的数  #通过中间临时变量实现大数和小数的位置互换
    print(li1)  #[1, 1, 2, 3, 4, 22]
bobble_sort2(li1)

#二、从大到小排序 -冒泡排序
#方法1，直接互换位置，不引入临时变量
li1 = [1,3,2,4,1]   #冒泡排序主要针对列表
# s1 = "1324"  #不适合字符串
def bobble_sort(li1):
    for i in range(0,len(li1)):  #0-3  限定范围-外循环
        #1外循环的过程，
        #第一次循环，先拿元素1依次和后面的元素2，元素3，元素4进行对比后，把小的数放在最右边
        #第二次循环，再拿元素2依次和后面的元素3、元素4进行对比后，把小的数放在最右边
        #第三次循环，再拿元素3依次和后面的元素4进行对比后，把小的数放在最右边
        for j in range(i+1,len(li1)):  #1-3，限定范围-内循环
            if li1[i] < li1[j]:  # 从小到大排序，大数都放在右边（如果是从大到小排序，就是小的数放右边，大于号改成小于号）
                #关键点：这里是大于号就是从小到大排序，是小于号就是从大到小排序
                #2内循环过程
                # 第一次循环，元素1和元素2对比，
                # 第二次循环，元素1和元素3对比，
                # 第三次循环，元素1和元素4对比--
                #把两两对比中小的数，放在右边（交换位置）
                li1[i],li1[j] = li1[j],li1[i]  #a,b = b,a（交换位置方法1 直接互换位置，不引入临时变量，简洁）
    print(li1)  #[4, 3, 2, 1, 1]
bobble_sort(li1)
# bobble_sort(s1)  #TypeError: 'str' object does not support item assignment

#方法2，互换位置，引入临时变量--互换的思想理解
li1 = [1,3,2,4,1,22]   #冒泡排序主要针对列表
# s1 = "1324"  #不适合字符串
def bobble_sort2(li1):
    for i in range(0,len(li1)):  #0-3  限定范围-外循环
        #1外循环的过程，
        #第一次循环，先拿元素1依次和后面的元素2，元素3，元素4进行对比后，把小的数放在最右边
        #第二次循环，再拿元素2依次和后面的元素3、元素4进行对比后，把小的数放在最右边
        #第三次循环，再拿元素3依次和后面的元素4进行对比后，把小的数放在最右边
        for j in range(i+1,len(li1)):  #1-3，限定范围-内循环
            if li1[i] < li1[j]:  ##关键点：这里是大于号就是从小到大排序，是小于号就是从大到小排序
                #2内循环过程
                # 第一次循环，元素1和元素2对比，
                # 第二次循环，元素1和元素3对比，
                # 第三次循环，元素1和元素4对比--
                #把两两对比中小的数，放在右边（交换位置）
                # li1[i],li1[j] = li1[j],li1[i]  #a,b = b,a（交换位置方法1 直接互换位置，不引入临时变量，简洁）
                temp = li1[i]  #1小的数存入临时变量
                li1[i] = li1[j] #2大的数赋值给小的数
                li1[j] = temp    #3把临时变量赋值给大的数  #通过中间临时变量实现大数和小数的位置互换
    print(li1)  #[22, 4, 3, 2, 1, 1]
bobble_sort2(li1)

"""
冒牌排序总结
1、通过两层嵌套的for循环的过程：---思考过程--关键点
    内循环实现了：
        第一次循环：元素1和元素2，
        第二次循环：元素1和元素3、
        第三次循环：元素1和元素4的一一比对，通过互换变量（直接互换，或者引入临时遍历），把大的数放在最右边
    外循环实现了：
        第一次循环：先拿元素1依次和后面的元素2、元素3、元素4进行一一对比
        第二次循环：再拿元素2依次和后面的元素3、元素4进行一一对比
        第三次循环：再拿元素3依次和后面的元素4进行一一对比
"""















