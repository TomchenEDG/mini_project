#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time   : 2019/8/18 0018 12:19 
# @Autohor: Sam
# @File   : Chapter09_practice.py


# 1.将 names= ['albert', 'james', 'kobe', 'kd'] 中的名字全部变大写
names= ['albert', 'james', 'kobe', 'kd']
upper_names = [name.upper() for name in names]
print(upper_names)


# 2.将 names=['albert', 'jr_shenjing', 'kobe', 'kd'] 以shenjing结尾的名字过滤掉，然后保存剩下的名字长度
names = ['albert', 'jr_shenjing', 'kobe', 'kd']
result = [name for name in names if not name.endswith('shenjing')]
print(result)


# 3,求文件a.txt中最长的行的长度（长度按字符个数算,需要使用max函数）
with open('a.txt', encoding='utf-8') as f:
    print(max(len(line) for line in f))


# 4,文件shopping.txt内容如下,
# 商品,价格,数量
# mac, 20000, 3
# lenovo, 3000, 10
# bmw, 1000000, 10
# chicken, 200, 1
# (1)求总共花了多少钱 ?
with open('shopping.txt', encoding='utf-8') as f:
    info = [line.split(',') for line in f]
    result = (sum(int(price[1])*int(price[2]) for price in info))
    print(result)

# (2)打印出所有商品的信息，格式为[{'name': 'xxx.', 'price': 333, 'count':3}...]
with open('shopping.txt', encoding='utf-8') as f:
    name_key = ['name', 'price', 'count']
    infos = [line.split(',') for line in f]
    dict_info = list(zip(name_key, info) for info in infos)
    print(dict_info)

# (3)求单价大于10000的商品信息，格式同上
with open('shopping.txt', encoding='utf-8') as f:
    name_key = ['name', 'price', 'count']
    infos = [line.split(',') for line in f]
    dict_info = list(zip(name_key, info) for info in infos if int(info[1]) > 10000)
    print(dict_info)
