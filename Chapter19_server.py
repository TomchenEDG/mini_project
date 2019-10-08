#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time   : 2019/10/6 0006 9:46 
# @Autohor: Sam
# @File   : Chapter19_server.py

# 服务端
# import socket
# phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# phone.bind(('127.0.0.1', 8082))
# phone.listen(5)
#
# print('start...')
# conn, client_address = phone.accept()
# print('连接来了：', conn, client_address)
#
# msg = conn.recv(1024)
# print('客户端的消息：', msg)
# conn.send(msg+b'Albert')
#
# conn.close()
# phone.close()
# 这个服务端只能通信一次，交流一次就挂电话了，我们要改进


# 改进，循环连路
# import socket
# phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# phone.bind(('127.0.0.1', 8082))
# phone.listen(5)
#
# print('start...')
# conn, client_address = phone.accept()
# print('连接来了：', conn, client_address)
#
# while True:
#     msg = conn.recv(1024)
#     print('客户端的消息：', msg)
#     conn.send(msg+b'Albert')
#
# conn.close()
# phone.close()
# 结论：可以实现循环连路，但是客户端一关闭就会奔溃，需要改进


# 改进
# import socket
# phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# phone.bind(('127.0.0.1', 8082))
# phone.listen(5)
#
# print('start...')
# conn, client_address = phone.accept()
# print('连接来了：', conn, client_address)
#
# while True:
#     try:
#         msg = conn.recv(1024)
#         print('客户端的消息：', msg)
#         conn.send(msg+b'Albert')
#     except Exception:
#         break
#
# conn.close()
# phone.close()
# 结论：虽然已经捕获异常，但是服务端还是会自己断了连接，
# 我们不能因为一个客户关闭客户端而断了服务端，因为服务端还在服务其他连接


# 继续改进
import socket
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
phone.bind(('127.0.0.1', 8082))
phone.listen(5)
print('start...')

while True:
    conn, client_address = phone.accept()
    print('客户端', client_address)
    while True:
        try:
            msg = conn.recv(1024)
            print('客户端的消息：', msg)
            conn.send(msg+b'Albert')
        except Exception:
            break

    conn.close()
phone.close()
# 结论：已正常工作了！~