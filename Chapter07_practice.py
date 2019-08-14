#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time   : 2019/8/13 0013 17:49 
# @Autohor: Sam
# @File   : Chapter07_practice.py



# 1. 编写装饰器，为多个函数加上认证的功能（用户的账号密码来源于文件）。
# 要求：登录成功一次，后续的函数都无需再输入用户名和密码；
# 注意：从文件中读出字符串形式的字典，可以用以下方式把 字典字符串 转化成 字符串

user_dic={
    'egon':'123',
    'alex':'alex3714',
    'wupeiqi':'wu13',
    'yuanhao':'123123'
}

# 将 user_dic写入db.txt文件
with open('db.txt','w',encoding='utf-8') as f:
    f.write(str(user_dic))

with open('db.txt','r',encoding='utf-8') as f:
    res = f.read()
    # print(res,type(res)) # 字符串类型
    user_dic = eval(res)
    # print(user_dic,type(user_dic)) # 字典类型

db_path = 'db.txt'
login_dic = {
    'user': None,
    'status': False,
}

def auth(func):
    def wrapper(*args,**kwargs):
        if login_dic['user'] and login_dic['status']:
            res = func(*args, **kwargs)
            return res

        name = input('your name: ')
        password = input('your password: ')
        with open(db_path, 'r', encoding='utf-8') as f:
            user_dic = eval(f.read())

        if name in user_dic and password == user_dic[name]:
                print('login ok')
                login_dic['user']=name
                login_dic['status']=True
                res=func(*args,**kwargs)
                return res
        else:
            print('login err')
    return wrapper

@auth # auth(index)
def index():
    print('welecome to index')

@auth
def home(name):
    print('welecome %s to home page' %name)

index()
home('egon')






# 2. 编写装饰器，为多个函数加上认证功能，要求登录成功一次，
# 在超时时间内无需重复登录，超过了超时时间，则必须重新登录

# import time,random
#
# user = {'user':None,'login_time':None,'timeout':0.000003,}
#
# def timmer(func):
#     def wrapper(*args,**kwargs):
#         s1 = time.time()
#         res = func(*args,**kwargs)
#         s2 = time.time()
#         print('%s' %(s2-s1))
#         return res
#     return wrapper
#
# def auth(func):
#     def wrapper(*args,**kwargs):
#         if user['user']:
#             timeout = time.time()-user['login_time']
#             if timeout < user['timeout']:
#                 return func(*args,**kwargs)
#         name = input('name>>: ').strip()
#         password = input('password>>: ').strip()
#         if name == 'egon' and password == '123':
#             user['user'] = name
#             user['login_time'] = time.time()
#             res = func(*args,**kwargs)
#             return res
#     return wrapper
#
# @auth
# def index():
#     time.sleep(random.randrange(3))
#     print('welcome to index')
#
# @auth
# def home(name):
#     time.sleep(random.randrange(3))
#     print('welcome %s to home ' %name)
#
# index()
# home('egon')





# 3. 编写日志装饰器，实现功能：一旦某函数执行，
# 则将函数执行时间写入到日志文件中，日志文件路径可以指定。
# 注意：时间格式的获取

# import time,os
#
# def auth(logfile):
#     def deco(func):
#         if not os.path.exists(logfile):
#             with open(logfile,'w',encoding = 'utf-8') as f:
#                 pass
#         def wrapper(*args,**kwargs):
#             res = func(*args,**kwargs)
#             with open(logfile,'a',encoding = 'utf-8') as f:
#                 f.write('%s %s run'%(time.strftime('%Y-%m-%d %X'),func.__name__))
#         return wrapper
#     return deco
#
# @auth('suhao.txt')
# def index():
#     print('this is my index')
#
# index()

