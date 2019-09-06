#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time   : 2019/8/30 0030 21:51 
# @Autohor: Sam
# @File   : Chapter12.py


# 调用类
# class DeepShareStudent:
#     school = 'deepshare'
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#     def learn(self):
#         print('%s is learning'% self)
#     def eat(self):
#         print('is eating')
#     def sleep(self):
#         print('is sleeping')
#
# stu1 = DeepShareStudent('王小二', 18, 'male')
# print(stu1.__dict__)
# print(stu1.__dict__['name'])
# print(stu1.name)

# 测试使用
# class DeepShareStudent:
#     school = 'deepshare'
#     name = 'aaaaaaaa'
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#     def learn(self):
#         print('%s is learning'% self)
#     def eat(self):
#         print('is eating')
#     def sleep(self):
#         print('is sleeping')
#
# stu1 = DeepShareStudent('王小二', 18, 'male')
# print(stu1.name)
# print(stu1.school)


# 测试使用
# class DeepShareStudent:
#     school = 'deepshare'
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#     def learn(self):
#         print('is learning', self)
#     def eat(self):
#         print('is eating')
#     def sleep(self):
#         print('is sleeping')
#
# stu1 = DeepShareStudent('王小二', 18, 'male')
# stu2 = DeepShareStudent('汪小四', 18, 'male')
# DeepShareStudent.learn('albert')
# stu1.learn()
# print(stu1)


# 测试使用
# class DeepShareStudent:
#     school = 'deepshare'
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#
#     def learn(self):
#         print('%s is learning'% self.name)
#     def eat(self):
#         print('is eating')
#     def sleep(self):
#         print('is sleeping')
#
# stu1 = DeepShareStudent('王小二', 18, 'male')
# stu2 = DeepShareStudent('汪小四', 18, 'male')
# stu1.learn()
# stu2.learn()


# 测试使用
class DeepShareStudent:
    school = 'deepshare'
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def learn(self):
        print('%s is learning'% self.name)
    def choose(self, course):
        print('%s is choosing %s'%(self.name, course))
    def eat(self):
        print('is eating')
    def sleep(self):
        print('is sleeping')

stu1 = DeepShareStudent('王小二', 18, 'male')
stu2 = DeepShareStudent('汪小四', 18, 'male')

stu1.choose('Python')