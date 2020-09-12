#!/usr/bin/env python

"""
一、整体思路
    1、读取excel表格的字段
    2、将读取的字段作为入参，发送请求给服务器，获取响应数据
    3、将响应数据的错误码--实际结果
        和读取的检查点的错误码（预期结果）进行比对
    4、相等，写入通过和响应数据到excel表格
       不相等，写入不通过和响应数据到excel表格

二、整体结构
    1、接口类，调http请求类，先导入请求类
        接口类，通过请求方法（POST还是GET）、请求类型（json还是Form）分支来判断，调不同的http请求类的方法
    2、每读取一行，就掉一次接口类（http请求类）--for

三、伪代码
    1、导包
        导入http请求类
        导入json
        导入openpyxl
    2、请求类
        1、调用请求类方法
            通过请求方法（POST还是GET）、请求类型（json还是Form）分支来判断，调不同的http请求类的方法
        2、比对响应数据的错误码和检查点
        3、相等，写入通过和响应数据到excel
           不相等，写入不通过和响应数据到excel
    3、循环for最大行数，获取excel的字段
        每获取一行，就调用接口类一次（http请求类），发一次请求

四、注意点
    1、从excel表格读取后的字段是json字符串，请求数据和检查点都需要转换成python的字典，放入内存使用
        json.loads(params1)
    2、发送http请求给服务器后，获取的响应数据（http请求类返回的是字典），将响应数据写入excel之前，需要
        先将字典转换成json字符串才能写入 json.dumps(响应数据,ensure_ascii=False)
    3、响应数据写入excel后的汉字乱码问题
        通过json.dumps(响应数据,ensure_ascii=False)的参数2解决，默认ensure_ascii=True是不显示汉字的
        改成False后，就可以显示汉字了
    4、写入excel表后，需要保存wb1.save(path1)才能写入生效
        写入的时候，excel表格需要关闭，不能是打开的，否则会包权限错误
    5、如何确保读取的行和写入的行保持一致，最大行数没有小括号
        通过for循环的i进行传递
    6、是否运行，continnue来控制
五、步骤
    1、先将url、params1、headers1、请求方法、请求类型、检查点通过全局变量写死
    2、然后从excel读取一行，写入一行到excel
    3、最后从excel读取多行-for循环
        写入多行

"""


















