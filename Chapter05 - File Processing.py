#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time   : 2019/8/2 0002 16:04 
# @Autohor: Sam
# @File   : Chapter05 - File Processing.py
# 在txt文件头的作用：告诉 Python解释器 用指定的字符编码去读取文件内容。
# 在 Pycharm 中，当我指定好了读取文件的字符编码，它会自动改变保存写入到硬盘的字符编码,




# r'a.txt'中的 r 代表只读模式
# 如果不指定字符编码，默认打开文件的字符编码与操作系统相匹配.
# 因为我是window，所以默认和电脑的字符编码一致：gbk
# f = open(r'a.txt', mode='r')
# data = f.read()
# print(data)
# f.close()
# # 应用程序的资源还在
# print(f)
# print()
#
# # 因为会遗漏close()关闭文件，最好使用with
# with open('a.txt', mode='r') as f:
#     data = f.read()
#     print(data)
#
#
# # 't'模型的文件的操作
# with open('a.txt', mode='r') as f:
#     # 判断是否可读
#     print(f.readable())
#     # 全部读取
#     print(f.read())
#     # 读文件会有一个光标移动，第一次读完了,光标移至末尾，第二次读无内容
#     print('-'*45)
#     print(f.read())
#
#
# # 一行一行读文件内容使用readline
# with open('a.txt', mode='r') as f:
#     print(f.readline(), end='')
#     print(f.readline(), end='')
#     print(f.readline(), end='')
#
#
#
# # 全部读取文件内容,存入列表.
# with open('a.txt', mode='r') as f:
#     print(f.readlines())
#
#
#
# # 建议使用f，f是迭代对象
# with open('a.txt', mode='r') as f:
#     for line in f:
#         print(line,end='')
#
#
# # t 模式下的 w，文件存在时，清空文件内容。
# # 当文件不存在时,就会创建空文档,
# with open('a.txt', 'w') as f:
#     f.write('你好')
#
#
#
# # 只写模式常用的方法:
# with open(r'a1.txt', mode='w') as f:
#     # 检查文件是否可写
#     print(f.writable())
#     # writelines指的是可以放一个列表或者元组，里面可以有多行内容，需要自己加换行符
#     f.writelines(['111111\n', '222222\n', '333333\n'])
#     # 下面这样代码与上面写的结果一样
#     f.write('aaaaaa\nbbbbbbb\ncccccc\n')
#
#
# # 只写模式常用的方法:
# with open(r'a1.txt', mode='w') as f:
#     # 检查文件是否可写
#     print(f.writable())
#     # 检查文件是否可读
#     print(f.readable())
#     f.write('22323232\n')
#
#
#
# # 'b'模式下的文件操作
#
# # 't'模式下无法读取图片
# with open('1.png', 'r') as f:
#     f.read()
#
# # 以 二进制 打开.
# with open('1.png', 'rb') as f:
#     data = f.read()
#     print(data)
#
# # 1、与模式类似,不能单独使用,必须是rb, wb, ab.
# # 2、b模式下读写都是以bytes单位的
# # 3、b模式下一定不能指定encoding参数,不指定encoding参数默认为二进制
# # 4、b模式(二进制)可以读取文字,图片,视频,什么文件都可以(因为所有类型的数据都要以二进制形式存在硬盘中)
#
#
# # rb模式：只读
# with open('1.jpg', 'rb') as f:
#     data = f.read()
#     print(data.decode('gbk'))
#
#
# # rw模式：只写
# with open ('a.txt', 'wb') as f:
#     msg = '你好,世界'
#     f.write(msg.encode('utf-8')) # 指定写入文件的字符编码
#
#
# # b模式写入文件
# with open ('a.txt', 'wb') as f:
#     msg = '你好,世界'
#     f.write(msg.encode('utf-8')) # 指定写入文件的字符编码
#
# # ab模式写入文件
# with open ('a.txt', 'ab') as f:
#     msg = '\n世界:你也好,小鬼'
#     f.write(msg. encode('utf-8')) # 指定写入文件的字符编码
#
#
# # 小模块，获取当前文件的地址
# import sys
# list_test = sys.argv
# print(list_test)
#
# # 光标移动
# with open('a.txt', 'r') as f:
#     f.seek(2) # 这个参数指的是偏移量,以字节为单位
#     data =f.read()
#     print(data)
#
# # 删除文件
# import os #首先导入这个模块
# os.rename('a.txt', 'b.txt') # 修改文件名,两个参数分别为源文件名和目标文名
# os.remove( 'al.txt') # 删除a1.txt文件,这个参数指的是文件路径!




# '-------------------------------------------------------------------------------------------------------'





# 练习一:
# 写一个程序在要保持文件内容的顺序不变的前提下，去除文件中重复的行。






