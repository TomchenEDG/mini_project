#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time   : 2019/10/6 0006 9:52 
# @Autohor: Sam
# @File   : Chapter19_client.py

# 客户端
# import socket
#
# phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# phone.connect(('127.0.0.1', 8082))
# phone.send('你好'.encode('utf-8'))
# data = phone.recv(1024)
# print(data.decode('utf-8'))
# phone.close()
# 结论：这个只能通信一次，然后就挂电话了，需要改进


# 改进:循环连路
# import socket
#
# phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# phone.connect(('127.0.0.1', 8082))
# while True:
#     msg = input('请输入你的名字>>:').strip()
#     if msg in ['albert', 'Albert', 'mayite', '马一特']:
#         msg = '机器禁止发送，请重新输入'
#         print(msg)
#         continue
# phone.send(msg.encode('utf-8'))
# data = phone.recv(1024)
# print(data.decode('utf-8'))
# phone.close()
# 实现了循环连路，但是已关闭，服务端就跟着关闭了.


# 改进
import socket

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
phone.connect(('127.0.0.1', 8082))
while True:
    msg = input('请输入你的名字>>:').strip()
    if msg in ['albert', 'Albert', 'mayite', '马一特']:
        msg = '机器禁止发送，请重新输入'
        print(msg)
        continue
    phone.send(msg.encode('utf-8'))
    data = phone.recv(1024)
    print(data.decode('utf-8'))
phone.close()
# 结论:完成了整个socket的使用了，可以不出问题的给服务端发信息了