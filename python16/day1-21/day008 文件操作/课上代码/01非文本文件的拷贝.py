#!/usr/bin/env python
#-*- coding:utf-8 -*-

#需求：将非文本文件001.png拷贝一份到002.jpg
"""
思路：
1、只读模式rb打开文件1
2、只写模式wb打开文件2
3、循环遍历文件1，过程中，写入文件2
4、从而实现图片文件拷贝
注意点：
1 非文本文件不涉及encoding，写了会报错

步骤：

"""
#方法1 简洁3行--推荐
path1 = r".\001.png"
path2 = r".\002.jpg" #注意：可以支持拷贝成不同格式的图片，拷贝后的图片，大小可能需要放大才能看清
with open(path1,mode="rb") as f1, open(path2, mode="wb") as f2: #自动刷新和关闭文件
    for i in f1:
        f2.write(i)

#方法2  7行
path1 = r".\001.png"
path3 = r".\003.jpg"
f1 = open(path1,mode="rb")
f2 = open(path3,mode="wb")
for i in f1:
    f2.write(i)
f2.flush()
f1.close()
f2.close()















