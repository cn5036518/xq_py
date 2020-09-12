#!/usr/bin/env python

"""
一、整体思路
1、http请求类以及完成，导入请求类
2、读取excel的字段
3、将excel字段作为入参，调用http请求，获取响应数据
4、将响应数据和检查点进行比对
5、相等，写入通过和响应数据到excel
   不相等，写入不通过和响应数据到excel

二、整体结构
1、接口类
    1、通过post get或者Json Form进行判断，如何调http请求类
    2、将响应数据和检查点进行比对

三、伪代码
    1、导包
        导入接口类
        导入json
        导入open--excel包
    2、定义全局变量  url params headers 请求方法 请求类型 检查点 是否执行等
    3、接口类
        构造方法
        普通方法test
        if 请求方法=="Post" and 请求类型 =="Json":
            result1 = 调http请求类的post方法获取响应数据 --字典类型
        elif 请求方法=="Post" and 请求类型 =="Form":
            调http请求类的post方法
        elif 请求方法=="Get" :
            调http请求类的get方法
        else:
            print("请检查测试用例数据")
        if result2["error_code"] == chech_point["error_code"]
            操作excel，将通过写入指定单元格  sh1.cell(行号，列号).value="通过"
            将响应数据转换成json字符串后，写入指定单元格
    4、获取单行的excel的字段
        1、指定excel的路径path1
        2、获取指定的工作簿文件 load workbook  wb1
        3、获取指定的工作表 get sheet by name  sh1
        4、获取指定的单元格（url 请求数据 请求方法 请求类型 检查点 是否运行-continue等）
            sh1.cell(行号，列号).value
    5、读取多行的excel的字段
        1、获取最大行数 max_row
        2、for i in range(max_row)  注意行号
                url = sh1.cell(i，列号).value
                params1 = sh1.cell(i，列号).value
                method1 = sh1.cell(i，列号).value
                data_type1 = sh1.cell(i，列号).value
                check_point1 = sh1.cell(i，列号).value
                yes_no1 = sh1.cell(i，列号).value

    6、调用接口类（新建接口类对象，对象来调方法）
        每读取一行，就调用一次请求

四、注意点
1、从excel读取的字段，是json字符串，params和检查点需要转换成python的字典后使用  json.loads()
2、发送请求后，获取的响应数据是字典（http请求类的return）
    但是往excel中写入响应数据的时候，需要把字段转换成json字符串，才行  json.dumps()
3、写入excel的响应数据-json字符串的汉字乱码问
   json.dumps(Non-ascii=False)  这个non-ascii默认是True，即不显示非ascii，
   改成False即可显示汉字
4、如何保证读取行的行号就是写入行的行号
   通过for循环的i进行传递
5、写入excel的时候
    1、注意save后才能生效
    2、写入保存的时候，excel不能是打开的，否则有权限错误
6、新建对象的时候，传入参数（自动调构造方法）
    对象调方法的时候，就不用再次传入参数了

五、方法总结
1、先用写死的url params headers，调http请求类，获取响应数据
2、再从excel读取一行，获取响应数据
3、最后，遍历循环读取多行，获取响应数据

"""

















