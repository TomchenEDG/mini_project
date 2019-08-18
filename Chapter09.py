#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time   : 2019/8/16 0016 15:23 
# @Autohor: Sam
# @File   : Chapter09.py



# 1.三元表达式
# x = 11
# y = 12
# res = x if x < y else y
# print(res)

# 2. 递归最大限度
# import sys
# print(sys.getrecursionlimit())


# (1)递归
# def get_age(n):
#     if n == 1:
#         return 18
#     return get_age(n - 1) + 2
#
# print(get_age(5))

# （2）递归
# items = [1,[2,[3,[4,[5,[6,[7,[8,[9,[10,]]]]]]]]]]
# def tell(l):
#     for item in l:
#         if type(item) is not list:
#             print(item)
#         else:
#             tell(item)
#
# tell(items)


# 匿名函数 联用max min sorted
# salaries = {
#     'james':300,
#     'kd': 100,
#     'zimuge': 1000,
#     'harden': 900
# }

# def get(k):
#     return salaries[k]
# print(max(salaries, key=get))

# print(max(salaries, key=lambda x: salaries[x]))


# map reduce filter联用
# nums = [1,2,3,4,5]
#
# res = map(lambda x: x**2, nums)
# print(list(res))

# names = ['James','Harden','Curry']
# res = map(lambda x: x + ' is super star', names)
# print(list(res))

# 合并 reduce
# from functools import reduce
# #
# # res1 = reduce(lambda x, y: x + y, range(1, 101))
# # print(res1)
#
# list1 = ['Today', 'is', 'the', 'first', 'day', 'of', 'the', 'rest', 'of', 'your', 'life']
# res = reduce(lambda x, y: x + ' ' + y + ' ', list1)
# print(res)


# 过滤 filter
# ages = [18, 19, 10, 23, 99, 30]
# res = filter(lambda n: n>=30, ages)
# print(list(res))

# format 内置函数
# res = '{name}{age}{sex}'.format(sex='male',name='Albert',age=17)
# print(res)

# res = '{1} {0} {1}'.format('male', 'Albert', 17)
# print(res)


# (1 )类与format
# class Person(object):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return "This guy is %s, %s years old."%(self.name, self.age)
#
# p1 = Person('albert', 18)
# print(p1)


# (2)
# class Person(object):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return "This guy is {self.name}, {self.age} years old.".format(self=self)
#
# p1 = Person('albert', 18)
# print(p1)


# 不同点 占位形态
# c = (2,2)
# s1 = '敌人坐标:%s'%s
# print(s1)

# c = (2,2)
# s1 = '敌人坐标:{}'.format(c)
# print(s1)


# 填充
# print("{:>10}".format('18'))
# print("{:3>10}".format('18'))
# print("{:*^18}".format('18'))



# float精度调整
# print('{:.5f}'.format(3.141592563))



# 查看调用方法
# print(dir('abc'))


# 去商和余数，返回元组
# print(divmod(16, 3))


# 字符内的表达式拿出运行
# res = eval('2*3')
# print(res, type(res))
#
# res1 = eval('[1,2,3,4]')
# print(res1, type(res1))
#
# res2 = eval('{"name":"Albert", "age":18}')
# print(res2, type(res2))


# 集合
# s = {1,2,3}
# s.add(4)
# print(s)

# 不可变集合:
# frzenset:返回一个冻结的集合，冻结后集合不能再添加或删除任何元素。
# f_set = frozenset(s)
# s.add(5)


# 全局作用域 和 局部作用域的名字和值
# x = 2
# print(globals())
# print(dir(globals()['__builtins__']))
#
# def func():
#     x = 1
#     print(locals())
#
# func()



# 哈希
# print(hash('a'))
# print(hash((1,2,3,4)))



# 查看文档注释
# print(help(max))



# 2**3%3
# print(pow(2,3,3))


# l = [1,4,3,5]
# re = reversed(l)
# print(list(re))
# print(l)



# 切片对象
# sc = slice(1, 5, 2)
# l = ['a', 'b', 'c', 'd', 'e', 'f']
# print(l[sc])
#
# t = (1,2,3,4,5,6,7,8)
# print(t[sc])



# 拉链函数
# left = 'hello'
# right1 = {'x':1, 'y':2, 'z':3}
# right2 = [1,2,3,4,5]
#
# re1 = zip(left, right1)
# re2 = zip(left, right2)
#
# print(list(re1))
# print(list(re2))


# 使用列表生成式
import time

# 列表生成式
time1 = time.time()
l1 = ['egg%s'%i for i in range(1000000)]
time2 = time.time()
print(time2 - time1)

# 普通方式
time3 = time.time()
l = []
for i in range(1000000):
    l.append('egg%s'%i)
time4 = time.time()
print(time4 - time1)