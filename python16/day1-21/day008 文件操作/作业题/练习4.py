#!/usr/bin/env python
#-*- coding:utf-8 -*-


'''
4，有如下文件t4.txt：

alex是老男孩python发起人，创建人。
alex其实是人妖。
谁说alex是sb？
你们真逗，alex再牛逼，也掩饰不住资深屌丝的气质。

将文件中所有的alex都替换成大写的SB（文件的改的操作）。
'''

import os

f = open('t4.txt',mode='r+',encoding='utf-8')
f2 = open('t5.txt',mode='w',encoding='utf-8')
for i in f:
    line1 = i.strip()
    line2 = line1.replace('alex','SB')   #注意：replace 不会改变原 string 的内容
    # print(line1)
    print(line2)
    # f2.write(line1+'\n')   #这个就不行，因为replace不会改变原字符串的内容--关键点
    f2.write(line2+'\n')

f.close()
f2.close()

os.remove('t4.txt')  #删除原文件
os.rename('t5.txt','t4.txt')  #新建的文件，重命名为原文件

'''
伪代码思路：
1、for循环遍历文件对象f
2、将每一行的字符串中的alex替换成SB
3、新的字符串写入新的文件对象f2
4、删除文件对象f对应的文件
5、重命名文件对象f2对应的文件名（改成已删除的文件名）

注意点：
replace 不会改变原 string 的内容
'''














