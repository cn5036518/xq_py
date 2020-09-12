#!/usr/bin/env python
#-*- coding:utf-8 -*-
import time
class Dog:
    pass


class Person:
    country = "中国"
    def __init__(self, name, sex, birthday):
        self.name = name
        self.sex = sex
        self.birthday = birthday

    @classmethod
    def learn(Dog):
        print(Dog)
        print(999)

    @property
    def age(self):
        return 30

Person.country = "美国"
p = Person("xue", "女", "19881009")
print(p.country)        #美国
p.country = "韩国"
print(p.country)        #韩国
print(Person.country)

print(Person.learn())

print(p.age)

