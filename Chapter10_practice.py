#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time   : 2019/8/19 0019 22:03 
# @Autohor: Sam
# @File   : Chapter10_practice.py


# 1,文件内容如下,标题为:姓名,性别,年纪薪资
# albert male 18 3000
# james male 38 30000
# 林志玲female 28 20000
# 新垣结衣female 28 10000
# 要求从文件中取出每一条记录放入列表中,列表的每个元素都是如下格式:
# {'name':'albert','sex': 'male', 'age':18, 'salary':3000}
# with open('info.txt', encoding='utf-8') as f:
#     list_info = []
#     for line in f:
#         data_info = line.split(' ')
#         name,sex = data_info[0], data_info[1]
#         age, salary = data_info[2], data_info[3]
#         people = {'name': name, 'sex': sex,
#                   'age': int(age), 'salary': int(salary)}
#         list_info.append(people)



# 2,根据题目1得到的列表, 取出薪资最高的人的信息
# print(max(list_info, key=lambda x: x['salary']))

# 3,根据题目1得到的列表,取出最年轻的人的信息
# print(min(list_info, key=lambda x: x['age']))

# 4,根据题目1得到的列表,将每个人的信息中的名字映射成首字母大写的形式
# res2 = map(lambda x: x['name'].capitalize(), list_info)
# print(list(res2))

# 5,根据题目1得到的列表,过滤掉名字以a开头的人的信息
# print(list(filter(lambda x: not x['name'].startswith('a'), list_info)))



# 6,使用递归打印斐波那契数列(前两个数的和得到第三个数,如: 0112358..)
# def Fibonacci(n):
#     if n < 1:
#         return
#     elif n == 1:
#         return 1
#     elif n == 2:
#         return 1
#     else:
#         return Fibonacci(n - 1) + Fibonacci(n - 2)
#
# for i in range(1, 20):
#     print(Fibonacci(i))



# 7,使用random模块写一个随机生成8位验证码的程序,验证码中有随机大小写字母和数字
# import random
#
# def get_verification():
#     verification_code = ''
#     for i in range(8):
#         alpha1 = chr(random.randint(65, 90))
#         alpha2 = chr(random.randint(97, 122))
#         number = random.randint(0, 9)
#         verification_code += random.choice([alpha1, alpha2, str(number)])
#     return verification_code
#
# print(get_verification())


# 8,写一个模拟撞库的程序, 假如密码都是用md5加密的,没有加盐,
# 撞库就是用多个猜测的密码是尝试比对正确的密码,比对过程一定是用md5来进行。
# import random
# import hashlib
#
#
# def get_password_violently():
#     while True:
#
#         password = ''
#
#         # imagine password is formed by 4 numbers or alphas
#         for i in range(4):
#             random_alpha = chr(random.randint(65, 90))
#             random_number = random.randint(0, 9)
#             password += random.choice([random_alpha, str(random_number)])
#
#         # md5 processing...
#         m = hashlib.md5()
#         m.update(password.encode('utf-8'))
#         md5_password = m.hexdigest()
#
#         all_alpha_number = list(map(lambda x: chr(x), range(48, 122)))
#
#         # simulate user input password
#         for a in all_alpha_number:
#             for b in all_alpha_number:
#                 for c in all_alpha_number:
#                     for d in all_alpha_number:
#                         input_password = a + b + c + d
#
#                         m = hashlib.md5()
#                         m.update(input_password.encode('utf-8'))
#                         input_md5_password = m.hexdigest()
#
#                         if input_md5_password == md5_password:
#                             return password
#
#
# res = get_password_violently()
# print("user's password", res)


# 9,使用re模块写一个验证手机号码是否有效的程序
# 首先准备了一个通讯录文件,嫩模联系方式txt,以下是文件内容:
# 姓名 地区 身高 体重 电话
# 况咏蜜 北京 171 48 11151054608
# 王心颜 上海 169 46 13813234424
# 马纤羽 深圳 173 50 13723452325
# 乔亦菲 广州 172 52 15823423525
# 罗梦竹 北京 175 49 38623423421
# 刘诺涵 北京 170 48 22623423765
# 岳妮妮 深圳 177 54 18835324553
# 贺婉萱 深圳 174 52 10933434452
# 叶梓萱 上海 171 49 16742432324
# 杜姗姗 北京 167 49 13324523342
# 我们按照中国大陆的手机号标准来比对验证, 输出有效的号码, 你有兴趣也可以打过去了解一下。
# import re
#
# def get_model_phone(file):
#     invalid_data = {}
#     with open(file, 'r', encoding='utf-8') as f:
#         for line in f:
#             model_data_list = line.split()
#             name = model_data_list[0]
#             phone = model_data_list[-1]
#             valid_phone = re.findall('13\d\d\d\d\d\d\d\d\d', phone)
#             if valid_phone:
#                 invalid_data[name] = valid_phone[0]
#         return invalid_data
#
# res = get_model_phone('info.txt')
# print(res)


