#!/usr/bin/env python
#-*- coding:utf-8 -*-

#计算两个数的和，+的底层算法
# 使用列表的方式实现两个大数字相加的操作
#
# 思路：
# 1，把输入的数字转化为列表，
# 2，比较列表的长度，不够的就在前面补0
# 3，将两个列表元素逐个相加，得出新的列表
# 4，如果元素大于等于10，则将这个元素重新赋值为取余10之后的结果，并且将前一个元素加一，
# 5，将结果输入即可。
# ---------------------

"""
步骤：
1 先位数相等
    注意点1：判断进位问题
2 再考虑位数不等
    注意点2：如果两个列表的长度不一样，在循环遍历过程中，进行两个列表的元素相加的时候，短的列表会出现越界的情况--报错
    IndexError: list index out of range
    还可能出现循环短列表的时候，长列表的多出位置没有参加计算
"""

n1 = "1554"
n2 = "917"

li1 = [0]  #解决8+4=12  多了一位1   注意点1
li2 = [0]

for i in n1:
    li1.append(i)  #1 将字符串中的而数字依次添加到空列表1
for i in n2:
    li2.append(i)
print(li1)  #[0, '5', '5', '4']
print(li2)  #[0, '9', '1', '7']

#对于两个列表长度不一致的情况，给短的列表前面补0（索引号是0的位置，插入0）
differerce = abs(len(li1) - len(li2))
if len(li1) > len(li2):
    for i in range(differerce):
        li2.insert(0,0)
else:
    for i in range(differerce):
        li1.insert(0, 0)
print(li1)  #[0, '1', '5', '5', '4']
print(li2) #[0, 0, '9', '1', '7']

li3 = []
for i in range(len(li1)):
    sum1 = int(li1[i]) + int(li2[i])  #2 将两个列表中的元素（字符转成int），相加的和后，依次添加到空列表3
    li3.append(sum1)
print(li3)  #[0, 14, 6, 11]

for i in range(len(li3)):  #通过索引，循环遍历列表3
    if li3[i] > 10:  #3 判断进位问题，如果两个数之和大于10，就需要进位
        li3[i] = li3[i]%10 #4 进位的处理，当前位，用除以10取余数即可
        li3[i-1] = li3[i-1] +1 #5 当前位的前一位，自增1即可
print(li3)  #[0,1, 4, 7, 1]

#列表转字符串
# s3 = "".join(li3)
# print(s3) #列表的元素是字符串才行，是int是不能直接拼接的
# 报错  TypeError: sequence item 0: expected str instance, int found
s3 = ""
for i in li3:
    s3 = s3 + str(i)  #注意，这里需要将int转换成str，才能进行拼接
print(s3)  #02471  字符串类型

#z字符串转数字
sum = int(s3)
print(sum)  #2471










