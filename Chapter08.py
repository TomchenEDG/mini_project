#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time   : 2019/8/15 0015 16:03 
# @Autohor: Sam
# @File   : Chapter08.py


# (1)迭代
# dict1 = {'x':1, 'y':2}
# n = 0
# for i in dict1:
#     if n < len(dict1):
#         print(dict1[i])
#     n += 1



# (2)迭代器 字典
# dict1 = {'x':1, 'y':2, 'z':3}
# iter_dict1 = dict1.__iter__()
#
# print(iter_dict1.__next__())
# print(iter_dict1.__next__())
# print(iter_dict1.__next__())
# # print(iter_dict1.__next__()) # 这里就会停止迭代


# (3)迭代器 集合
# set1 = {'a', 'b', 'c'}
# iter_set1 = set1.__iter__()
#
# print(iter_set1.__next__())
# print(iter_set1.__next__())
# print(iter_set1.__next__())


# yield 构建迭代器
# def test_yield():
#     print('============>first')
#     yield 1
#     print('============>second')
#     yield  2
#     print('============>third')
#     yield  3
#
# res = test_yield()
#
# print(res)
# print(res.__iter__() is res)
# print(res.__next__())
# print(res.__next__())
# print(res.__next__())


# 自定义range
# def show_my_range(start, stop, step=1):
#     n = start
#     while n < stop:
#         yield n
#         n += step
#
# for item in show_my_range(1, 10):
#     print(item)



# 关于yield 相关操作
# def eat(name):
#     print('【1】 %s is ready for eating'%name)
#     while True:
#         food = yield
#         print('【2】%s starts to eat %s'%(name, food))
#
# personl = eat('Albert')
# personl.__next__()
# # personl.__next__()
# personl.send('猪油膏')
# personl.send('红魔系')
# personl.close() # 关闭后后面不能传值
# personl.send('谁说的')

# yield 生成器
# def test_yield():
#     print('first')
#     yield 1
#     print('second')
#     yield 2
#     print('third')
#     yield 3
#
# res = test_yield()
# print(res)
# print(res.__iter__() is res)
# print(res.__next__())
# print(res.__next__())
# print(res.__next__())
# print(res.__next__())

# 自定义range
# def show_my_range(start, stop, step=1):
#     n = start
#     while n < stop:
#         yield n
#         n += step
#
# for item in show_my_range(1, 10, 3):
#     print(item)


# yield 两个小项目
# 1.
# def eat(name):
#     print('[1] %s is ready for eating'%name)
#     while True:
#         food = yield
#         print('[2] %s starts to eat %s'%(name, food))
#
# person1 = eat("Albert")
#
# # person1.__next__()
# # person1.__next__()
#
# person1.send(None)
# person1.send('蒸羊')
# person1.send('熊掌')
# person1.close()
# person1.send('烧鹅')
# person1.send('烧鸡')


# 2.
# def eat(name):
#     print('%s is ready for eating'%name)
#     food_list = []
#     while True:
#         food = yield food_list
#         print('%s starts to eat %s'%(name, food))
#         food_list.append(food)
#
# name = 'Albert'
#
# person1 = eat(name)
# person1.send(None)
# res1 = person1.send('蒸羊')
# print('%s has eaten %s'%(name, res1))
#
# res2 = person1.send('蒸鹿')
# print('%s has eaten %s'%(name, res2))
#
# res3 = person1.send('蒸鹿')
# print('%s has eaten %s'%(name, res3))
#
# res4 = person1.send('蒸鹿')
# print('%s has eaten %s'%(name, res4))
#
# person1.close()
# person1.send('烧鹅')


