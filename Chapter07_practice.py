#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time   : 2019/8/13 0013 17:49 
# @Autohor: Sam
# @File   : Chapter07_practice.py



# 1. 编写装饰器，为多个函数加上认证的功能（用户的账号密码来源于文件）。
# 要求：登录成功一次，后续的函数都无需再输入用户名和密码；
# 注意：从文件中读出字符串形式的字典，可以用以下方式把 字典字符串 转化成 字符串

# db_path = 'a.txt'
# login_status = {'status':False}
#
# def auth(auth_type='file'):
#     def auth2(func):
#         def wrapper(*args,**kwargs):
#             if login_status['status']:
#                 return func(*args, **kwargs)
#             if auth_type == 'file':
#                 with open(db_path, encoding='utf-8') as f:
#                     user_dic = eval(f.read())
#                 name = input('username:').strip()
#                 password = input('password').strip()
#                 if name in user_dic and password == user_dic[name]:
#                     login_status['status'] = True
#                     res = func(*args,**kwargs)
#                     return res
#                 else:
#                     print('username or password error')
#             elif auth_type == 'sql':
#                 pass
#             else:
#                 pass
#         return wrapper
#
#     return auth2
#
#
# @auth
# def index():
#     print('index')
#
# @auth(auth_type='file')
# def home(name):
#     print('welecome %s to home page' %name)
#
# # index()
# home('albert')






# 2. 编写装饰器，为多个函数加上认证功能，要求登录成功一次，
# 在超时时间内无需重复登录，超过了超时时间，则必须重新登录

# import time
# import random
#
# user_data = {
#     'user':None,
#     'login':False,
#     'now_time': time.time()
# }
#
# db_username = 'albert'
# db_password = '123'
#
# def auth(func):
#     def wrapper(*args, **kwargs):
#         passed_time = time.time() - user_data['now_time']
#
#         if user_data['user'] and passed_time < 3:
#             return func(*args, **kwargs)
#         else:
#             while True:
#                 username = input('input your username>>:').strip()
#                 password = input('input your password>>:').strip()
#                 if username == db_username and password == db_password:
#                     print('login successfully')
#                     user_data['user'] = username
#                     user_data['login'] = True
#                     user_data['now_time'] = time.time()
#                     return func(*args, **kwargs)
#                 else:
#                     print('username or password is invalid!')
#
#     return wrapper
#
# @auth
# def index():
#     print('This is index page')
#
# @auth
# def home(name):
#     print('welcome %s to home page' %name)
#
# index()
# time.sleep(random.randint(2, 4))
# home('albert')





# 3. 编写日志装饰器，实现功能：一旦某函数执行，
# 则将函数执行时间写入到日志文件中，日志文件路径可以指定。
# 注意：时间格式的获取

# import time
#
# def auth(file):
#     def wrapper(func):
#         def inner(*args, **kwargs):
#             with open(file, 'a', encoding = 'utf-8') as f:
#                 f.write('[%s]:[%s]\n'%(func.__name__, time.strftime('%Y-%m-%d %X')))
#                 return func(*args, **kwargs)
#
#         return inner
#
#     return wrapper
#
# @auth('db1.txt')
# def index():
#     print('this is my index')
#
# @add_log('db2.txt')
# def home(name):
#     print('Welcome %s to home page'% name)
#
# index()
# home('albert')

