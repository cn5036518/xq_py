#!/usr/bin/env python
#-*- coding:utf-8 -*-

#需求：将文件1中所有good，全部修改成sb
"""
思路1：
1、将文件1的内容全部读取到内存中--read
2、内存中-字符串中，替换字符串后，形成新的字符串
3、将新的字符串写入文件2
弊端：如果文件大，内存会爆掉
扩展：删除文件1，将文件2重命名成文件1

思路2：--改进版  推荐
两个文件，文件1逐行读（读完后，逐行修改），文件2逐行写（每修改一行，写入一行）
1、循环遍历文件1--for i in f1
   逐行读取文件1的内容
2、过程中，对每一行-字符串，进行替换后，形成新的为字符串
3、将每一行新的字符串逐行写入文件2
扩展：删除文件1，将文件2重命名成文件1--nok
"""
#方法1  #不推荐
path1 = r".\002\alex2.txt"
path2 = r".\002\alex3.txt"
with open(path1, mode="r", encoding="utf-8") as f:  #只读
    content = f.read()  #读取文件1的全部内容到内存（字符串中）
    content2 = content.replace("good","sb")   #字符串的方法，对字符串本身没有任何修改
    #参数3不写，就是替换所有，参数3如果是1，只替换左边第一个good，其余不替换

with open(path2, mode="w", encoding="utf-8") as f: #只写
    f.write(content2) #把读完后的字符串，批量修改后，全部一次性写入到文件2

#方法2  #推荐  关键点--必须掌握
path1 = r".\002\alex4.txt"
path2 = r".\002\alex5.txt"
with open(path1, mode="r", encoding="utf-8") as f, open(path2, mode="w", encoding="utf-8") as f2:
    #注意：一次性打开两个文件，第二个文件open前面必须有逗号分隔，行末必须是冒号,2个文件对象f和f2
    for i in f:
        i2 = i.replace("good","sb")  #1将每一行进行逐行替换
        f2.write(i2) #2将修改后的每一行，逐行写入文件2











