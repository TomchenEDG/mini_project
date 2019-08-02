#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time   : 2019/8/2 0002 6:14 
# @Autohor: Sam
# @File   : Chapter03 - Data Type.py

# 不可变类型：整型int, 字符串型，元组
# 可变类型：列表



# 练习1
name ="  alberT"
# 1 移除name变量对应的值两边的空格,并输出处理结果
print(name.strip())
# 2 判断name变量对应的值是否以"al"开头,并输出结果
print('al' in name)
# 3 判断name变量对应的值是否以"T"结尾,并输出结果
print(name[-1]=='T')
# 4 将name变量对应的值中的"1"替换为"p",并输出结果
print(name.replace("l","p"))
# 5 将name变量对应的值根据"1"分割,并输出结果。
print(name.split('l'))
# 6 将name变量对应的值变大写,并输出结果
print(name.upper())
# 7 将name变量对应的值变小写,并输出结果
print(name.lower())
# 8 请输出name变量对应的值的第2个字符?
print(name[3])
# 9 请输出name变量对应的值的前3个字符?
print(name[:5])
# 10 请输出name变量对应的值的后2个字符?
print(name[-2:])
# 11 请输出name变量对应的值中"e"所在索引位置?
print(name.find('e'))
# 12 获取子序列,去掉最后一个字符。如: albert则获取alber
print(name[:7])

print('-'*100)

# # 练习2
# # 有列表 data=['albert',18,[2000,1,1]]，
# # 分别取出列表中的名字，年龄，出生的年，月，日赋值给不同的变量。
data = ['albert',18,[2000,1,1]]
name,age,born = data[0], data[1], data[2]
print('name:%s\nage:%s\nborn:%s'%(name,age,born))

print('-'*100)

# 练习3
# 有如下值集合 ：
# [11,22,33,44,55,66,77,88,99,90]，将所有大于 66 的值保存至字典的第一个key中，
# 将小于 66 的值保存至第二个key的值中，即： {'k1': 大于66的所有值, 'k2': 小于66的所有值}
k = [11,22,33,44,55,66,77,88,99,90,]
dictK = {}
strNumberK1, strNumberK2 = '', ''
for i in k:
    if i > 66:
        strNumberK2 += ','+ str(i)
    else:
        strNumberK1 += ',' + str(i)
dictK['k1'] = strNumberK1
dictK['k2'] = strNumberK2
print(dictK)

print('-'*100)

# 练习4
# 1.列表l=['a','b',1,'a','a']，列表元素均为可不可变类型，
# 去重，得到新列表，且新列表无需保持列表原来的顺序。
l = ['a','b',1,'a','a']
notRepeat_l = list(set(l))
print(notRepeat_l)
#
# # 2.在上题的基础上，保存列表原来的顺序。
for i in range(len(notRepeat_l)-1):
    if notRepeat_l[i] == 1:
        notRepeat_l[i] = str(notRepeat_l[i])
notRepeat_l.sort()
notRepeat_l[0],notRepeat_l[1] = notRepeat_l[1],notRepeat_l[0]
print(notRepeat_l)

# 3.有如下列表，列表元素为可变类型，去重，得到新列表，且新列表一定要保持列表原来的顺序
l = [{'name': 'albert', 'age' :18, 'sex':'male'},
     {'name': 'james',   'age':35,  'sex':'male'},
     {'name': 'taylor',  'age':25,  'sex':'female'},
     {'name': 'albert',  'age':18,  'sex':'male'},
     {'name': 'albert',  'age':18,  'sex':'male'},]
seenSet, new_l = set(), []
# 循环列表里的每个字典
for dict in l:
    # 将字段转换为元组
    dictToTuple = tuple(dict.items())
    # 如果元组不在集合里面，则元组添加到集合里面
    if dictToTuple not in seenSet:
        seenSet.add(dictToTuple)
        new_l.append(dict)
print(new_l)

print('-'*100)

# 练习五
# 使用至少两种方法统计字符串 s='hello albert albert say hello world world' 中每个单词的个数。
# 第一种：
s = 'hello albert albert say hello world world'
listS = s.split(' ')
countS = {}
for word in listS:
    countS[word] = countS.get(word,0) + 1
print(countS)
# 第二种：
s = 'hello albert albert say hello world world'
listS = s.split(' ')
dictS = dict.fromkeys(listS)
for key in dictS:
    dictS[key] = listS.count(key)
print(dictS)

print('-'*100)

# 练习六
# 实现简易购物程序.
# 要求如下：首先打印 商品详细信息，然后请用户输入 商品名 和 购买个数，
# 则将商品名，价格，购买个数加入购物列表，如果输入为空 或 其他非法输入则要求用户重新输入.
goodsDic = {'apple':10,
             'mac':10000,
             'iphone':8000,
             'lenovo':30000,
             'chicken':10,}
print("商品详细信息:",goodsDic)

listShoppingCart = []
# 如果输入为空 或 其他非法输入则要求用户重新输入
goodsName = input('您好，请您输入商品名：')
while goodsName not in goodsDic.keys():
    goodsName = input('输入有误，请您重新输入商品名：')
howManyGoods = input('您需要购买多少：')
while not howManyGoods.isdigit():
    howManyGoods = input('输入有误，请您重新输入所需购物数：')
# 添加商品名，价格，购买个数加入购物列表
listShoppingCart.append([goodsName, goodsDic[goodsName], howManyGoods])
print(listShoppingCart)

