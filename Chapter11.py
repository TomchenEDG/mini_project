#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time   : 2019/8/28 0028 11:01 
# @Autohor: Sam
# @File   : Chapter11.py


# 程序中的类
# class DeepShareStudent:
#
#     school = 'deepshare'
#
#     def learn(self):
#         print('is learning')
#
#     def eat(self):
#         print('%s is eating'% self)
#
#     def sleep(self):
#         print('is sleeping')
#
#     print('==============>')

# name_and_func = DeepShareStudent.__dict__
# print(name_and_func)

# print(name_and_func['school'])
# print(name_and_func['learn'])

# name_and_func['eat']('albert')

# 调用类直接点
# DeepShareStudent.sleep('albert')

# 修改属性
# DeepShareStudent.school = '深小'
# print(DeepShareStudent.school)
#
# 添加属性
# DeepShareStudent.country = '城市'
# print(DeepShareStudent.country)
#
# 删除属性
# del DeepShareStudent.country
# print(DeepShareStudent.country)

# 调用类的同时会产生对象，我们赋值给对象就可以
# stu1 = DeepShareStudent()
# print(stu1)

# 新建__init__，__init__会自动执行
# class DeepShareStudent:
#     school = 'deepshare'
#     print('==============>')
#
#     def __init__(self):
#         print('===init run===>')
#
#     def learn(self):
#         print('is learning')
#
#     def eat(self):
#         print('%s is eating'% self)
#
#     def sleep(self):
#         print('is sleeping')
#
# DeepShareStudent()


# 不加入self运行代码就会报错
# class DeepShareStudent:
#     school = 'deepshare'
#     print('==============>')
#
#     def __init__(self, x, y, z):
#         self.NAME = x
#         self.AGE = y
#         self.GENDER = z
#         print('===init run===>')
#
#     def learn(self):
#         print('is learning')
#     def eat(self):
#         print('%s is eating'% self)
#     def sleep(self):
#         print('is sleeping')
#
# stu1 = DeepShareStudent('立体快', 18, 'male')
#
# print(stu1.NAME)
# print(stu1.learn())
