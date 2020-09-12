#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2019/11/15 7:03
#@author:wangtongpei
#@email: cn5036520@163.com

#1 print
print('哈哈1')
print('哈哈2',end='\n')  #默认结束符是 换行 \n
print('哈哈3',end=' ')  #把默认的结束符-换行  改成 空格
print('---------------------1')

print('哈哈4',end=' ',sep=',') #注意点：这个sep分隔符在打印一个信息的时候，是体现不出来的
print('---------------------2')

li1 = [1,2,3]
for i in li1:
    print(i,end='')  #123 #结束符从默认的换行 改成了 空白
print('---------------------3')

for i in li1:
    print(i,end='\n',sep=' ') #end-结束符不写默认是换行符 sep不写默认是空格
print('---------------------4')

for i in li1:
    print(i,end='\n',sep=',') #
print('---------------------5')

for i in li1:
    print(i,end='',sep=',') #
print('---------------------6')

for i in li1:
    print(i,end=' ',sep=',') #
print('---------------------7')

for i in range(len(li1)):
    print(i,li1[i],end='\n',sep=' ') #
print('---------------------8')

for i in range(len(li1)):
    print(i,li1[i]) #
print('---------------------9')

for i in range(len(li1)):
    print(i,li1[i],end='\n',sep=',') #注意点:sep分隔符是针对打印2个及以上元素的
print('---------------------10')

for i in range(len(li1)):
    print(i,li1[i],end=',',sep='*') # 行结束符是 逗号，多个元素间的分隔符号是*
    #0*1,1*2,2*3,
print('---------------------11')

#2 range()
for i in range(2):  #0 1
    print(i)
print('---------------------2-1')

for i in range(1,3):  #1 2
    print(i)
print('---------------------2-2')

for i in range(1,5,2):  #1 3
    print(i)
print('---------------------2-3')









