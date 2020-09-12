#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""
1、模块是什么？（what）
    一个py文件就是一个模块。
    例子：比如xiaoqiang.py就是一个模块

2、如何导入模块？(how)
    ---在代码里写import xiaoqiang即可（注意：导入模块的时候，xiaoqing后面不需要.py）

3、模块的查找顺序
    模块首先从当前目录查询，如果当前目录没有，再按照path顺序逐一查询(sys.path)

4、模块的导入次数
    一个模块只会被导入一次，不管你执行了多少次import。
    好处：这一可以防止导入模块被一遍又一遍地执行。--提升性能
"""

import sum1    #导入模块（导入当前目录下的sum1.py文件）
print(sum1.add1(1,2)) #3  #调用文件sum1.py中的add1函数，传入实参1,2
#格式： 模块名.模块里的函数名

from sum1 import add1  #导入当前目录下的sum1文件中的add1函数
# from sum1 import *  #不推荐，避免这种写法
print(add1(2,3)) #5
#格式2：不需要写模块名，直接写函数名即可

"""
from语句是让你从模块中导入指定的部分（例如：函数）--推荐
from sum1 import * 是把一个模块的所有内容全部都导入，不推荐，有坑
"""
















