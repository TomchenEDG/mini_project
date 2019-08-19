#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time   : 2019/8/18 0018 19:37 
# @Autohor: Sam
# @File   : Chapter10.py


# 查找sys.path路径包含的模块
# import sys
# print(sys.path)


# 包的使用
# import a.x1,a.y1
# #
# # a.x1.func1()
# # a.y1.func2()

# 包的绝对导入
from a import x1, y1
# x1.func1()
# y1.func2()
# print(x1.func1())
# print(y1.func2())


# 常用函数
# 1.时间戳
import time
# print(time.time())

# 2.格式化字符串
# print(time.strftime('%Y-%m-%d %H:%M:%S %p'))
# print(time.strftime('%Y-%m-%d %X %p'))

# 3.struct_ time对象
# print(time.localtime())
# print(time.localtime().tm_year)
# print((time.gmtime())) #UTC时间，北京领先8小时

# 4.了解
# print(time.localtime())

# print(time.localtime(111).tm_hour)
#
# print(time.mktime(time.localtime()))
# print(time.strftime('%Y/%m/%d',time.localtime()))
# print(time.strftime('2017/04/08', '%Y/%m/%d'))

# print(time.asctime(time.localtime()))
# print(time.ctime(123)) # ctime() 把一个时间戳（按秒计算的浮点数）转化为time.asctime()的形式。


# 打印进度条
# num = 30
# print('%s%%'%num)
#
# width = 30
# print(('[%%-%ds]'%width)%'#')
# print(('[%%-%ds]'%width)%'##')
# print(('[%%-%ds]'%width)%'###')

# 小项目，进度条显示
# def progress(percent, width=50):
#     if percent > 1:
#         percent = 1
#     show_str = ('[%%-%ds]' % width) % (int(width * percent) * '#')
#     print('\r%s %d%%' % (show_str, int(100 * percent)), end='')
#
# import time
#
# recv_size = 0
# total_size = 809700
# while recv_size < total_size:
#     time.sleep(0.1)
#     recv_size += 8096
#     percent = recv_size / total_size
#     progress(percent)



# 2.datatime模块
# import datetime
#
# print(datetime.datetime.now())
# print(datetime.datetime.now() + datetime.timedelta(days=3))
# print(datetime.datetime.now() + datetime.timedelta(days=-3))
# print(datetime.datetime.now() + datetime.timedelta(hours=3))
# print(datetime.datetime.now() + datetime.timedelta(seconds=111))

# current_time = datetime.datetime.now()
# print(current_time.replace(year=1977))
# print(datetime.date.fromtimestamp(11))


# 3.shutil 压缩文件
# import shutil
# import time
#
# ret = shutil.make_archive(
#     r"模块对象_%s" % time.strftime('%Y-%m-%d'),
#     'gztar',
#     root_dir = r"F:\Program Files (x86)\PyCharm 2019.1.3\JetBrains_code\untitled\venv\Scripts\a"
# )


# 4.logging模块
import logging

# basicConfig配置文件
# filename: 指定日志文件名
# format: 指定输出的格式和内容，format可以输出很多有用信息，如下例所示:
#  %(levelno)s: 打印日志级别的数值
#  %(levelname)s: 打印日志级别名称
#  %(pathname)s: 打印当前执行程序的路径，其实就是sys.argv[0]
#  %(filename)s: 打印当前执行程序名
#  %(funcName)s: 打印日志的当前函数
#  %(lineno)d: 打印日志的当前行号
#  %(asctime)s: 打印日志的时间
#  %(thread)d: 打印线程ID
#  %(threadName)s: 打印线程名称
#  %(process)d: 打印进程ID
#  %(message)s: 打印日志信息
# datefmt: 指定时间格式，同time.strftime()
# level: 设置日志级别，默认为logging.WARNING

# logging.basicConfig(
#     filename='access.log',
#     format='%(asctime)s - %(name)s - %(levelname)s - %(module)s: %(message)s',
#     datefmt='%Y-%m-%d %H:%M:%S %p',
#     level=20,
# )
#
# logging.debug('debug...')
# logging.info('info....')
# logging.warning('可能着火...')
# logging.error('着火啦快跑')
# logging.critical('火越烧越大')


# logging模块的四大对象

# 1.负责产生日志
# logger1 = logging.getLogger('xxx')
#
# # 2.过滤日志不常用
#
# # 3.handler 控制日志打印到文件or终端
# fh1 = logging.FileHandler(filename='a1.log',encoding='utf-8')
# fh2 = logging.FileHandler(filename='a2.log',encoding='utf-8')
# sh = logging.StreamHandler()
#
# # 4.format：控制日志的格式
# formatter1 = logging.Formatter(
#     fmt='%(asctime)s - %(name)s - %(levelname)s - %(module)s: %(message)s',
#     datefmt='%Y-%m-%d %H:%M:%S %p',
# )
#
# formatter2 = logging.Formatter(fmt='%(asctime)s - %(message)s',)
#
# # 为logger对象绑定handler
# logger1.addHandler(fh1)
# logger1.addHandler(fh2)
# logger1.addHandler(sh)
#
# # 为logger对象绑定日志格式
# fh1.setFormatter(formatter1)
# fh2.setFormatter(formatter1)
# sh.setFormatter(formatter2)
#
# # 日志级别：两层关卡，必须都通过，日志才能正常记录
# logger1.setLevel(30)
#
# fh1.setLevel(10)
# fh2.setLevel(10)
# sh.setLevel(10)
#
# # 调用logger对象下的方法,产生日志，然后交给不同的handler，控制日志记录到不同的地方
# logger1.debug('调试信息')
# logger1.info('使用中')
# logger1.warning('出错了')
# logger1.critical('问题很严重')


# 5.json与pickle序列化
# json序列化
import json

# dict = {'name':'Albert', 'age':18}
#
# with open('db1.json','wt',encoding='utf-8') as f:
#     json.dump(dict, f)

# 反序列化
# with open('db1.json', 'rt', encoding='utf-8') as f:
#     dic = json.load(f)
#     print(dic['name'])


# pickle序列化
import pickle
# #
# s = {1,2,3,4,}
# res = pickle.dumps(s)
# print(res, type(res))
#
# with open('db2.pkl', 'wb') as f:
#     f.write(res)
# #
# # # 它的反序列化
# with open('db2.pkl', 'rb') as f:
#     data = f.read()
#     s = pickle.load(data)
#     print(s, type(s))

# dump与load
# s = {1,2,3}
# with open('db1.pkl', 'wb') as f:
#     pickle.dump(s, f)
#
# with open('db1.pkl', 'rb') as f:
#     s = pickle.load(f)
#     print(s, type(s))


# 6.os模块
import os

# 获取当前位置
# res = os.getcwd()
# print(res)

# 获取当前位置的文件名，包括后缀
# res = os.listdir('.')
# print(res)

# 打印斜杠
# print(os.sep)

# 打印\r\n
# print([os.linesep, ])

# 打印冒号
# print(os.pathsep)

# 执行系统命令'ls'(MacOS系统)，windows用'dir'命令
# print(os.system('dir'))


# os.path系列
file_path = r'a/b/c/d.txt'



