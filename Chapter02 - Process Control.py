#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time   : 2019/7/28 0028 10:54 
# @Autohor: Sam
# @File   : Chapter02 - Process Control.py







# 单个人登录认证。
userName = input("请输入您的用户名：")
passWord = input("请输入您的密码：")

while userName != 'Albert' and passWord != '1':
    userName = input("账户信息有误，请重新输入您的用户名：")
    passWord = input("请重新输入您的密码：")
else:
    print("用户认证成功，正在登录.")







# 查看用户权限
showPermission = input("如需查看权限，请输入用户名：")
if showPermission == 'Albert':
    print(showPermission,"超级管理员")
elif showPermission == 'tom':
    print(showPermission, "普通管理员")
elif showPermission == 'jack':
    print(showPermission, "业务主管")
elif showPermission == 'rain':
    print(showPermission, "业务主管")
else:
    print(showPermission, "普通用户")







# 根据日期判断周几
from datetime import datetime

inputDate = input("请输入日期（格式为：2001,5,2）：")
inputDateSplit = inputDate.split(',')
weekDay = datetime(int(inputDateSplit[0]),
               int(inputDateSplit[1]),
               int(inputDateSplit[2])).weekday()+1
if weekDay < 6:
    print("上班。")
else:
    print("出去浪")







# 循环验证用户登录
userName = input("请输入您的用户名：")
passWord = input("请输入您的密码：")
i = 1

while i < 3:
    if userName != 'Albert' and passWord != '1':
        userName = input("账户信息有误，请重新输入您的用户名：")
        passWord = input("请重新输入您的密码：")
        i += 1
    else:
        print("用户通过认证，已登录系统...\n")
        charWord = input("可以输入“q”退出程序：")
        if charWord == "q":
            print("成功退出！")
            break
else:
    print("帐号密码的错误输入超过3次，系统自动退出程序！")






# 猜年龄游戏
guessNumber = 0
albertAge = 18
count = 1

while guessNumber != albertAge:
    if count < 4:
        guessNumber = int(input("你有{}次机会，请输入>>:".format(4 - count)))
        if guessNumber > albertAge :
            print("猜的太大了，往小里试试...\n")
        elif guessNumber < albertAge :
            print("猜的太小了，往大里试试...\n")
        else:
            print("恭喜你,猜对了...")
            break
        count += 1
    else:
        continuePlay = input("是否还想继续玩?  Y：继续玩。 N：不玩了，请输入：")
        if continuePlay == 'Y':
            count = 1
            continue
        else:
            print('游戏已退出，谢谢您的参与！')
            break
else:
    print("恭喜你,猜对了...")





# # 使用while循环输出1 2 3 4 5 6  7  8 9 10
count = 0
while count < 10:
    count += 1
    print("count:{}".format(count))




# 求1-100的所有数的和
count = 1
totalSum = 0

while count < 101:
    totalSum = totalSum + count
    count += 1
print("count:{}".format(totalSum))




# # 输出 1-100 内的所有奇数
count = 0
while count <= 100:
    if count%2 == 1:
        print ('loop',count)
    count += 1





# 输出 1-100 内的所有偶数
count = 0
while count <= 100:
    if count%2 == 0:
        print ('loop',count)
    count += 1





# 求1-2+3-4+5 ... 99的所有数的和
num = 0
for i in range(100):
    if i % 2 == 0:
        num = num - i
    else:
        num = num + i
print(num)







# 打印如下金字塔图形
for i in range(5):
    for k in range(4-i):
        print(" ",end=" ")
    for j in range(2*i+1):
        print("*", end=" ")
    print()