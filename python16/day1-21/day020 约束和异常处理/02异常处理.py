#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/5/24 16:34

def division(a,b):
    try:
        result = a/b #如果这里出现错误，会产生一个异常对象，把这个异常对象返回给函数调用方--第12行
        return result
    except ZeroDivisionError as e:#内部产生的所有异常都会被捕获，捕获的异常会交给e
        print('0不能是除数',e)
    except FileNotFoundError as e:
        print('文件没有找到',e)
    except FileExistsError as e:
        print('文件已经存在',e)
    except Exception as e:    #所以上述没有明确捕获的错误，都在这里被统一捕获（最后兜底）
        print('其他错误',e)
    else:
        pass  #没有异常的话，就执行else；有异常就执行except
    finally:
        pass  #不管是否有异常，都会执行finally（比如关闭文件对象，关闭数据库连接）

quotient = division(10,0)   #0不能是除数 division by zero
print(quotient)
print('-----------------1')

def division2(a,b):
    print(a/b)

# division2(10,0)  #ZeroDivisionError: division by zero
print('-----------------2')
















