#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time   : time
# @Autohor: Sam
# @File   : File


# yield是线程并发的例子
# def eater(name):
#     print('%s 准备开始吃饭啦'%name)
#     food_list = []
#     while True:
#         food = yield food_list
#         print('%s 吃了 %s'%(name, food))
#         food_list.append(food)
# g = eater('albert')
# g.send(None)    # 对于表达式的yield,在使用时，第一次必须传None，g.send(None)等同于next(g)
# next(g)
# g.send('蒸羊羔')
# g.send('蒸鹿儿')
# g.send('蒸熊掌')
# g.send('烧素鸭')
# g.close() # close()之后的代码都不会发送了


# 单线程的并发
# import time
#
# def consumer():
#     while True:
#         x = yield
#         print(x)
#
# def producer():
#     g = consumer() # 造一个生成器
#     print(g)
#     a = next(g) # 相当于传None参数
#     print(a)
#     for i in range(1000):
#         b = g.send(i)   # 相当于上面的代码给他喂吃的，没有返回值，即返回值为空
#         print(b)    # 打印一下，就能够看出来这两个任务是交替执行的
#
# start = time.time()
# producer()
# stop = time.time()
# print(stop - start)
# 结论：单线程的执行


# 对比，串行和并发的效率
# 1.串行
# import time
# def task1():
#     res = 1
#     for i in range(1000000):
#         res += i
# def task2():
#     res = 1
#     for i in range(1000000):
#         res *= i
# start = time.time()
# task1()
# task2()
# stop = time.time()
# print(stop-start)
# 结果：0.11200642585754395


# 2.并行
# import time
# def task1():
#     res = 1
#     for i in range(1000000):
#         res += i
#         yield
# def task2():
#     g = task1()
#     res = 1
#     for i in range(1000000):
#         res *= i
#         next(g)
# start = time.time()
# task2()
# stop = time.time()
# print(stop-start)
# 结果：0.24201393127441406
# 证明了串行计算中，纯计算的任务比并发更快


# yield,实现单线程下的并发
# import time
# def task1():
#     res = 1
#     for i in range(1000000):
#         res += i
#         yield
#         time.sleep(10)
# def task2():
#     print('程序开始了')
#     g = task1()
#     res = 1
#     for i in range(1000000):
#         res *= 1
#         print(res)
#         next(g)
# start = time.time()
# task2()
# stop = time.time()
# print(stop-start)


# greelet模块
# from greenlet import greenlet
# import time
# def eat(name):
#     print('%s eat 1'%name)
#     # time.sleep(30) # 遇到IO不会切换
#     g2.switch('James') # 切换
#     print('%s eat 2'%name)
#     g2.switch() # 切换
# def play(name):
#     print('%s play 1'%name)
#     g1.switch() # 切换，在三个switch之间来回切换
#     print('%s play 2'%name)
# g1 = greenlet(eat) # 这里的参数只能放函数,不能传参数
# g2 = greenlet(play)
# g1.switch('Albert') # 在第一次切换的时候为任务传参
# 结论：greenlet可以来回切换线程


# gevent模块
# import gevent
# import time
# def eat(name):
#     print('%s eat 1'%name)
#     time.sleep(5) # 遇到IO会切换
#     print('%s eat 2'%name)
# def play(name):
#     print('%s play 1'%name)
#     gevent.sleep(3)
#     print('%s play 2'%name)
# g1 = gevent.spawn(eat, 'Albert')
# g2 = gevent.spawn(play, 'James')
# 结论：运行会自动结束，因为单线程下，异步提交。不等反馈结果，直接执行下一步。


# 修改
# import gevent,time
# def eat(name):
#     print('%s eat 1'%name)
#     time.sleep(5) # 遇到IO会切换
#     print('%s eat 2'%name)
# def play(name):
#     print('%s play 1'%name)
#     gevent.sleep(3)
#     print('%s play 2'%name)
# g1 = gevent.spawn(eat, 'Albert')
# g2 = gevent.spawn(play, 'James')
# gevent.sleep(10) # 让主线程多睡一会就可以了


# 继续改进：
# import gevent,time
# def eat(name):
#     print('%s eat 1'%name)
#     time.sleep(5) # 遇到IO会切换
#     print('%s eat 2'%name)
# def play(name):
#     print('%s play 1'%name)
#     gevent.sleep(3)
#     print('%s play 2'%name)
# g1 = gevent.spawn(eat, 'Albert')
# g2 = gevent.spawn(play, 'James')
# gevent.joinall([g1, g2])    # joinall的参数必须作为一个整体传入，是元组或者列表都可以
# 结论：改进完成


# 模拟I/O设备
# import gevent
# import time
# def eat(name):
#     print('%s eat 1'%name)
#     time.sleep(5)
#     print('%s eat 2'%name)
# def play(name):
#     print('%s play 1'%name)
#     time.sleep(3)
#     print('%s play 2'%name)
#
# g1 = gevent.spawn(eat, 'Albert')
# g2 = gevent.spawn(play, 'James')
# gevent.joinall([g1, g2])
# 结论：还是不能跳过I/O设备来执行程序


# 改进
# from gevent import monkey
# monkey.patch_all()
# import gevent
# import time
# def eat(name):
#     print('%s eat 1'%name)
#     time.sleep(5)
#     print('%s eat 2'%name)
# def play(name):
#     print('%s play 1'%name)
#     time.sleep(3)
#     print('%s play 2'%name)
#
# g1 = gevent.spawn(eat, 'Albert')
# g2 = gevent.spawn(play, 'James')
# gevent.joinall([g1, g2])
# 结论：还是会忽略time


# 改进
# from gevent import monkey;monkey.patch_all()
# from threading import current_thread
# import gevent
# import time
# def eat():
#     print('%s eat 1'%current_thread().name)
#     time.sleep(5)
#     print('%s eat 2'%current_thread().name)
# def play():
#     print('%s play 1'%current_thread().name)
#     time.sleep(3)
#     print('%s play 2'%current_thread().name)
#
# g1 = gevent.spawn(eat, )
# g2 = gevent.spawn(play, )
# print(current_thread().name)
# gevent.joinall([g1, g2])
# 结论：实现了协程
