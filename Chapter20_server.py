#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time   : 2019/10/6 0006 10:39 
# @Autohor: Sam
# @File   : Chapter20_server.py


# subprocess模块 远程控制代码
# 服务端
# from socket import *
# import subprocess
# server = socket(AF_INET, SOCK_STREAM)
# server.bind(('127.0.0.1', 8082))
# server.listen(5)
# print('start...')
#
# while True:
#     conn, client_address = server.accept()
#     print(client_address)
#     while True:
#         try:
#             cmd = conn.rece(1024)
#             obj = subprocess.Popen(cmd.decode('utf-8'),
#                                    shell=True,
#                                    stdout=subprocess.PIPE,
#                                    Stderr=subprocess.PIPE)
#             stdout = obj.stdout.read()
#             stderr = obj.stderr.read()
#
#             conn.send(stdout)
#             conn.send(stderr)
#         except ConnectionAbortedError:
#             break
#     conn.close()
# server.close()



# 字节长度，可以打印
# from socket import *
# import subprocess
# server = socket(AF_INET, SOCK_STREAM)
# server.bind(('127.0.0.1', 8082))
# server.listen(5)
# print('start...')
#
# while True:
#     conn, client_address = server.accept()
#     print(client_address)
#     while True:
#         try:
#             cmd = conn.rece(1024)
#             obj = subprocess.Popen(cmd.decode('utf-8'),
#                                    shell=True,
#                                    stdout=subprocess.PIPE,
#                                    Stderr=subprocess.PIPE)
#             stdout = obj.stdout.read()
#             stderr = obj.stderr.read()
#
#             #打印字节长度
#             print(len(stdout +_stderr))
#
#             conn.send(stdout)
#             conn.send(stderr)
#         except ConnectionAbortedError:
#             break
#     conn.close()
# server.close()


# 验证Nagle算法
# from socket import *
# server = socket(AF_INET, SOCK_STREAM)
# server.bind(('127.0.0.1', 8080))
# server.listen(5)
#
# conn, client_address = server.accept()
#
# res1 = conn.recv(1024)
# print('第一次：', res1)
# res2 = conn.recv(1)
# print('第二次：', res2)
#
# conn.close()
# server.close()
# 结论，会粘包


# 改进
# from socket import *
# server = socket(AF_INET, SOCK_STREAM)
# server.bind(('127.0.0.1', 8080))
# server.listen(5)
#
# conn, client_address = server.accept()
#
# res1 = conn.recv(1024)
# print('第一次：', res1)
# res2 = conn.recv(1)
# print('第二次：', res2)
#
# conn.close()
# server.close()
# 结论：还是会粘包


# 改进
# from socket import *
# server = socket(AF_INET, SOCK_STREAM)
# server.bind(('127.0.0.1', 8080))
# server.listen(5)
#
# conn, client_address = server.accept()
#
# res1 = conn.recv(5)
# print('第一次：', res1)
# res2 = conn.recv(5)
# print('第二次：', res2)
#
# conn.close()
# server.close()
# 结论，这个解决办法可以


# struct使用
# import struct
# res1 = struct.pack('i', 1231)
# res2 = struct.pack('i', 1)
# res3 = struct.pack('i', 1473985)
#
# print(res1, len(res1))
# print(res2, len(res2))
# print(res3, len(res3))

# res4 = struct.unpack('i', res3)
# print(res4)


# UDP接口
# 服务端
# import socket
# server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# server.bind(('127.0.0.1', 8080))
# while True:
#     client_data, client_addr = server.recvfrom(1024)
#     msg = input('回复%s:%s>>>:hello'%(client_addr[0], client_addr[1]))
#     server.sendto(msg.encode('utf-8'), client_addr)


# UPD服务端
# 验证不粘包
# import socket
# server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# server.bind(('127.0.0.1', 8080))
# res1, client_addr = server.recvfrom(512)
# print(res1)
# res2, client_addr = server.recvfrom(512)
# print(res2)
# res3, client_addr = server.recvfrom(512)
# print(res3)
# 改进
# import socket
# server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# server.bind(('127.0.0.1', 8080))
# res1, client_addr = server.recvfrom(1)
# print(res1)
# res2, client_addr = server.recvfrom(2)
# print(res2)
# res3, client_addr = server.recvfrom(3)
# print(res3)