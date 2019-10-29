#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time   : time
# @Autohor: Sam
# @File   : File


# 服务端
# from socket import *
#
# s = socket()
# s.bind(('127.0.0.1', 8080))
# s.listen(5)
#
# while True:
#     conn, address = s.accept()
#     print(address)
#     while True:
#         try:
#             data = conn.recv(1024)
#             if not data: break
#             print('from client msg: ', data)
#         except ConnectionResetError:
#             break
#     conn.close()


# 使用非阻塞IO模型
# from socket import *
# s = socket()
# s.bind(('127.0.0.1', 8080))
# s.listen(5)
# s.setblocking(False)
#
# while True:
#     try:
#         conn, address = s.accept()
#     except BlockingIOError:
#         print('r_list:', len(r_list))
#         print('上面的那家伙在IO， 我可以去执行其他任务了')
# 结论：开启了非阻塞IO模型


# 继续改进：
# from socket import *
# s = socket()
# s.bind(('127.0.0.1', 8080))
# s.listen(5)
# s.setblocking(False)
# r_list = []
#
# while True:
#     try:
#         conn, address = s.accept()
#         r_list.append(conn)
#     except BlockingIOError:
#         print('r_list:', len(r_list))
#         # print('上面的那家伙在IO， 我可以去执行其他任务了')
#         for cnn in r_list:
#             data = conn.recv(1024)
#             conn.send(data.upper())


# 改进
# from socket import *
# s = socket()
# s.bind(('127.0.0.1', 8080))
# s.listen(5)
# s.setblocking(False)
# r_list = []
#
# while True:
#     try:
#         conn, address = s.accept()
#         r_list.append(conn)
#     except BlockingIOError:
#         print('r_list:', len(r_list))
#         # print('上面的那家伙在IO， 我可以去执行其他任务了')
#         for cnn in r_list:
#             try:
#                 data = conn.recv(1024)
#                 conn.send(data.upper())
#             except BlockingIOError:
#                 continue
#             except ConnectionResetError:
#                 conn.close()
#                 r_list.remove(conn)

# 继续改进
# from socket import *
# s = socket()
# s.bind(('127.0.0.1', 8080))
# s.listen(5)
# s.setblocking(False)
# r_list = []
#
# while True:
#     try:
#         conn, address = s.accept()
#         r_list.append(conn)
#     except BlockingIOError:
#         print('r_list:', len(r_list))
#
#         del_conn_list = []
#         for cnn in r_list:
#             try:
#                 data = conn.recv(1024)
#                 conn.send(data.upper())
#             except BlockingIOError:
#                 continue
#             except ConnectionResetError:
#                 conn.close()
#                 del_conn_list.append(conn)
#
#         for conn in del_conn_list:
#             r_list.remove(conn)


# 改进
# from socket import *
# s = socket()
# s.bind(('127.0.0.1', 8080))
# s.listen(5)
# s.setblocking(False)
# r_list = []
#
# while True:
#     try:
#         conn, address = s.accept()
#         r_list.append(conn)
#     except BlockingIOError:
#         print('r_list:', len(r_list))
#
#         del_conn_list = []
#         for cnn in r_list:
#             try:
#                 data = conn.recv(1024)
#
#                 if not data:
#                     conn.close()
#                     del_conn_list.append(conn)
#                     continue
#
#                 conn.send(data.upper())
#             except BlockingIOError:
#                 continue
#             except ConnectionResetError:
#                 conn.close()
#                 del_conn_list.append(conn)
#
#         for conn in del_conn_list:
#             r_list.remove(conn)


# 改进
# from socket import *
# s = socket()
# s.bind(('127.0.0.1', 8080))
# s.listen(5)
# s.setblocking(False)
# r_list = []
# w_list = []
#
# while True:
#     try:
#         conn, address = s.accept()
#         r_list.append(conn)
#     except BlockingIOError:
#         print('r_list:', len(r_list))
#
#         del_conn_r_list = []
#         for cnn in r_list:
#             try:
#                 data = conn.recv(1024)
#
#                 if not data:
#                     conn.close()
#                     del_conn_r_list.append(conn)
#                     continue
#                 # conn.send(data.upper())
#                 w_list.append((conn, data.upper()))
#             except BlockingIOError:
#                 continue
#             except ConnectionResetError:
#                 conn.close()
#                 del_conn_r_list.append(conn)
#         del_conn_data_w_list = []
#         for item in w_list:
#             try:
#                 conn = item[0]
#                 data = item[1]
#                 conn.send(data)
#                 del_conn_data_w_list.append(item)
#             except BlockingIOError:
#                 continue
#         for conn in del_conn_r_list:
#             r_list.remove(conn)
#         for item in del_conn_data_w_list:
#             w_list.remove(item)


# 改进
# from socket import *
# import time
# s = socket()
# s.bind(('127.0.0.1', 8080))
# s.listen(5)
# s.setblocking(False)
# r_list = []
# w_list = []
#
# while True:
#     try:
#         conn, address = s.accept()
#         r_list.append(conn)
#     except BlockingIOError:
#
#         time.sleep(0.05)
#
#         print('r_list:', len(r_list))
#
#         del_conn_r_list = []
#         for cnn in r_list:
#             try:
#                 data = conn.recv(1024)
#
#                 if not data:
#                     conn.close()
#                     del_conn_r_list.append(conn)
#                     continue
#                 # conn.send(data.upper())
#                 w_list.append((conn, data.upper()))
#             except BlockingIOError:
#                 continue
#             except ConnectionResetError:
#                 conn.close()
#                 del_conn_r_list.append(conn)
#         del_conn_data_w_list = []
#         for item in w_list:
#             try:
#                 conn = item[0]
#                 data = item[1]
#                 conn.send(data)
#                 del_conn_data_w_list.append(item)
#             except BlockingIOError:
#                 continue
#             except ConnectionResetError:
#                 conn.close()
#                 del_conn_data_w_list.append(item)
#         for conn in del_conn_r_list:
#             r_list.remove(conn)
#         for item in del_conn_data_w_list:
#             w_list.remove(item)
# 结论：这是非阻塞的代码


# selcet方法
# import select
# from socket import *
#
# s = socket()
# s.bind(('127.0.0.1', 8080))
# s.listen(5)
#
# s.setblocking(False)
#
# r_list = [s, ]
# w_list = []
#
# while True:
#     r1, w1, x1 = select.select(r_list, w_list, [], 3)
#     print('r1:', len(r1))
#     print('w1:', len(w1))


# 改进
# import select
# from socket import *
#
# s = socket()
# s.bind(('127.0.0.1', 8080))
# s.listen(5)
#
# s.setblocking(False)
#
# r_list = [s, ]
# w_list = []
#
# while True:
#     r1, w1, x1 = select.select(r_list, w_list, [], 3)
#     print('r1:', len(r1))
#     print('w1:', len(w1))
#     for r in r1:
#         if r == s:
#             conn, address = r.accept()
#             r_list.append(conn)
#         else:
#             data = r.recv(1024)
#             r.send(data.upper())


# 改进：
# import select
# from socket import *
#
# s = socket()
# s.bind(('127.0.0.1', 8080))
# s.listen(5)
#
# s.setblocking(False)
#
# r_list = [s, ]
# w_list = []
# w_data = {}
#
# while True:
#     r1, w1, x1 = select.select(r_list, w_list, [], 3)
#     print('r1:', len(r1))
#     print('w1:', len(w1))
#     for r in r1:
#         if r == s:
#             conn, address = r.accept()
#             r_list.append(conn)
#         else:
#             try:
#                 data = r.recv(1024)
#                 if not data:
#                     r.close()
#                     r_list.remove(r)
#                     continue
#                 w_list.append(r)
#                 w_data[r] = data.upper()
#             except ConnectionResetError:
#                 r.close()
#                 r_list.remove(r)
#                 continue
#
#     for w in w1:
#         w.send(w_data[w])
#         w_list.remove(w)
#         w_data.pop(w)