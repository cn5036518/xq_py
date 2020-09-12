#!/usr/bin/env python
#-*- coding:utf-8 -*-

# from a1_interface2 import Interface1  #导入src目录-py文件的接口类
from a1_interface2 import For_case1  #导入src目录-py文件的循环case类
from mail_excel import Send_mail  #导入发邮件文件的类

if __name__ == "__main__":  #注意==  后面的双引号
    # 五、新建遍历case类对象
    f1 = For_case1()
    # 对象调方法(这个方法中调了接口类)
    f1.for_case1()

    #六、新建发邮件类对象
    s1 = Send_mail()
    #对象调方法
    s1.send_mail("接口测试报告190402")
    print("邮件发送成功")























