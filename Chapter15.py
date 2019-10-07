#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time   : 2019/10/5 0005 8:51 
# @Autohor: Sam
# @File   : Chapter15.py


# 异常处理:语法异常
# print('start...')
# x = 1
# x += 1
# if
#     print('stop...')
# 结论：检测语法异常


# 异常检测
# try:
#     print('start...')
#     x = 1
#     # y
#     l = []
#     l[3]
#     d = {'a':1}
#     d['b']
#     print('end...')
# except NameError:
#     print('变量名没有定义')
# except KeyError:
#     print('字典的Key不存在')
# except IndexError:
#     print('索引超出列表的范围')
#
# print('other...')


# 修改上面代码
# try:
#     print('start...')
#     x = 1
#     # y
#     l = []
#     l[3]
#     d = {'a':1}
#     d['b']
#     print('end...')
# except (NameError, KeyError, IndexError):
#     print('变量名没有定义或字典的Key不存在或索引超出列表的范围')
#
# print('other...')
# 结论：没有严格定义异常，可以组合这些错误


# 万能异常
# try:
#     print('start...')
#     x = 1
#     # y
#     l = []
#     # l[3]
#     d = {'a':1}
#     # d['b']
#     import os
#     os.aaa
#
#     print('end...')
# except Exception:
#     print('万能异常--->')
#
# print('other...')
# 结论：万能异常虽然可以捕获所有异常，但不能清楚的知道异常的类型


# 把异常类型赋值给e
# try:
#     print('start...')
#     x = 1
#     # y
#     l = []
#     # l[3]
#     d = {'a':1}
#     # d['b']
#     import os
#     os.aaa
#
#     print('end...')
# except Exception as e:
#     print('万能异常--->', e)
#
# print('other...')
# 结论：这样又能平稳过度，又能知道异常的类型


# 继续优化
# try:
#     print('start...')
#     x = 1
#     # y
#     l = []
#     l[3]
#     d = {'a':1}
#     d['b']
#     print('end...')
# except NameError as e:
#     print('变量名没有定义', e)
# except KeyError as e:
#     print('字典的Key不存在', e)
# except IndexError as e:
#     print('索引超出列表的范围', e)
#
# print('other...')


# try...else...联用
# try:
#     print('start...')
#     # x = 1
#     # # y
#     # l = []
#     # l[3]
#     # d = {'a': 1}
#     # d['b']
#     # import os
#     # os.aaa
#     print('end...')
# except NameError as e:
#     print('NameError:', e)
#
# except KeyError as e:
#     print('KeyError', e)
#
# except Exception as e:
#     print('万能异常--->', e)
#
# else:
#     print('被检测的代码中没有出现任何异常的情况下执行')
#
# print('other...')
# 结论：没有异常，执行else


# try...finally... 组合
# try:
#     print('start...')
#     # x = 1
#     # # y
#     # l = []
#     # l[3]
#     # d = {'a': 1}
#     # d['b']
#     # import os
#     # os.aaa
#     print('end...')
# except NameError as e:
#     print('NameError:', e)
#
# except KeyError as e:
#     print('KeyError', e)
#
# except Exception as e:
#     print('万能异常--->', e)
#
# else:
#     print('被检测的代码中没有出现任何异常的情况下执行')
#
# finally:
#     print('无论有没有异常，都会执行')
#
# print('other...')
# 结论：有异常 和 无异常 都会执行 finally，
# finally的子代码通常放的是回收系统资源代码


#　主动触发异常 raise
# print(TypeError)
# obj = TypeError('类型错误')
# print(obj)
#
# class People:
#     def __init__(self, name):
#         if not isinstance(name, str):
#             raise TypeError('用户名 %s 必须是 str 类型'% name)
#         self.name = name
#
# p = People(123)
# 可以主动触发错误


# 断言 assert
# print('part1...')
# print('part1...')
# print('part1...')
# print('part1...')
# student = ['Albert', 'Harden', 'Curry', 'Wade']
# student = []
# assert len(student) > 0
# print('part2...')
# print('part2...')
# print('part2...')
# 有断言，我们可以捕获异常，停止后面的执行


# 自定义异常类
# class RegisterError(BaseException):
#     def __init__(self, message, username):
#         self.message = message
#         self.username = username
#     def __str__(self):
#         return '<%s:%s>'%(self.username, self.message)

# print(RegisterError)
# obj = RegisterError('注册失败', 'Albert')
# print(obj)
# raise RegisterError('注册失败', 'Albert')
# 结论：我们可以自定义异常类，但要记住基类是BaseException