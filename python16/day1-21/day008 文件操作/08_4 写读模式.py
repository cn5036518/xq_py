#!/usr/bin/env python
#-*- coding:utf-8 -*-

#写读模式 w+   （先写后读）

path1 = r".\ceshi4.txt"
f = open(path1,mode="w+",encoding="utf-8")
f.write("疙瘩汤")   #会把文件清空后，再开始写入
f.flush()
f.seek(0,0)  #光标回到文件最开头  #疙瘩汤
# f.seek(1,0)  #报错  UnicodeDecodeError: 'utf-8' codec can't decode byte 0x96
# in position 0: invalid start byte
# 原因是：utf-8下，一个汉字字符是3个字节，这里只从文件开头，偏移了1个字节，不到一个汉字字符，所以会报错

# f.seek(3,0)  #光标回到文件最开头算起，第3个字节之后（utf-8下，一个汉字字符就是3个字节）  #瘩汤
#参数1 指定是偏移量（单位是字节）
       #当参数2不写，或者指定0的时候，参考基线是文件开头
       #此时，参数1是0，表示文件的最开头
       #参数1是1，表示的是文件最开头的第一个字节（这里是字节，而不是字符）后
#参数2 不写默认是0，表示文件开头位置算起（偏移量的参考基线）

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

"""
seek()函数总结：
seek（offset[,whence]）
1 参数1是必填的，参数2不是必填的
2、 参数1是偏移量，单位是字节（而不是字符）
3、 参数2不写，默认是0，表示文件的最开头开始算起（定义偏移量的参考基线）
    参数2指定0，表示文件的最开头开始算起（定义偏移量的参考基线）
    参数2指定1，表示文件的当前光标所在开始算起（定义偏移量的参考基线）
    参数2指定2，表示文件的最末尾开始算起（定义偏移量的参考基线）

# seek(偏移量, 位置)
# 位置: 0开头, 1当前位置, 2末尾
# 移动到末尾: seek(0, 2)
# 移动到开头: seek(0, 0)

注意点：
1、w写模式   新建文件后，写入之前，光标在文件开头，写入字符串后，当前光标是在文件最后的
2、r只读模式 打开文件后，刚刚打开后，光标是在文件的开头
   循环读取或者全部读取所有文件内容后，当前光标就移动到了文件最后
3、a追加写模式 打开文件后，光标是在文件的末尾
4、参数1，偏移量的单位是字节（而不是字符），utf-8下，一个汉字是3个字节
   必须偏移量是3的倍数，否则会出现报错

seek(0,0)  光标移动到文件开头
seek(0,2)  光标移动到文件末尾
"""
















