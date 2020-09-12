#!/usr/bin/env python
#-*- coding:utf-8 -*-

s1 = "abcddddas"
#需求：计算字符串中，子字符串中每个字符都不重复的时候，最大长度的子字符串

"""
思路：
1、循环遍历字符串
2、通过空字符串进行拼接
3、拼接前，先判断一下，如果新的字符已经在之前拼接的字符串中
   就需要将之前拼接的字符串的第一次出现的字符，切片切出去
4、然后接着拼接
"""
s0 = ""
li1= []
li2= []
for i in range(len(s1)):
    if s1[i] not in s0:  #不在拼接字符串，就拼接
        s0 = s0 + s1[i]
        # print(s0)
        # print(len(s0))
        li1.append(len(s0))
        li2.append(s0)
        # print(li1)
    else:  #2 如果已经在拼接字符串。就需要将之前拼接的字符串的第一次出现的字符（及它之前的字符），切片切出去
        index1 = s0.index(s1[i]) #3 计算第二次出现字符a的时候，字符a第一次在已经拼接字符串的位置-索引号
        s0 = s0[index1+1:] #4 将字符a第一次出现的位置，即位置之前的字符，切片切出去
        s0 = s0 + s1[i] #5 继续拼接字符串
print(s0)    #das   问题是：abcd比das要长，但是abcd被切片切出去了
print(max(li1)) #4   数目求出来了，但是子字符串还没输出
print(li1)
print(li2)
# #     max(iterable[, key=func]) -> value
# # max(a, b, c, ...[, key=func]) -> value
# #
# # With a single iterable argument, return its largest item.
# # With two or more arguments, return the largest argument.
#
dic1 = {}
for i in li2:
    pass
    dic1[i] = len(i)
print(dic1)  #{'abcd': 4, 'das': 3, 'da': 2, 'a': 1, 'abc': 3, 'ab': 2}
#
# #如何给字典进行排序，用字典的value进行排序
# # from collections import Counter
# # s11 = Counter(dic1)
# # print(s11)
#
li11 = sorted(dic1.items(),key=lambda x:x[1],reverse=True)
print(li11)


"""



"""


# 题目描述
#
# 给定一个字符串，请找出其中无重复字符的最长子字符串。
#
# 样例
# 例如，在”abcabcbb”中，其无重复字符的最长子字符串是”abc”，其长度为 3。
# 对于，”bbbbb”，其无重复字符的最长子字符串为”b”，长度为1。
#
# 思路#
# 遍历字符串中的每一个元素。
# 借助一个辅助键值对来存储某个元素最后一次出现的下标。
# 用一个整形变量存储当前无重复字符的子串开始的下标。

def longest_substring(str):
    if str == None or len(str)==0:
        return 0
    maxlen = 0 #最大的字串长度
    position = {}#保存非重复字符最后的位置
    start = 0#保存非重复字串开始的位置
    for i in range(len(str)):  #0-4
        if (str[i] in position) and (position[str[i]] >= start) :
            start = position[str[i]] +1
            position[str[i]] = i
        position[str[i]] = i
        current_len = i-start+1 #当前非重复字串的长度
        maxlen = max(maxlen, current_len)
    return maxlen

# if __name__ == '__main__':
#     print('longest substring:')
#     str1 = 'abcab'
#     # str1 = ''
#     print(longest_substring(str1))














