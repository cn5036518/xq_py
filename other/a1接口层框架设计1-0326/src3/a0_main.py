#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""
目录结构：
1、将所有的文件都先放在src文件夹中
2、请求类：http_class.py
   出参-目的-返回-return：是返回实际响应结果

3、遍历case类:a2_forcese.py
    出参-目-返回-return：获取excel中的字段，将字段作为元组返回后，作为接口类的入参（*ret1 可变长参数）

4、接口类：a3_interface.py
            入参：接口类的入参是遍历case类的出参--即从excel中读取的字段
            逻辑：接口类需要调用请求类（需要先导入请求类文件的get和post类）返回实际响应结果，
                 将实际响应结果和excel中获取的检查点（通过遍历case类获取）进行比对

5、主函数：入口函数
    1、先导入接口类和遍历case类的文件
    2、新建遍历类的对象，调方法，返回excel中的字段作为元组ret1返回
    3、新建接口类的对象，调方法，入参是*ret1--前面加上星号
        返回的时间响应结果和excel中获取的检查点（通过遍历case类获取）进行比对
"""

from a2_forcase import Forcase    #from 文件名 import 类名
from a3_interface import Interface_test

# 一、新建遍历类对象
forcase1 = Forcase()  #前天，先将遍历类导入进来
# 遍历类对象调方法
ret1 =forcase1.forcase()
# print(ret1)

# # # 二、新建接口类对象
# # test1 = Interface_test(url, params1, headers1, check_point1, method1, data_type1,yes_no1)  # 自动执行构造方法，传入参数
# test1 = Interface_test(*ret1)  # 自动执行构造方法，传入可变长参数  元组变量前面必须加上星号*
# # # 接口对象调方法
# test1.test()

for j in ret1:
    print(j)
#     # # 二、新建接口类对象
#     # test1 = Interface_test(url, params1, headers1, check_point1, method1, data_type1,yes_no1)  # 自动执行构造方法，传入参数
    test1 = Interface_test(*j)  # 自动执行构造方法，传入可变长参数  元组变量前面必须加上星号*
#     # # 接口对象调方法
#     test1.test()






















