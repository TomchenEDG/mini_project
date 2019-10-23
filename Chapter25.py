#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time   : time
# @Autohor: Sam
# @File   : File

# IO异步
# from concurrent.futures import ThreadPoolExecutor
# from threading import current_thread
# import time
# def task(n):
#     print('%s is running'%current_thread().name)
#     time.sleep(2)
#     return n ** 2
# def parse(obj):
#     res = obj.result()
#     print('结果是:',res)
# if __name__ == '__main__':
#     t = ThreadPoolExecutor(4)
#     for i in range(10):
#         t.submit(task, i).add_done_callback(parse)