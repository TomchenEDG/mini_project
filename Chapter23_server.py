#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time   : time
# @Autohor: Sam
# @File   : File


# 服务端
# from socket import *
# from threading import Thread
# def communicate(conn, client_address):
#     while True:
#         try:
#             data = conn.recv(1024)
#             if not data:break
#             conn.send(data.upper())
#         except ConnectionResetError:
#             break
#     conn.close()
# def server():
#     server = socket(AF_INET, SOCK_STREAM)
#     server.bind(('127.0.0.1', 8080))
#     server.listen(5)
#     while True:
#         conn, client_address = server.accept()
#         print(client_address)
#         t = Thread(target=communicate,args=(conn, client_address))
#         t.start()
#     server.close()
# if __name__ == '__main___':
#     server()



# 线程池改写套接字通信程序
from socket import *
from concurrent.futures import ThreadPoolExecutor
thread_pool = ThreadPoolExecutor(50)
def communicate(conn, client_address):
    while True:
        try:
            data = conn.recv(1024)
            if not data:break
            conn.send(data.upper())
        except ConnectionResetError:
            break
    conn.close()
def server():
    server = socket(AF_INET, SOCK_STREAM)
    server.bind(('127.0.0.1', 8080))
    server.listen(5)
    while True:
        conn, client_address = server.accept()
        print(client_address)
        thread_pool.submit(communicate, conn, client_address)
    server.close()
if __name__ == '__main__':
    server()