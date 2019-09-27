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



# 查看类型和内存地址
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
# print(stu1)
# print(type(stu1))
# print(id(stu1))
# 实验结果：stu1的类型是DeepShareStudent，stu1的类也是DeepShareStudent



# 列表也是一个类
# l1 = [1,2,3,4]
# print(type(l1))
# print(l1.append)



# 实验，类的使用
# l1 = [1,2,3,4]
# list.append(l1, 5)
# print(l1)
# 实验结果：确实可以当作类来使用



# 实验，类的使用
# l1 = [1,2,3,4]
# l2 = ['a', 'b', 'c']
# l2.append('d')
# print(l2)
# print(l1)



# 对比,跟上面的输出一样，写法不一样
# l1 = [1,2,3,4]
# l2 = ['a', 'b', 'c']
# list.append(l2, 'd')
# print(l2)
# print(l1)
# 实验结果：添加到l2的值，不会到l1



# 查看
# class Bar:
#     n = 1111
#     def __init__(self, x):
#         self.x = x
#
# obj = Bar('abc')
# print(Bar)
# print(obj.__dict__)
# print(obj.x)
# print(obj.n)



# 添加
# class Bar:
#     n = 1111
#     def __init__(self, x):
#         self.x = x
#
# obj = Bar('abc')
#
# print(Bar)
# print(obj.__dict__)
# print(obj.x)
# print(obj.n)
#
# obj.abc = 'abc' # 添加函数
# print(obj.abc)



# 修改
# class Bar:
#     n = 1111
#     def __init__(self, x):
#         self.x = x
#
# obj = Bar('abc')
#
# print(Bar)
# print(obj.__dict__)
# print(obj.x)
# print(obj.n)
#
# obj.abc = 'abc' # 添加函数
# print(obj.abc)
# obj.abc = '123' # 修改函数
# print(obj.abc)



# 删除
# class Bar:
#     n = 1111
#     def __init__(self, x):
#         self.x = x
#
# obj = Bar('abc')
#
# print(Bar)
# print(obj.__dict__)
# print(obj.x)
# print(obj.n)
#
# obj.abc = 'abc' # 添加函数
# print(obj.abc)
# del obj.abc # 删除函数


# 三个对象共享属性
# class foo:
#     count = 0
#     def __init__(self):
#         foo.count += 1
#
# obj1 = foo()
# obj2 = foo()
# obj3 = foo()
# print(obj1.count)
# 实验结果：这个写法可以记录调用次数



# 小实验
# class People:
#     def __init__(self, name, aggressivity, life_value=100):
#         self.name = name
#         self.aggressivity = aggressivity
#         self.life_value = life_value
#
#     def bite(self, enemy):
#         enemy.life_value -= self.aggressivity
#         print("""
#         人[%s]咬了一口狗[%s]
#         狗掉血[%s]
#         狗还剩血量[%s]
#         """%(self.name, enemy.name, self.aggressivity, enemy.life_value))
#
# class Dog:
#     def __init__(self, name, dog_type, aggressivity, life_vlaue):
#         self.name = name
#         self.dog_type = dog_type
#         self.aggressivity = aggressivity
#         self.life_value = life_vlaue
#
#     def bite(self, enemy):
#         enemy.life_value -=self.aggressivity
#         print("""
#         狗[%s]咬了一口人[%s]
#         人掉血[%s]
#         人还剩血量[%s]
#         """%(self.name, enemy.name, self.aggressivity, enemy.life_value))
#
# P1 = People('张二炮', 60)
# d1 = Dog('小黑', '藏獒', 200, 200)
#
# P1.bite(d1)
# d1.bite(P1)
