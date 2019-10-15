#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time   : 2019/10/9 0009 9:55 
# @Autohor: Sam
# @File   : Chapter22.py

# 查看进程
# import time
# time.sleep(1000)


# 获取进程ID
# import time
# import os
#
# print('one:',os.getppid())
# print('two:',os.getppid())
# time.sleep(500)


# 函数建立子进程
# from multiprocessing import Process
# import time
# def task(name):
#     print('2 %s进程开始'%name)
#     time.sleep(3)
#     print('3 %s进程结束'%name)
#
# if __name__ == '__main__':
#     # target参数指定要开启的进程所要执行的任务
#     p = Process(target=task, args=('Albert',))
#     p.start()
#     print('1 这是主进程')
# 结论：这是创建进程的过程


# 多进程类
# from multiprocessing import Process
# import time
# class MyProcess(Process):
#     def __init__(self, name):
#         super(Process, self).__init__()
#         self.name = name
#     def run(self):
#         print('2 %s进程开始'%self.name)
#         time.sleep(3)
#         print('3 %s进程结束'%self.name)
# if __name__ == '__main__':
#     p = MyProcess('Albert')
#     p.start()
#     print('1 这是主进程')
# 结论：这是类创建进程的过程


# 验证进程内存空间相互隔离
# from multiprocessing import Process
# import time
# x = 10
# def task():
#     time.sleep(3)
#     global x
#     x = 0
#     print(x, '子进程结束')
# if __name__ == '__main__':
#     p = Process(target=task,)
#     p.start()
#     time.sleep(5)
#     print(x)
# 结论：确定可以隔离


# 父进程监视子进程join()
# from multiprocessing import Process
# import time
# x = 10
# def task():
#     time.sleep(3)
#     global x
#     x = 0
#     print(x, '子进程结束')
#
# if __name__ == '__main__':
#     p = Process(target=task,)
#     p.start()
#     p.join()
#     print(x)
# 结论：可以执行监视


# 制作多个进程
# from multiprocessing import Process
#
# def task(n):
#     print('%s is running'% n)
#
# if __name__ == '__main__':
#     for i in range(10):
#         p = Process(target=task, args=(i,))
#         p.start()
#     print('主进程...')
# 结论：打印不是按照顺序的，因为CPU在处理


# 让父进程等待这10个子进程结束
# from multiprocessing import Process
# import time
#
# def task(n):
#     print('%s is running'% n)
#
# if __name__ == '__main__':
#     start_time = time.time()
#     p_list = []
#     for i in range(10):
#         p = Process(target=task, args=(i,))
#         p_list.append(p)
#         p.start()
#     for p in p_list:
#         p.join()
#     print('主进程...', time.time() - start_time)


# 父进程让子进程停止运行
# from multiprocessing import Process
# import time
#
# def task(n):
#     print('%s is running'% n)
#     time.sleep(n)
#
# if __name__ == '__main__':
#     p = Process(target=task, args=(1,), name='这是个牛逼的进程')
#     p.start()
#     print(p.pid)
#     print(p.name)
#     p.terminate()
#     time.sleep(1)
#     p.join()
#     print(p.is_alive())
# 结论，父进程是可以让子进程停止运行的


# 打印几个ipd进程名称
# from multiprocessing import Process
# import time, os
#
# def task(n):
#     print('self:%s,parent:%s'%(os.getpid(), os.getpid()))
#     time.sleep(n)
#
# if __name__ == '__main__':
#     p = Process(target=task, args=(1,))
#     p.start()
#     print('子进程:', p.pid)
#     print('主进程:', os.getpid())
#     print('主进程的父进程（Pycharm进程PID）:', os.getpid())


# 设置守护进程
# from multiprocessing import Process
# import time
# def task(name):
#     print('%s is running'% name)
#     time.sleep(3)
# if __name__ == '__main__':
#     p = Process(target=task, args=(1,))
#     p.daemon = True # 把子进程变成守护进程
#     p.start()
#     print('主进程')
# 结论：守护进程就是守护主进程运行代码


# 并发与串行
# from multiprocessing import Process
# import time, random
#
# def task1():
#     print('任务1 名字是：英格拉姆')
#     time.sleep(random.randint(1, 5))
#     print('任务1 性别是：male')
#     time.sleep(random.randint(1, 5))
#     print('任务1 年龄是：22')
#     time.sleep(random.randint(1, 5))
#
# def task2():
#     print('任务1 名字是：卡戴珊')
#     time.sleep(random.randint(1, 5))
#     print('任务1 性别是：female')
#     time.sleep(random.randint(1, 5))
#     print('任务1 年龄是：25')
#     time.sleep(random.randint(1, 5))
#
# def task3():
#     print('任务1 名字是：詹姆斯')
#     time.sleep(random.randint(1, 5))
#     print('任务1 性别是：male')
#     time.sleep(random.randint(1, 5))
#     print('任务1 年龄是：34')
#     time.sleep(random.randint(1, 5))
#
# if __name__ == '__main__':
#     p1 = Process(target=task1,)
#     p2 = Process(target=task2,)
#     p3 = Process(target=task3,)
#     p1.start()
#     p2.start()
#     p3.start()
#     print('主进程')
# 结论：这样打印是会错乱的。


# 改进
# from multiprocessing import Process
# import time, random
#
# def task1():
#     print('任务1 名字是：英格拉姆')
#     time.sleep(random.randint(1, 5))
#     print('任务1 性别是：male')
#     time.sleep(random.randint(1, 5))
#     print('任务1 年龄是：22')
#     time.sleep(random.randint(1, 5))
#
# def task2():
#     print('任务1 名字是：卡戴珊')
#     time.sleep(random.randint(1, 5))
#     print('任务1 性别是：female')
#     time.sleep(random.randint(1, 5))
#     print('任务1 年龄是：25')
#     time.sleep(random.randint(1, 5))
#
# def task3():
#     print('任务1 名字是：詹姆斯')
#     time.sleep(random.randint(1, 5))
#     print('任务1 性别是：male')
#     time.sleep(random.randint(1, 5))
#     print('任务1 年龄是：34')
#     time.sleep(random.randint(1, 5))
#
# if __name__ == '__main__':
#     p1 = Process(target=task1,)
#     p2 = Process(target=task2,)
#     p3 = Process(target=task3,)
#     p1.start()
#     p1.join()
#     p2.start()
#     p2.join()
#     p3.start()
#     p3.join()
#     print('主进程')
# 结论：这个固定谁先抢到就是谁的，不合理！


# 改进 使用互斥锁
# from multiprocessing import Process, Lock
# import time, random
#
# mutex = Lock()
#
# def task1(lock):
#     lock.acquire()
#     print('任务1 名字是：英格拉姆')
#     time.sleep(random.randint(1, 5))
#     print('任务1 性别是：male')
#     time.sleep(random.randint(1, 5))
#     print('任务1 年龄是：22')
#     time.sleep(random.randint(1, 5))
#     lock.release()
#
# def task2(lock):
#     lock.acquire()
#     print('任务2 名字是：卡戴珊')
#     time.sleep(random.randint(1, 5))
#     print('任务2 性别是：female')
#     time.sleep(random.randint(1, 5))
#     print('任务2 年龄是：25')
#     time.sleep(random.randint(1, 5))
#     lock.release()
#
# def task3(lock):
#     lock.acquire()
#     print('任务3 名字是：詹姆斯')
#     time.sleep(random.randint(1, 5))
#     print('任务3 性别是：male')
#     time.sleep(random.randint(1, 5))
#     print('任务3 年龄是：34')
#     time.sleep(random.randint(1, 5))
#     lock.release()
#
# if __name__ == '__main__':
#     p1 = Process(target=task1, args=(mutex,))
#     p2 = Process(target=task2, args=(mutex, ))
#     p3 = Process(target=task3, args=(mutex, ))
#     p1.start()
#     p2.start()
#     p3.start()
#     print('主进程')
# 结论：使用互斥锁可以实现


# IPC机制，队列
# from multiprocessing import Queue
# q = Queue(3)
# q.put("1")
# q.put("2")
# q.put("3")
# print(q.get())
# print(q.get())
# print(q.get())
# print(q.get())


# 增加阻塞和超时
# from multiprocessing import Queue
#
# q = Queue(3)
# q.put("1", block=True)
# q.put("2", block=True)
# q.put("3", block=True)
# # q.put("4", block=False)
# print(q.get())
# print(q.get())
# print(q.get())


# 生产者消费者模型
import time
import random
# from multiprocessing import Process, Queue
#
# def consumer(name, q):
#     while True:
#         res = q.get()
#         time.sleep(random.randint(1, 3))
#         print('\033[46m消费者===> %s 吃了 %s\033[0m'%(name, res))
#
# def producer(name, q, food):
#     for i in range(5):
#         time.sleep(random.randint(1, 2))
#         res = '%s%s'%(food, i)
#         q.put(res)
#         print('\033[46m消费者===> %s 吃了 %s\033[0m'%(name, res))
#
# if __name__ == '__main__':
#     # 1. 共享的吧台
#     q = Queue()
#     # 2. 生存者们
#     p1 = Process(target=producer, args=('Albert主厨', q, '新疆大盘鸡'))
#     p2 = Process(target=producer, args=('厨神', q, '扬州烤鹅'))
#     p3 = Process(target=producer, args=('主厨小迷弟', q, '南京回锅肉'))
#     # 3.消费者们
#     c1 = Process(target=consumer, args=('孙悟空', q))
#     c2 = Process(target=consumer, args=('猪八戒', q))
#     p1.start()
#     p2.start()
#     p3.start()
#     c1.start()
#     c2.start()
# 这个进程会卡死，需改进


# 守护进程
import time
import random
# from multiprocessing import Process, Queue
#
# def consumer(name, q):
#     while True:
#         res = q.get()
#         time.sleep(random.randint(1, 3))
#         print('\033[46m消费者===> %s 吃了 %s\033[0m'%(name, res))
#
# def producer(name, q, food):
#     for i in range(5):
#         time.sleep(random.randint(1, 2))
#         res = '%s%s'%(food, i)
#         q.put(res)
#         print('\033[46m消费者===> %s 吃了 %s\033[0m'%(name, res))
#     q.put(None)
#
# if __name__ == '__main__':
#     # 1. 共享的吧台
#     q = Queue()
#     # 2. 生存者们
#     p1 = Process(target=producer, args=('Albert主厨', q, '新疆大盘鸡'))
#     p2 = Process(target=producer, args=('厨神', q, '扬州烤鹅'))
#     p3 = Process(target=producer, args=('主厨小迷弟', q, '南京回锅肉'))
#     # 3.消费者们
#     c1 = Process(target=consumer, args=('孙悟空', q))
#     c2 = Process(target=consumer, args=('猪八戒', q))
#
#     p1.start()
#     p2.start()
#     p3.start()
#     c1.start()
#     c2.start()
# 结论：有些事物没有显示出来，需改进


# 改进
# import time
# import random
# from multiprocessing import Process, Queue
#
# def consumer(name, q):
#     while True:
#         res = q.get()
#         time.sleep(random.randint(1, 3))
#         print('\033[46m消费者===> %s 吃了 %s\033[0m'%(name, res))
#
# def producer(name, q, food):
#     for i in range(5):
#         time.sleep(random.randint(1, 2))
#         res = '%s%s'%(food, i)
#         q.put(res)
#         print('\033[46m消费者===> %s 吃了 %s\033[0m'%(name, res))
#     q.put(None)
#
# if __name__ == '__main__':
#     # 1. 共享的吧台
#     q = Queue()
#     # 2. 生存者们
#     p1 = Process(target=producer, args=('Albert主厨', q, '新疆大盘鸡'))
#     p2 = Process(target=producer, args=('厨神', q, '扬州烤鹅'))
#     p3 = Process(target=producer, args=('主厨小迷弟', q, '南京回锅肉'))
#     # 3.消费者们
#     c1 = Process(target=consumer, args=('孙悟空', q))
#     c2 = Process(target=consumer, args=('猪八戒', q))
#
#     p1.start()
#     p2.start()
#     p3.start()
#     c1.start()
#     c2.start()
#
#     # 保证生存者生成完毕后，在队列末尾添加结束信号
#     p1.join()
#     p1.join()
#     p1.join()
#     # 有几个生成者就应该有几个结束信号
#     q.put(None)
#     q.put(None)
# 继续改进


# 继续改进
# import time
# import random
# from multiprocessing import Process, JoinableQueue
#
# def consumer(name, q):
#     while True:
#         res = q.get()
#         time.sleep(random.randint(1, 3))
#         print('\033[46m消费者===> %s 吃了 %s\033[0m'%(name, res))
#
# def producer(name, q, food):
#     for i in range(5):
#         time.sleep(random.randint(1, 2))
#         res = '%s%s'%(food, i)
#         q.put(res)
#         print('\033[46m消费者===> %s 吃了 %s\033[0m'%(name, res))
#     q.put(None)
#
# if __name__ == '__main__':
#     # 1. 共享的吧台
#     q = JoinableQueue()
#     # 2. 生存者们
#     p1 = Process(target=producer, args=('Albert主厨', q, '新疆大盘鸡'))
#     p2 = Process(target=producer, args=('厨神', q, '扬州烤鹅'))
#     p3 = Process(target=producer, args=('主厨小迷弟', q, '南京回锅肉'))
#     # 3.消费者们
#     c1 = Process(target=consumer, args=('孙悟空', q))
#     c2 = Process(target=consumer, args=('猪八戒', q))
#
#     p1.start()
#     p2.start()
#     p3.start()
#
#     c1.start()
#     c2.start()
#
#     # 保证生存者生成完毕后，在队列末尾添加结束信号
#     p1.join()
#     p1.join()
#     p1.join()
#     # 有几个生成者就应该有几个结束信号
#     q.join()
#     print('主进程结束')
# 结论:子进程还是傻傻等着吃


# 改进
# import time
# import random
# from multiprocessing import Process, JoinableQueue
#
# def consumer(name, q):
#     while True:
#         res = q.get()
#         time.sleep(random.randint(1, 3))
#         print('\033[46m消费者===> %s 吃了 %s\033[0m'%(name, res))
#         q.task_done()
#
# def producer(name, q, food):
#     for i in range(5):
#         time.sleep(random.randint(1, 2))
#         res = '%s%s'%(food, i)
#         q.put(res)
#         print('\033[46m消费者===> %s 吃了 %s\033[0m'%(name, res))
#
# if __name__ == '__main__':
#     # 1. 共享的吧台
#     q = JoinableQueue()
#     # 2. 生存者们
#     p1 = Process(target=producer, args=('Albert主厨', q, '新疆大盘鸡'))
#     p2 = Process(target=producer, args=('厨神', q, '扬州烤鹅'))
#     p3 = Process(target=producer, args=('主厨小迷弟', q, '南京回锅肉'))
#     # 3.消费者们
#     c1 = Process(target=consumer, args=('孙悟空', q))
#     c2 = Process(target=consumer, args=('猪八戒', q))
#
#     c1.daemon = True # 子进程变成守护进程
#     c2.daemon = True
#
#     p1.start()
#     p2.start()
#     p3.start()
#
#     c1.start()
#     c2.start()
#
#     # 保证生存者生成完毕后
#     p1.join()
#     p1.join()
#     p1.join()
#
#     # 生存者生产完毕后，拿到队列中肯定还有数据,直到这个数据量变为0，q.join()这行代码才算运行完毕
#     q.join()
#     print('主进程结束')