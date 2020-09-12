#!/usr/bin/env python
#-*- coding:utf-8 -*-

# 需求，按照列表中的年龄倒序排列
li1  = [{"name": '张三', 's': 68}, {'name': '李四', 's': 97}]

# 通过sorted方法排序：
s = sorted(li1, key=lambda x: x['s'], reverse=True)
print(s)  #[{'name': '李四', 's': 97}, {'name': '张三', 's': 68}]















