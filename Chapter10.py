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
# file_path = r'a/b/c/d.txt'
# 当前目录下创建d.txt
# print(os.path.abspath(file_path))


# 分割路径 为 ('a/b/c', 'd.txt')
# res = os.path.split(r'a/b/c/d.txt')
# print(res)
# print(res[-1])
# print(res[0])


# 判断是否是绝对路径
# print(os.path.isabs(r'b/c/d.txt'))
# print(os.path.isabs(r'/Users/albert/Desktop/函数/05模块对象.py'))


# path1 = os.path.dirname(__file__)
# print(path1) # 获取当前运行脚本的绝对路径

# 返回path的目录。
# BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# DB_PATH = r'%s\db\db.txt'% BASE_DIR
#
# print(BASE_DIR)
# print(DB_PATH)

# 组合
# print(os.path.join('C:\\','a', 'b', 'a.txt'))
# print(os.path.join('C:\\', 'a', 'D:\\', 'b', 'a.txt'))
# print(os.path.join('a', 'b', 'a.txt'))

# 得到文件大小
# res = os.path.getsize(r"F:\Program Files (x86)\PyCharm 2019.1.3\JetBrains_code\untitled\venv\Scripts\3.215. Kth Largest Element in an Array(heap).py")
# print(res)

# 正则表达式
import re

# print(re.findall('\w', 'ab 12\+- *&_')) # 匹配字母数字和下划线
# print(re.findall('\W', 'ab 12\+- *&_')) # 匹配 非字母 非数字 非下划线

# print(re.findall('\s', 'ab \r1\n2\t\+- *&_')) # 匹配任意空白字符
# print(re.findall('\S', 'ab \r1\n2\t\+- *&_'))   # 匹配任意非空字符
# print(re.findall('\d', 'ab \r1\n2\t\+- *&_'))   # 匹配任意数字
# print(re.findall('\D', 'ab \r1\n2\t\+- *&_'))   # 匹配任意非数字
# print (re.findall('\w_nb', 'albert james_nb123123curry_nb, harden_nb'))

# print(re.findall('\Aalbert', 'abcalbertx is nb')) # 匹配不到
# print(re.findall('\Aalbert', 'albert is nb')) # 匹配字符串开始
# print(re.findall('^albert', 'albert is nalbertb')) #  匹配albert开头的字符串
# print(re.findall('nba$', 'albertnba is super nba alertanba')) # 匹配nba结尾
# print(re.findall('^albert$', 'albert')) # 以albert并以albert结尾
# print(re.findall('a\nc', 'a\nc a\tc alc')) # 匹配一个换行符

# 重复匹配：
# 1.代表了换行符外的任意一个字符
# print(re.findall('a.c', 'abc a1c aAc aaaaaaa\nc'))
# print(re.findall('a.c', 'abc a1c aAc aaaaaca\nc', re.DOTALL))

# 2.？:代表左边那一个字符重复0次或1次
# print(re.findall('ab?', 'a ab abb abbb abbbb abbbb abab'))

# 3.*:代表左边那一个字符出现0次或无穷次
# print(re.findall('ab*', 'a ab abb abbb abbbb abbbb a1bbbbbbb'))

# 4. + :代表左边那一个字符出现1次或无穷次
# print(re.findall('ab+', 'a ab abb abbb abbbb abbbb a1bbbbbbb'))

# 5.{m, n}:代表左边那一个字符出现m次到n次
# print(re.findall('ab?', 'a ab abb abbb abbbb abbbb'))
# print(re.findall('ab{0, 1}', 'a ab abb abbb abbbb abbbb'))
# print(re.findall('ab*', 'a ab abb abbb abbbb abbbb ab1bbbbbbb'))
# print(re.findall('ab{0,}', 'a ab abb abbb abbbb abbbb a1bbbbbbb'))
# print(re.findall('ab+', 'a ab abb abbb abbbb abbbb a1bbbbbbb'))
# print(re.findall('ab{1,}', 'a ab abb abbb abbbb abbbb a1bbbbbbb'))
# print(re.findall('ab{1,3}', 'a ab abb abbb abbbb abbbb a1bbbbbbb aabb'))

# 贪婪匹配: .* :匹配任意长度，任意的字符
# print(re.findall('a.*c', 'ac a123c aaaac a *123)()c asdfasfdsadf'))

# 非贪婪匹配： .*?
# print(re.findall('a.*?c', 'a123c456c'))

# 8.其他方法
# print(re.findall('\Aalbert', '123albert say......'))
# print(re.findall('^albert', 'albert say....'))
# print(re.search('albert', '123albert say......').group()) # 整个字符串中查找
# print(re.match('albert', '123albert say......')) # 从开头找


# 哈希
import hashlib
# 1 字符串加密
m = hashlib.md5() # md5是加密算法的一种
# m = hashlib.sha256 ()
# m = hashlib.sha512 ()
m.update('hello'.encode('utf-8'))
m.update('world'.encode('utf-8'))
m.update('Albert'.encode('utf-8'))
print('字符串md5值:', m.hexdigest()) # 9b904c5a3b6b865bf0ac9413887c375b

# 2 文件nd5值效验
# m = hashlib.md5()
# with open(r'/Users/albert/Desktop/函数/05模块对象.py', 'rb') as f:
#     for line in f:
#         m.update(line)
#     file_md5 = m.hexdigest ()
# print('文件md5值: ', file_md5)

# 3 密码加盐
# import hashlib
# pwd = 'albert1231'
# m = hashlib.md5 ()
# m.update ('天王盖地虎'.encode ('utf-8'))
# m.update(pwd.encode ('utf-8'))
# m.update ('宝塔炖蘑菇'.encode ('utf-8'))
# print ('密码md5值: ', m.hexdigest())



# import subprocess
# # subprocess用于在程序中执行系统命令
# cmd = input ('>>: ').strip() #Macos系统用ls测试, Windows系统用dir测试
#
# obj = subprocess.Popen(cmd,
#                        shell=True,
#                        stdout=subprocess.PIPE,
#                        stderr=subprocess.PIPE
#                        )
# print(obj)
#
# res1 = obj.stdout.read()    # 输出正确结果
# print('正确结果：', res1.decode('utf-8'))
#
# res2 =obj.stderr.read() # 输出错误结果
# print ('错误结果: ', res2 .decode('utf-8'))