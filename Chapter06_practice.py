#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time   : 2019/8/9 0009 16:19 
# @Autohor: Sam
# @File   : Chapter06_practice.py


# 1.写函数，用户传入修改的文件名，与要修改的内容，执行函数，完成批了修改操作。
def modify_file(filename,old,new):
    """
    根据文件名找到文件路径，打开文件后逐行换成新的内容放到新文件，然后删除旧文件。
    :param filename: 文件名
    :param old: 旧内容
    :param new: 新内容
    :return: 无返回
    """
    import os
    with open(filename,'r',encoding='utf-8') as read_f,\
        open('.bak.swap','w',encoding='utf-8') as write_f:
        for line in read_f:
            if old in line:
                line=line.replace(old,new)
            write_f.write(line)
    os.remove(filename)
    os.rename('.bak.swap',filename)



# 2.写函数，计算传入字符串中【数字】、【字母】、【空格] 以及 【其他】的个数.
def count_sort(String):
    """
    统计任意字符里面的数字、字符、空格、其他的个数。
    :param String:任意字符串
    :return: [数字，字母，空格，其他]
    """
    num,alpha,spac,other =0,0,0,0
    for i in String:
        if i.isdigit():
            num += 1
        elif i.isalpha():
            alpha += 1
        elif i.isspace():
            spac += 1
        else:
            other += 1
    return [num, alpha, spac, other]



# 3.	写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5。
def morethan_five(data):
    """
    判断所输入的（字符串、列表、元组）长度是否大于5
    :param data: 任意一个字符串、列表、元组
    :return: 无
    """
    lenth = len(data)
    if lenth > 5:
        print("该数据大于5")



# 4.	写函数，检查传入列表的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
def check_length(list_input):
    """
    如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
    :param list_input: 需要检查的列表
    :return: 返回前两个长度的内容
    """
    if len(list_input) > 2:
        return list_input[:2]



# 5.写函数，检查 获取传入 列表 或 元组 对象的所有奇数位索引对应的元素，
# 并将其作为新列表返回给调用者。
def check_odd(data_input):
    """
    获取 列表 或 元组 对象的所有奇数位索引对应的元素
    :param data_input: 列表 或 元组
    :return: 所有奇数位索引对应的元素
    """
    if type(data_input) is list:
        tuple_odd = []
        for i in range(1,len(data_input),2):
            tuple_odd += [data_input[i],]
        return tuple_odd

    else:
        tuple_odd = ()
        for i in range(1, len(data_input), 2):
            tuple_odd += (data_input[i],)
        return tuple_odd

# 6.	写函数，检查字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
def check_dict(input_dict):
    """
    检查字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容
    :param input_dict: 检查字典
    :return:如果大于2返回前两个长度的内容
    """
    if len(input_dict.values()) > 2:
        new_dict = {}
        i = 0
        for key, value in input_dict.items():
            new_dict[key] = value
            i += 1
            if i == 2:
                break
    else:
        return
    return new_dict







# 7.	用函数改写第一阶段购物项目
import os

product_list = [
    ['IphoneXR', 9800],
    ['Coffee', 30],
    ['Mac Pro 2019', 25000],
    ["Albert's Python Book", 99],
    ['Bike', 199],
    ['ViVo X20', 2499],
]

shopping_cart = {}
current_user_info = []

db_file = r'db.txt'

def strat_run():
    print('''
    1：Register
    2：Login
    3：Shop
    ''')

    choice = input("""
    Please choose the function by inputting corresponding number, 
    if you input q, you'll quit the program>>:""").strip()

    if choice == '1':
        user_registering()
    elif choice == '2':
        user_logining()
    elif choice == '3':
        user_shopping()
    elif choice == 'q':
        return
    else:
        print('Invalid operation')

def user_registering():
    username = input('please input your username>>:').strip()
    while True:
        password1 = input('please input your password>>:').strip()
        password2 = input('please verify your password>>:').strip()
        if password1 == password2:
            print('Register successfully, input 2 to login')
            break
        else:
            print('The twice password are inconsistent. Please input again')

    with open(db_file, 'a', encoding='utf-8') as file:
        file.write('%s|%s\n' % (username, password1))
        # flush():刷新文件
        file.flush()

    strat_run()

def user_logining():
    tag = True
    count = 0

    while tag:
        if count == 3:
            print("You've tried too many times. You'll quit the program")
            break
        username = input('username>>:').strip()
        password = input('password>>:').strip()

        # read the user data
        with open(db_file, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip('\n')
                user_info = line.split('|')

                username_of_db = user_info[0]
                password_of_db = user_info[1]

                # verify user data
                if username == username_of_db and password == password_of_db:
                    print('Login successfully')
                    if len(user_info) == 3:
                        balance_of_db = user_info[2]
                        balance = balance_of_db
                        balance = int(balance)
                    else:
                        while True:
                            salary = input('please input your salary>>:').strip()
                            if not salary.isdigit():
                                continue
                            salary = int(salary)
                            balance = salary
                            break

                    # append the username and balance into the list
                    current_user_info = [username_of_db, balance]
                    print('Hello %s, your balance is %s, input 3 to start shopping' % (
                        current_user_info[0], current_user_info[1]))
                    tag = False
                    break
            else:
                print('username or password is invalid')
                count += 1
    strat_run()

def user_shopping():
    if not current_user_info:
        print('Please login first')
    else:
        # get user's balance, and then shop
        username_of_db = current_user_info[0]
        balance = current_user_info[1]

        print('Dear user[%s], your balance is [%s], wish you enjoy your shopping' % (
            username_of_db,
            balance
        ))

        tag = True
        while tag:
            for index, product in enumerate(product_list):
                print(index, product)
            choice = input("Input the numbers of product. if you input q, you'll quit the program>>:").strip()
            if choice.isdigit():
                choice = int(choice)
                if choice < 0 or choice >= len(product_list):
                    continue

                product_name = product_list[choice][0]
                product_price = product_list[choice][1]

                if balance > product_price:
                    if product_name in shopping_cart:  # You've bought the product
                        shopping_cart[product_name]['count'] += 1
                    else:
                        shopping_cart[product_name] = {'product_price': product_price, 'count': 1}

                    balance -= product_price  # deduct money
                    current_user_info[1] = balance  # update user's balance
                    print(
                        "Added product " + product_name + " into shopping cart,your current balance " + str(
                            balance))

                else:
                    print(
                        "You can't afford the product. The price of the product is %s, and you're lack of %s yuan"
                        % (
                            product_price,
                            product_price - balance
                        ))
                print('your shopping cart is %s' % shopping_cart)
            elif choice == 'q':
                print(
                    "--------------------------------The goods list you've bought--------------------------------")

                total_cost = 0
                for i, key in enumerate(shopping_cart):
                    print('%s%23s%23s%23s%23s' % (
                        i,
                        key,
                        shopping_cart[key]['count'],
                        shopping_cart[key]['product_price'],
                        shopping_cart[key]['product_price'] * shopping_cart[key]['count']
                    ))
                    total_cost += shopping_cart[key]['product_price'] * shopping_cart[key]['count']

                print("""
                your total expenditure: %s
                your balance: %s
                """ % (total_cost, balance))

                while tag:
                    inp = input('Confirm purchase(yes/no?)>>: ').strip()
                    if inp not in ['Y', 'N', 'y', 'n', 'yes', 'no']:
                        continue
                    if inp in ['Y', 'y', 'yes']:

                        # write the balance into the file
                        src_file = db_file
                        dst_file = r'%s.swap' % db_file
                        with open(src_file, 'r', encoding='utf-8') as read_file, \
                                open(dst_file, 'w', encoding='utf-8') as write_file:
                            for line in read_file:
                                # startswith() 方法用于检查字符串 是否是以 指定子字符串开头 。
                                if line.startswith(username_of_db):
                                    user_info_line_list = line.strip('\n').split('|')
                                    balance_of_db = balance
                                    balance_of_db = str(balance_of_db)
                                    if len(user_info_line_list) == 2:
                                        user_info_line_list.append(balance_of_db)
                                    else:
                                        user_info_line_list[-1] = balance_of_db
                                    line = '|'.join(user_info_line_list) + '\n'

                                write_file.write(line)
                        os.remove(src_file)
                        os.rename(dst_file, src_file)

                        print("You've bought successfully. Please wait for the goods patiently")

                    shopping_cart = {}
                    current_user_info = []
                    tag = False
            else:
                print('Invalid operation')

        strat_run()

def main():
    """
    主函数，主要用来调用其他函数
    :return: 无
    """
    strat_run()


if __name__ == '__main__':
    main()