#!/usr/bin/env python
#-*- coding:utf-8 -*-

path1 = r".\ceshi5.txt"
f = open(path1,mode="r+",encoding="utf-8")
f.write("我爱我的祖国")
f.seek(9)   #光标移动到文件开头，之后第9个字节后 （第三个中文字符后面）
f.truncate()  #参数是空的时候，会将光标所在位置的后面全部删除，只保留光标所在位置的前面内容  #"我爱我"
f.flush()  #写（新增-write或者删除-truncate） 都需要刷新缓存
f.close()  #关闭文件












