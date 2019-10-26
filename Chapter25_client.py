#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time   : time
# @Autohor: Sam
# @File   : File

#　客户端
from socket import *

client = socket()
client.connect(('127.0.0.1', 8082))

while True:
    data = input('>>:').strip()
    if not data: continue
    client.send(data.encode('utf-8'))
    res = client.recv(1024)
    print(res.decode('utf-8'))


# 改进
from socket import *
import os

client = socket()
client.connect(('127.0.0.1', 8082))

while True:
    data = '%s say hello'%os.getpid()
    if not data: continue
    client.send(data.encode('utf-8'))
    res = client.recv(1024)
    print(res.decode('utf-8'))

