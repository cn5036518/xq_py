#!/usr/bin/env python
#-*- coding:utf-8 -*-

#写读模式 w+   （先写后读）  很少用到，因为每次一打开文件，就把之前的内容全部清除了
# 正确用法：先去写，写完后读取（读取前，需要先seek移动光标）

path1 = r".\ceshi4.txt"
f = open(path1,mode="w+",encoding="utf-8")
f.write("疙瘩汤")   #会把文件清空后，再开始写入
f.flush()
content = f.read()
print(content)  #空白 原因是：写入完毕后，光标在文件最末尾，此时读取就读取不到内容了
f.close()










