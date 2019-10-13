#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time   : 2019/10/6 0006 10:53 
# @Autohor: Sam
# @File   : Chapter20_client.py


# 客户端
# from socket import *
# client = socket(AF_INET, SOCK_STREAM)
# client.connect(('127.0.0.1', 8082))
#
# while True:
#     cmd = input('>>>:').strip()
#     if not cmd:continue
#     client.send(cmd.encode('utf-8'))
#     res = client.recv(102400)
#     print(res.decode('utf-8'))
# client.close()


# 客户端：
# from socket import *
# import time
# client = socket(AF_INET, SOCK_STREAM)
# client.connect(('127.0.0.1', 8080))
#
# client.send(b'hello')
# client.send(b'world')
#
# client.close()
# 结论：会粘包


# 改进：
from socket import *
import time
# client = socket(AF_INET, SOCK_STREAM)
# client.connect(('127.0.0.1', 8080))
#
# client.send(b'hello')
# time.sleep(1)
# client.send(b'world')
#
# client.close()
# 结论：还是会粘包


# UDP通信
# 客户端
# import socket
# client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# while True:
#     msg = input('>>>:').strip()
#     client.sendto(msg.encode('utf-8'),('127.0.0.1', 8080))
#     res, server_addr = client.recvfrom(1024)
#     print(res.decode('utf-8'))


# UDP协议不粘包
# 客户端
# import socket
# client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# client.sendto(b'hello', ('127.0.0.1', 8080))
# client.sendto(b'world', ('127.0.0.1', 8080))
# client.sendto(b'albert',('127.0.0.1', 8080))
