#!/usr/bin/env python
#-*- coding:utf-8 -*-

# from a1_interface2 import Interface1  #导入src目录-py文件的接口类
from a1_interface2 import For_case1  #导入src目录-py文件的循环case类
from mail_excel import Send_mail  #导入发邮件文件的类

# path1 = r".\testcase2.xlsx"  #.\表示相对路径，当前目录下，存放测试用例
# path2 = r".\testcase3.xlsx"  #相对路径，当前目录下，存放测试报告（测试用例文件填写测试结果和响应数据后）

import datetime

cur = datetime.datetime.now()
cur = str(cur)
# print(cur)

# path1 = r"D:\PycharmProjects\xiaoqiang\base_181027\a1接口层框架设计1-0326\src26\testcase3.xlsx"
path1_report = r".\testcase3.xlsx"   #附件路径-测试报告路径
from1 = "cn5036520@163.com"
to1 = "cn5036520@163.com"
title1 = "接口测试报告邮件"+cur
content1 = """
    hello world
    hello world2
    """

path2_case = r".\testcase2.xlsx"  #.\表示相对路径，当前目录下，存放测试用例


if __name__ == "__main__":  #注意==  后面的双引号
    # 一、新建遍历case类对象
    f1 = For_case1()
    # f1 = For_case1()
    # 对象调方法(这个方法中调了接口类)
    f1.for_case1(path2_case,path1_report)  #参数1-测试用例路径  参数2-测试报告路径

    #二、新建发邮件类对象
    s1 = Send_mail()
    #对象调方法
    s1.send_mail(title1,from1,to1,path1_report,content1)
    #参数1-邮件标题  参数2-发件人 参数3-收件人 参数4-测试报告路径 参数5-邮件正文
    print("邮件发送成功")























