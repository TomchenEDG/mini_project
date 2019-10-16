#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time   : time
# @Autohor: Sam
# @File   : File


# 用函数的方式创建线程
# from threading import Thread
# import time
# def task(name):
#     print("%s is running "% name)
#     time.sleep(3)
#
# if __name__ == '__main__':
#     t = Thread(target=task, args=('Albert', ))
#     t.start()
#     print('主线程')
# 结论：线程开销比较小


# 类创建子线程
# from threading import Thread
# import time
# class MyThread(Thread):
#     def run(self):
#         print("%s is running" % self.name)
#         time.sleep(3)
# if __name__ == '__main__':
#     t = MyThread()
#     t.start()
#     print('主线程')
# 结论：继承Thread类从而可以调用start方法


# 证明：同一进程内的多个线程同属于一个进程
# from threading import Thread
# import time
# import os
#
# def task():
#     print("%s is running //" % os.getpid())
#     time.sleep(3)
#
# if __name__ == '__main__':
#     t = Thread(target=task, )
#     t.start()
#     print('主线程', os.getpid())
# 结论：同一进程内多个线程同属于一个进程


# 同一进程内的多个线程共享该进程内的资源
# from threading import Thread
# import time
#
# x = 999
# def task():
#     global x
#     x = 1
#     time.sleep(3)
# if __name__ == '__main__':
#     t = Thread(target=task,)
#     t.start()
#     t.join()
#     print('主线程', x)
# 结论:t.join()可以让主线程等待子线程，否则就不会停止运行


# 线程对象的其他方法
# from threading import Thread, current_thread, active_count, enumerate
# import time
#
# def task():
#     print('%s is running' % current_thread().name)
#     time.sleep(3)
#
# if __name__ == '__main__':
#     t1 = Thread(target=task, name='这是一个牛逼的线程')
#     t2 = Thread(target=task,)
#     t3 = Thread(target=task,)
#     t1.start()
#     t2.start()
#     t3.start()
#     print(t1.is_alive()) # 判断这个线程是否存活
#     print(active_count()) # 查看活跃进程数量：主线程数量 + 子线程数量
#     print(enumerate()) # 把当前活跃的线程对象全部放到列表
#     print('主线程', current_thread().name)
# 结论，以上是线程一些方法


# 守护线程
# from threading import Thread, current_thread
# import time
# def task():
#     print('%s is running'%current_thread().name)
#     time.sleep(3)
# if __name__ == '__main__':
#     t1 = Thread(target=task, name='这是一个牛逼的线程')
#     t1.start()
#     print('主线程', current_thread().name)
# 结论：一般情况下，主线程会等待子线程结束才能结束


# 把子线程变成守护线程后
# from threading import Thread, current_thread
# import time
# def task():
#     print('%s is running'%current_thread().name)
#     time.sleep(3)
# if __name__ == '__main__':
#     t1 = Thread(target=task, name='这是一个牛逼的线程')
#     t1.daemon = True
#     t1.start()
#     print('主线程', current_thread().name)
# 结论：子线程编程守护线程后，主线程运行结束就会结束


# 主进程和守护进程 子进程的区别
# from multiprocessing import Process
# import time
# def foo():
#     print(123)
#     time.sleep(1)
#     print("end123")
# def bar():
#     print(456)
#     time.sleep(3)
#     print("end456")
# if __name__ == '__main__':
#     p1 = Process(target=foo)
#     p2 = Process(target=bar)
#     p1.daemon = True    # 主进程很快运行完,守护进程不会运行
#     p1.start()
#     p2.start()
#     print("----------main---------")  # 主进程代码运行完毕,守护进程就会结束
# 结论1：主进程运行结束，守护进程是不会执行的，直接结束
# 结论2：主进程运行结束，会等待子进程运行完毕之后才结束


# 主线程 与 守护线程的运行
# from threading import Thread
# import time
# def foo():
#     print(123)
#     time.sleep(1)
#     print("end123")
# def bar():
#     print(456)
#     time.sleep(3)
#     print("end456")
# if __name__ == '__main__':
#     p1 = Thread(target=foo)
#     p2 = Thread(target=bar)
#     p1.daemon = True    # 主进程很快运行完,守护进程不会运行
#     p1.start()
#     p2.start()
#     print("----------main---------")  # 主进程代码运行完毕,守护进程就会结束
# 结论1：主线程线运行完成后，再等待守护线程运行完毕，再结束整个运行
# 结论2：线程开销小，所以会先与主线程运行


# 主线程 与 非守护线程的运行
# from threading import Thread
# import time
# def foo():
#     print(123)
#     time.sleep(5)
#     print("end123")
# def bar():
#     print(456)
#     time.sleep(3)
#     print("end456")
# if __name__ == '__main__':
#     p1 = Thread(target=foo)
#     p2 = Thread(target=bar)
#     p1.daemon = True    # 主进程很快运行完,守护进程不会运行
#     p1.start()
#     p2.start()
#     print("----------main---------")  # 主进程代码运行完毕,守护进程就会结束
# 结论：主线程运行结束后再等待子线程运行结束就会关闭，不会等待守护线程


# 生成100个线程
# from threading import Thread
# import time
# x = 100
# def task():
#     global x
#     temp = x
#     time.sleep(0.1)
#     x = temp - 1
# if __name__ == '__main__':
#     start = time.time()
#     thread_list = []
#     for i in range(100):
#         t = Thread(target=task)
#         thread_list.append(t)
#         t.start()
#     for t in thread_list:
#         t.join()
#     print('主', x)
#     print(time.time() - start)
# 结论：0.1可以生成100个线程,但是数据会不安全，需加锁


# 加锁
# from threading import Thread, Lock
# import time
# mutex = Lock()
# x = 100
# def task():
#     global x
#     mutex.acquire()
#     temp = x
#     time.sleep(0.1)
#     x = temp - 1
#     mutex.release()
# if __name__ == '__main__':
#     start = time.time()
#     thread_list = []
#     for i in range(100):
#         t = Thread(target=task)
#         thread_list.append(t)
#         t.start()
#     for t in thread_list:
#         t.join()
#     print('主', x)
#     print(time.time() - start)
# 结论：加锁之后，需要10 秒


# 死锁现象
# from threading import Thread, Lock
# import time
# mutex1 = Lock()
# mutex2 = Lock()
# class MyThread(Thread):
#     def run(self):
#         self.f1()
#         self.f2()
#     def f1(self):
#         mutex1.acquire()
#         print('%s 拿到了1锁===f1'%self.name)
#         mutex2.acquire()
#         print('%s 拿到了2锁===f1'%self.name)
#         mutex2.release()
#         mutex1.release()
#     def f2(self):
#         mutex2.acquire()
#         print('%s 拿到了2锁===f2'%self.name)
#         time.sleep(0.1)
#         mutex1.acquire()
#         print('%s 拿到了1锁===f2'%self.name)
#         mutex1.release()
#         mutex2.release()
# if __name__ == '__main__':
#     for i in range(10):
#         t = MyThread()
#         t.start()
#     print('主')
# 结论：代码会出现死锁。改进需要递归锁


# 递归锁
# from threading import Thread, RLock
# import time
# mutexA = mutexB = RLock()
# class MyThread(Thread):
#     def run(self):
#         self.f1()
#         self.f2()
#     def f1(self):
#         mutexA.acquire()
#         print('%s 拿到了A锁===f1'%self.name)
#         mutexB.acquire()
#         print('%s 拿到了B锁===f1'%self.name)
#         mutexB.release()
#         mutexA.release()
#     def f2(self):
#         mutexB.acquire()
#         print('%s 拿到了B锁===f2'%self.name)
#         time.sleep(0.1)
#         mutexA.acquire()
#         print('%s 拿到了A锁===f2'%self.name)
#         mutexA.release()
#         mutexB.release()
# if __name__ == '__main__':
#     for i in range(10):
#         t = MyThread()
#         t.start()
#     print('主')
# 结论：加了递归锁之后就不会产生死锁了


# 信号量
# from threading import Thread, Semaphore, current_thread
# import time, random
# sm = Semaphore(5) # 卫生间有5个仓位
# def go_wc():
#     sm.acquire()
#     print('%s 上卫生间ing '% current_thread().getName())
#     time.sleep(random.randint(1,3))
#     sm.release()
# if __name__ == '__main__':
#     for i in range(23):
#         t = Thread(target=go_wc)
#         t.start()
# 结论：给进程先提供5个仓位，进程可以先进去五个，根据退出再进入


# 进程池
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import time, os, random
print(os.cpu_count()) #打印CPU数目

def task(x):
    print('%s is running'% os.getpid())
    time.sleep(random.randint(2, 5))
    return x ** 2
if __name__ == '__main__':
    p = ProcessPoolExecutor(max_workers=5) # 不传参数默认开启的进程数是cpu的核数
    for i in range(20):
        p.submit(task, i) # 分配任务
