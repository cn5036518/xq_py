#!/usr/bin/env python
#-*- coding:utf-8 -*-

# 2. 给出一个纯数字列表. 请对列表进行排序(升级题).--冒泡排序
# 思路:
# 1. 完成a和b的数据交换. 例如, a = 10, b = 24 交换之后, a = 24, b = 10
# 2. 循环列表. 判断a[i]和a[i+1]之间的大小关系, 如果a[i]比a[i+1]大. 则进行互换. 循环结束的时候.
# 当前列表中最大的数据就会被移动到最右端.
# 3. 想一想, 如果再次执行一次上面的操作. 最终第二大的数据就移动到了右端. 以此类推.
# 如果反复的进行执行相应的操作. 那这个列表就变成了一个有序列表.

# #方法1   中间临时变量temp
# li1 = [9,1,3,2,5,8,7]
#
# for i in range(len(li1)):
#     for j in range(len(li1)):
#         if li1[j] > li1[i]:  #控制升序排列--从小到大
#             # （两两对比--将位置是0--i的数，依次和位置是j--1,2,3...的数进行对比，，将j中大的数放在右边）
#             temp = li1[i]  #变量1存入临时变量
#             li1[i] = li1[j] #变量2存入变量1
#             li1[j] = temp  #临时变量存入变量2   完成互换（通过temp）
#
# # for i in range(len(li1)):
# #     # for j in range(len(li1)):
# #     for j in range(i + 1, len(li1)):  # 这里的i+1，正好将j=i+1 将i和j错开
# #         if li1[i] > li1[j]:  # 控制升序排列--从小到大（如果左边的数，大于右边的数，就互换）
# #             # 如果位置是0-i中的数，大于位置是1,2,3...--j中的数，就把i中的数，放在右边
# #             temp = li1[i]  # 变量1存入临时变量
# #             li1[i] = li1[j]  # 变量2存入变量1
# #             li1[j] = temp  # 临时变量存入变量2   完成互换（通过temp）
# """
# 内循环
# i=0 j=1 对比索引号是0和索引号是1的两个数，
# 把如果索引号是1的数，大于索引号是0的数，就互换位置，大的数，放在索引号是0的位置
# i=0 j=2 对比索引号是0和索引号是2的两个数
# 把如果索引号是2的数，大于索引号是0的数，就互换位置，大的数，放在索引号是0的位置
# ...
# i=0 j=5 对比索引号是0和索引号是5的两个数，把大的数，放在右边
#
# 外循环
# i=1 进行内循环
# i=2 进行内循环
# ...
# i=5 进行内循环
# """
# print(li1)  #[1, 2, 3, 5, 7, 8]
#
# #方法2 不引入中间临时变量
# li1 = [9,1,3,2,5,8,7]
# for i in range(len(li1)):
#     for j in range(len(li1)):
#         if li1[j] > li1[i]:
#             # （两两对比--将位置是0--i的数，依次和位置是j--1,2,3...的数进行对比，，将j中大的数放在右边）
#             li1[i],li1[j] = li1[j],li1[i]  #互换（直接互换，不引入temp）
# print(li1)  #[1, 2, 3, 5, 7, 8]

#方法3   中间临时变量temp   --推荐1  好理解
li1 = [9,1,3,2,5,8,7]

for i in range(len(li1)):
    # for j in range(len(li1)):
    for j in range(i+1,len(li1)):  #这里的i+1，正好将j=i+1 将i和j错开  升序
    # for j in range(0,len(li1)):  #这里的i+1，正好将j=i+1 将i和j错开      降序
        if li1[i] > li1[j]:  #控制升序排列--从小到大（如果左边的数，大于右边的数，就互换）
            #如果位置是0-i中的数，大于位置是1,2,3...--j中的数，就把i中的数，放在右边
            temp = li1[i]  #变量1存入临时变量
            li1[i] = li1[j] #变量2存入变量1
            li1[j] = temp  #临时变量存入变量2   完成互换（通过temp）
"""
内循环
i=0 j=1 对比索引号是0和索引号是1的两个数，把大的数，放在右边
i=0 j=2 对比索引号是0和索引号是2的两个数，把大的数，放在右边
...
i=0 j=5 对比索引号是0和索引号是5的两个数，把大的数，放在右边

外循环
i=1 进行内循环
i=2 进行内循环
...
i=5 进行内循环
"""
print(li1)  #[1, 2, 3, 5, 7, 8]

#方法4 不引入中间临时变量  #推荐2  简洁
li1 = [9,1,3,2,5,8,7]
for i in range(len(li1)):
    # for j in range(len(li1)):
    for j in range(i+1,len(li1)):  #这里的i+1，正好将j=i+1 将i和j错开
        if li1[i] > li1[j]:  #（如果左边的数，大于右边的数，就互换）
            # 如果位置是0-i中的数，大于位置是1,2,3...--j中的数，就把i中的数，放在右边
            li1[i],li1[j] = li1[j],li1[i]  #互换（直接互换，不引入temp）
print(li1)  #[1, 2, 3, 5, 7, 8]

"""
总结：
冒泡排序：--核心词：交换
方法1,2，暂时先放一下
方法3,4，比较好理解，必须掌握

思路回顾：
内循环
第一次循环，将索引号是0和索引号是1的数，进行对比，如果左边的数，大于右边的数，就互换位置
第二次循环，将索引号是0和索引号是2的数，进行对比，如果左边的数，大于右边的数，就互换位置
...
第n次循环，将索引号是0和索引号是n的数，进行对比，如果左边的数，大于右边的数，就互换位置

外循环
第一次外循环，索引号是0，进行内循环
第二次外循环，索引号是1，进行内循环
第三次外循环，索引号是2，进行内循环
...
第n次外循环，索引号是n-1，进行内循环

for i in range(len(li1)):    ---重点，必须掌握
    for j in range(i+1,len(li1)):  #关键点，这里的j从i+1 开始，就把i和j错开了
        if li1[i] > li1[j]:  #如果左边的数大于右边的数，就互换位置（控制升序还是降序，这里是升序）
        # 把大数都换到最右边，就是升序排序（反之，就是降序）
            li1[i],li1[j] = li1[j],li1[i]
"""

#方法5 不引入中间临时变量  老师  推荐
li1 = [9,1,3,2,5,8,7]
for i in range(len(li1)):
    # for j in range(len(li1)):
    # for j in range(len(li1)-1):  #必须是len（li1）-1，不减去1的话，后面的li1[j+1]会出现越界  注意点1
    for j in range(len(li1)-1-i):  #必须是len（li1）-1，不减去1的话，后面的li1[j+1]会出现越界  注意点1
        #注意点2 len(li1)-1-i  这里减i是优化步骤，因为第一次外循环后，最大的数已经在最右边（倒数第一的数，不需要再两两比对了）
        # 第二次外循环后，倒数第二大的数已经在右边倒数第二（倒数第二的数，不需要再两两比对了）
        if li1[j] > li1[j+1]:  #（如果左边的数，大于右边的数，就互换；如果右边的数大， 就不互换，保持现状）
            # 注意这里的j用的是内循环的索引号   注意点3
            # 如果位置是j的数，大于位置是j+1的数，就把位置j的数，放在右边（最大的数，在最右边--气泡向上）
            li1[j],li1[j+1] = li1[j+1],li1[j]  #互换（直接互换，不引入temp）
print(li1)  #[1, 2, 3, 5, 7, 8]
"""
总结：
冒泡排序：   --核心词：交换
方法1,2，暂时先放一下
方法3,4，比较好理解，必须掌握--我的思路  内循环，是索引号是0和索引号是1,2,3，...n-1分别就是比较，大的数放右边（互换）
方法5，  比较好理解，必须掌握--老师思路  内循环，是两两相邻的数进行比较，大的数放右边（互换）

思路回顾：
内循环
第一次循环，将索引号是0和索引号是1的数，进行对比，如果左边的数，大于右边的数，就互换位置
第二次循环，将索引号是1和索引号是2的数，进行对比，如果左边的数，大于右边的数，就互换位置
...
第n次循环，将索引号是n-1和索引号是n的数，进行对比，如果左边的数，大于右边的数，就互换位置

外循环
第一次外循环，索引号是0，进行内循环
第二次外循环，索引号是1，进行内循环
第三次外循环，索引号是2，进行内循环
...
第n次外循环，索引号是n-1，进行内循环
"""
print("-------------排序")

#变量互换的方法有2个
#1 引入临时变量   --必须掌握
a = 20
b = 10
temp = a   #1 变量1放入临时变量temp
a = b      #2 变量2存入变量1
b = temp   #3 临时变量temp存入变量2  从而实现变量1和变量2的互换（除了python外，其他变成语言java等就是这个思路）
print(a)  #10
print(b) #20

#2 不引入临时变量  --必须掌握
a=20
b=10
a,b = b,a   #python可以解包，直接互换两个变量  （先计算等号右边，然后解包，分别赋值给等号左边，从而实现互换）
print(a)  #10
print(b)  #20
print("-------------互换")








