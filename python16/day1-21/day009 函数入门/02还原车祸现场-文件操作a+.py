#!/usr/bin/env python
#-*- coding:utf-8 -*-

f = open('疙瘩汤.txt',mode='a+',encoding='utf-8')
#这里的a+表示可追加可读   如果是a就只能追加，不能读
f.seek(0)   #读取文件后，光标默认在文件最后，将光标移到文件开头
s = f.read(1)
print(s)  #饿
f.seek(0)
f.write('你好')   #这个‘你好’会添加到文件末尾，而不是添加到文件开头
# 官网文档  'a' for appending (which on some Unix systems,
# means that all writes append to the end of the file regardless of the current seek position
f.close()

'''
小结：
1、r+在先读后写的时候，会忽略光标的当前位置，写在文件的最后
2、r+在先读，然后把光标移到开头seek（0）后，再写，写入的内容‘刘伟’会覆盖文件开头的前2个字符
3、a+写的时候，会忽略光标的当前位置，不管光标的位置在哪里，只要是写，就写在文件的最后
'''












