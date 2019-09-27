#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time   : 2019/8/30 0030 21:51 
# @Autohor: Sam
# @File   : Chapter12.py


# 1.调用类
# class DeepShareStudent:
#     school = 'deepshare'
#
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#
#     def learn(self):
#         print('%s is learning'% self)
#
#     def eat(self):
#         print('is eating')
#
#     def sleep(self):
#         print('is sleeping')
#
# stu1 = DeepShareStudent('王小二', 18, 'male')
# print(stu1.__dict__)
# print(stu1.__dict__['name'])
# print(stu1.name)



# 2.添加一个name，让类有两个name属性
# 很明显调用类的对象后，是在init那里获得name的值
# class DeepShareStudent:
#     school = 'deepshare'
#     name = 'aaaaaaaa'
#
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#
#     def learn(self):
#         print('%s is learning'% self)
#
#     def eat(self):
#         print('is eating')
#
#     def sleep(self):
#         print('is sleeping')
#
# stu1 = DeepShareStudent('王小二', 18, 'male')
# print(stu1.name)
# print(stu1.school)
# 实验结果：对象发现自己没有school属性时，就会往类的名称空间搜索school属性，向上一层搜索



# 3.如果是类的名称空间中，还会往上找吗？
# school = 'deepshare'
# class DeepShareStudent:
#     name = 'aaaaaa'
#
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#
#     def learn(self):
#         print(' %s is learning'%self)
#
#     def eat(self):
#         print('is eating')
#
#     def sleep(self):
#         print('is sleeping')
#
# stu1 = DeepShareStudent('王小二', 18, 'male')
# print(stu1.school)
# 实验结果：肯定是不能的，school是全局，与对象stu1没有任何关系



# 打印类和对象的内存地址，查看是否一致
# class DeepShareStudent:
#     school = 'deepshare'
#
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#
#     def learn(self):
#         print(' %s is learning'%self)
#
#     def eat(self):
#         print('is eating')
#
#     def sleep(self):
#         print('is sleeping')
# stu1 = DeepShareStudent('王小二', 18, 'male')
# stu2 = DeepShareStudent('王三小', 18, 'male')
# print(DeepShareStudent.__dict__)
# print(id(DeepShareStudent.__dict__))
# print(stu1.__dict__)
# print(id(stu1.__dict__))
# print(id(stu2.__dict__))
# 我们打印了类和对象的内存地址，都是不相同的，都有自己的内存空间



# 类调用函数，对象调用函数的不同
# class DeepShareStudent:
#     school = 'deepshare'
#
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#
#     def learn(self):
#         print('is learning')
#
#     def eat(self):
#         print('is eating')
#
#     def sleep(self):
#         print('is sleeping')
#
# stu1 = DeepShareStudent('王小二', 18, 'male')
# stu2 = DeepShareStudent('汪三小', 18, 'male')
# DeepShareStudent.learn('albert')
# stu1.learn()
# 实验结果：类调用learn函数要传参，而stu1不需要传参，stu1对象自动传参



# 验证：stu1对象自动传参
# class DeepShareStudent:
#     school = 'deepshare'
#
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#
#     def learn(self):
#         print('is learning', self)
#
#     def eat(self):
#         print('is eating')
#
#     def sleep(self):
#         print('is sleeping')
#
# stu1 = DeepShareStudent('王小二', 18, 'male')
# stu2 = DeepShareStudent('汪三小', 18, 'male')
# DeepShareStudent.learn('albert')
# stu1.learn() # DeepShareStudent.learn(stu1)
# print(stu1)
#
# print(DeepShareStudent.learn)
# DeepShareStudent.learn('albert')
# 实验结果：stu1调用learn方法本质原理就是把它自己传进来



# 哪个对象来调用就会把第一次参数传给它
# class DeepShareStudent:
#     school = 'deepshare'
#
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#
#     def learn(self):
#         print('is learning', self)
#
#     def eat(self):
#         print('is eating')
#
#     def sleep(self):
#         print('is sleeping')
#
# stu1 = DeepShareStudent('王小二', 18, 'male')
# stu2 = DeepShareStudent('汪三小', 18, 'male')
# stu1.learn()
# stu2.learn()



# stu1来说明：
# class DeepShareStudent:
#     school = 'deepshare'
#
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#
#     def learn(self):
#         print('%s is learning'%self.name)
#
#     def eat(self):
#         print('is eating')
#
#     def sleep(self):
#         print('is sleeping')
#
# stu1 = DeepShareStudent('王小二', 18, 'male')
# stu2 = DeepShareStudent('汪三小', 18, 'male')
# stu1.learn()
# stu2.learn()
# 实验结果：类内部的所有变量都是给对象共享的。



# 增加函数choose
# class DeepShareStudent:
#     school = 'deepshare'
#
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#
#     def learn(self):
#         print('%s is learning'%self.name)
#
#     def choose(self, course):
#         print('%s is choosing %s '% (self.name, course))
#
#     def eat(self):
#         print('is eating')
#
#     def sleep(self):
#         print('is sleeping')
#
# stu1 = DeepShareStudent('王小二', 18, 'male')
# stu2 = DeepShareStudent('汪三小', 18, 'male')
#
# stu1.choose('Python')
# stu2.choose('AI')
# pycharm会自动生成self，self会自动传值，自动把它本身当作第一个参数传入





