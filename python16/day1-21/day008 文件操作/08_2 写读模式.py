#!/usr/bin/env python
#-*- coding:utf-8 -*-

#写读模式 w+   （先写后读）

path1 = r".\ceshi4.txt"
f = open(path1,mode="w+",encoding="utf-8")
f.write("疙瘩汤")   #会把文件清空后，再开始写入
f.flush()
f.seek(0) #表示移动光标到文件开头  #参数1是偏移量（偏移单位是字节bytes），
# 0表示文件最开头，1表示文件开头第一个字节（这里是字节，而不是字符）后
# f.seek(3) #表示移动光标到文件开头  #参数1是偏移量（偏移单位是字节bytes，3个字节是1个汉字），
# 0表示文件最开头，1表示文件开头第一个字节后
# f.seek(1) #表示移动光标到文件开头  #参数1是偏移量（偏移单位是字节bytes，3个字节是1个汉字，1个字节是1/3个汉字，会报错），
# UnicodeDecodeError: 'utf-8' codec can't decode byte 0x96 in position 0: invalid start byte

# 0表示文件最开头，1表示文件开头第一个字节后

#参数2不写默认是0，表示从文件开头开始算起（偏移量的参考基线）
#参数2 指定1，表示从文件当前光标所在位置算起（偏移量的参考基线）
#参数2 指定2，表示从文件末尾算起（偏移量的参考基线）

#seek(offset[, whence])
# offset -- 开始的偏移量，也就是代表需要移动偏移的字节数

# whence：可选，默认值为 0。
# 给offset参数一个定义，表示要从哪个位置开始偏移；
# 0代表从文件开头开始算起，1代表从当前位置开始算起，2代表从文件末尾算起。

content = f.read()
print(content)  #疙瘩汤
f.close()
















