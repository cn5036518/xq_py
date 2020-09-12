#!/usr/bin/env python
#-*- coding:utf-8 -*-

class H1:
    def test1(self):
        result1 = a  #通过类2的对象，直接调类2的成员变量
        return result1

class H2:
    def __init__(self):
        self.b1 = 2

h1 = H2()
a = h1.b1

h1 = H1()
ret1 = h1.test1()
print(ret1)

print("---")


# class H3:
#     def __init__(self):
#         pass
#
#     def test1(self):
#         print("hah")
#
#     def test2(self):
#         print("445")
#         # H3().test1()
#         H3.test1(self)
#
# H3().test2()

#结论：成员变量














