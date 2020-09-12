#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/8/20 17:43


# 5、使用os模块创建如下目录结构
# # glance
# # ├── __init__.py
# # ├── api
# # │   ├── __init__.py
# # │   ├── policy.py
# # │   └── versions.py
# # ├── cmd
# # │   ├── __init__.py
# # │   └── manage.py
# # └── db
# #      ├── __init__.py
# #      └── models.py

import os

# os.mkdir('glance')
# os.chdir('glance')
# print(os.getcwd())

# os.makedirs('glance/__init__.py')

os.makedirs('glance/api')
os.chdir('glance/api')
print(os.getcwd())
open('__init.py',mode='w',encoding='utf-8')
open('policy.py',mode='w',encoding='utf-8')
open('versions.py',mode='w',encoding='utf-8')

os.chdir('..')  #相对路径
os.makedirs('cmd')
os.chdir('./cmd')  #相对路径
print(os.getcwd())
open('__init.py',mode='w',encoding='utf-8')
open('manage.py',mode='w',encoding='utf-8')

os.chdir('..')  #相对路径
os.makedirs('db')
os.chdir('./db')  #相对路径
print(os.getcwd())
open('__init.py',mode='w',encoding='utf-8')
open('models.py',mode='w',encoding='utf-8')

os.chdir('../..')  #相对路径
print(os.getcwd())
open('__init.py',mode='w',encoding='utf-8')














