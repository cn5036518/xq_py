#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""
11，写函数，用户传入修改的文件名，与要修改的内容，执行函数，完成整个文件的批量修改操作（升级题）。
"""

#这个写法应该不对
def modify_file(file_name,content): #文件名和修改内容作为参数
    # （修改不同的文件，修改不同文件的内容，不需要修改源代码，只需要修改实参即可）
    f = open(file_name,mode='r+',encoding='utf-8')
    print(f.tell())  #0  r+模式下，光标默认在文件开头
    f.seek(0,2)  #将光标移动到文件末尾
    f.write('\n'+content)  #在文件最后添加一行‘hello’
    f.close()

file_name1 = '001.txt'
content1 ='hello'
modify_file(file_name1,content1)










