#!/usr/bin/env python
#-*- coding:utf-8 -*-

# h1=0

class H2:
    def __init__(self):
        # self.h1 = 2
        pass

    def test(self):
        # global h1
        self.h1 = 2
        return self.h1

h11 = H2()
# ret1 = h11.test()
# print(ret1)
# print(h1)

class H1:
    def test2(self):
        # print(ret1)
        return H2().h1
h33 = H1()
print(h33.test2())














