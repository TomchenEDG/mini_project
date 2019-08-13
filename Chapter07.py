#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time   : 2019/8/12 0012 17:47 
# @Autohor: Sam
# @File   : Chapter07.py

# 2..函数嵌套定义
# def func1():
#     print('from func1')
#     def func2():
#         print('from func2')
#
#     print(func2)
#     func2()
#
# func1()

# 函数在定义阶段不执行函数体内的代码
# def f1():
#     print('f1')
#
#     def f2():
#         print('f2')
#
#         def f3():
#             print('f3')
#
#         f3()
#
#     f2()
#
# f1()


# len()是内置名称空间，写代码不能覆盖内置名称空间
# len = 0
# def f1():
#     len = 1
#     def f2():
#         len = 2
#         print(len)
#     len = 3
#     f2()
#
# f1()


# 全局变量 global
# global_count = 0
#
# def global_check():
#     print(global_count)
#
# def global_modify():
#     global global_count
#     global_count += 1
#     print(global_count)
#
# global_check()
# global_modify()


# # 局部变量与它的修改
# def make_counter():
#     count = 0
#     def check_counter():
#         print(count)
#     check_counter()
#
#     def modify_counter():
#         # nonlocal count
#         # count += 1
#         print(count)
#
#     modify_counter()
#
# make_counter()


# 把函数当作变量
# def bar():
#     print('from bar')
#
# f = bar
# f()


# 把函数赋值给函数
# def bar():
#     print('from bar')
# def wrapper(func):
#     func()
# wrapper(bar)


# 全局变量x不用通过参数传递给函数
# x = 1
# def foo():
#     return x
#
# res = foo()
# print(res)


# 把函数赋值给函数
# def bar():
#     print('from bar')
# def foo(func):
#     return func
#
# f = foo(bar)
# f()


# 可以把函数当变量使用
# def get():
#     print('from get')
#
# def put():
#     print('from put')
#
# l1 = [get, put]
# print(l1)
# l1[0]()

# 尽量少用if elif
# def auth():
#     print('登录...')
#
# def register():
#     print('注册...')
#
# def check():
#     print('查看...')
#
# def transfer():
#     print('转账...')
#
# def pay():
#     print('支付...')
#
# func_dict = {
#     '1':auth,
#     '2':register,
#     '3':check,
#     '4':transfer,
#     '5':pay
# }
#
# def interactive():
#     while True:
#         print("""
#         1  登录
#         2  注册
#         3  查看
#         4  转账
#         5  支付
#         """)
#         choice = input('>=:').strip()
#         if choice in func_dict:
#             func_dict[choice]()
#         else:
#             print('非法操作')
#             break
#
# interactive()


# 局部变量x的变化
# def outer():
#     x = 1
#
#     def inner():
#         # x = 2
#         print('from inner', x)
#
#     return inner

# 打印函数地址
# f = outer()
# print(f)

# 声明全局变量不能改变x的值
# x = 3
# f()

# 函数体内也不能改变x的值
# def foo():
#     x = 4
#     f()
#
# foo()


# 但是闭包函数可以用外层函数来调用内部的函数。
# def outer():
#     name = 'Albert'
#
#     def inner():
#         print('my name is %s'% name)
#
#     return inner
#
# f = outer()
# f()

# 2.为函数体传值的两种方式
# (1) 以参数的形式的传入
# import requests
#
# def get(url):
#     response = requests.get(url)
#     print(response)
#     if response.status_code == 200:
#         print(response.text)
#
# get('https://www.baidu.com')


# (2)闭包函数的形式
# import requests
#
# def outer(url):
#     # url = 'http://www.baidu.com'
#     def get():
#         response = requests.get(url)
#         if response.status_code == 200:
#             print(response.text)
#     return get
#
# baidu = outer('https://www.baidu.com')
# python = outer('https://www.python.org')

# baidu()
# print('==============================================')
# python()



# 简化与总结闭包函数用法
# def outer(x):
#     def foo():
#         print(x)
#     return foo
#
# f_10 = outer(10)
#
# f_10()
#
# f_100 = outer(100)
# f_100()



# 装饰器的学习

# import time
# def index():
#     time.sleep(3)
#     print('welcome to index page')
#
# index()



# 版本一（只有index函数可以使用）
# import time
# def index():
#     time.sleep(3)
#     print('welcome to index page')
#
# # 开始计时
# start_time = time.time()
# index()
# end_time = time.time()
# print('run time is %s'%(end_time - start_time))



# 版本二（两个函数都可以使用，但是有大量重复代码）
# import time
# def index():
#     time.sleep(3)
#     print('welcome to index page')
#
# def home(name):
#     time.sleep(5)
#     print('welcome %s to home page'%name)
#
# start_time = time.time()
# index()
# stop_time = time.time()
# print('run time is %s'%(stop_time - start_time))
#
# start_time = time.time()
# home('Albert')
# stop_time = time.time()
# print('run time is %s'%(stop_time - start_time))



# 版本三（修改了源函数的调用方式）
import time

# def index():
#     time.sleep(3)
#     print('welcome to index page')
#
# def home(name):
#     time.sleep(5)
#     print('welcome %s to home page'% name)
#
# def wrapper(func):
#     start_time = time.time()
#     func()
#     stop_time = time.time()
#     print('run time is %s'%(stop_time - start_time))
#
# wrapper(index)


# 版本四（使用闭包函数，不修改源函数调用方式）
# import time
#
# def index():
#     time.sleep(3)
#     print('welcome to index page')
#
# def outer(func):
#     def wrapper():
#         start_time = time.time()
#         func()
#         stop_time = time.time()
#         print(stop_time - start_time)
#
#     return wrapper

# a = outer(index)
# a()
# index = outer(index)
# index()  # 等于wrapper()



# 版本五（解决原函数返回值无效）
# import time
# def index():
#     time.sleep(1)
#     print('welcome to index page')
#     return 1
#
# def outer(func):
#     def wrapper():
#         start_time = time.time()
#         res = func()
#         stop_time = time.time()
#         print(stop_time - start_time)
#         return res
#     return wrapper
#
# index = outer(index)
# res = index()
# print(res)


# 版本六：（终极版，解决有参函数和无参函数通用的问题）
# import time
#
# def index():
#     time.sleep(1)
#     print('welcome to index page')
#     return 1
#
# def home(name):
#     time.sleep(2)
#     print('welcome %s to home page'%name)
#
# def timer(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         res = func(*args, **kwargs)
#         stop_time = time.time()
#         print(stop_time - start_time)
#         return res
#
#     return wrapper

# index = timer(index)
# index()
# home = timer(home)
# home('Albert')

# home(name='Albert')
# home('Albert')
# index()




# 总结：无参装饰器模版
# def outer(func):
#     def inner(*args, **kwargs):
#         """
#         这里写装饰器逻辑
#         :param args: 任意位置参数
#         :param kwargs: 任意位置关键参数
#         :return: 一个函数对象
#         """
#         res = func(*args, **kwargs)
#         return res
#
#     return inner