#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2019/12/24 6:59
#@author:wangtongpei
#@email: cn5036520@163.com

#6看代码写结果

class UserInfo(object):
    pass

class Department(object):
    pass

class StarkConfig(object):   #StarkConfig(UserInfo).run()
    def __init__(self, num):
        self.num = num

    def get_vals(self):
        v = [11, 22, 33]
        extra = self.extra_vals()  #注意点 pass
        if extra:
            v.extend(extra)
        return v

    def extra_vals(self):
        pass

    def run(self):
        return self.get_vals()

class RoleConfig(StarkConfig):  # RoleConfig(Department).run()
    def extra_vals(self):
        return [99, 88]

class AdminSite(object):
    def __init__(self):
        self._registry = {}

    def register(self, k, v):
        self._registry[k] = v(k)

site = AdminSite()  #self._registry = {} #1新建一个空字典
site.register(UserInfo, StarkConfig)    #2参数是两个类名
# self._registry[UserInfo] = StarkConfig(UserInfo)
#self._registry = {UserInfo:StarkConfig(UserInfo)}

site.register(Department, RoleConfig)  #3参数是两个类名
# self._registry[Department] = RoleConfig(Department)
#self._registry = {UserInfo:StarkConfig(UserInfo),Department:RoleConfig(Department)}

for k, row in site._registry.items():
    print(row.run())
    #StarkConfig(UserInfo).run()   #[11, 22, 33]
    #RoleConfig(Department).run()  #[11, 22, 33, 99, 88]












