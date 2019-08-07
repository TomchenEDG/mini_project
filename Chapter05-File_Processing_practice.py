#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time   : 2019/8/6 0006 20:23 
# @Autohor: Sam
# @File   : Chapter05 - File Processing_practice.py





# 练习一:
# 写一个程序：在要保持文件内容的顺序不变的前提下，去除文件中重复的行。

list_file_content = []
with open(r'a1.txt', mode='r', encoding='utf-8') as rfile:
    for c in rfile:
        list_file_content.append(c)

resule_content = []
set_file_content = set()
for i in list_file_content:
    if i not in set_file_content:
        set_file_content.add(i)
        resule_content.append(i)

with open('a2.txt', mode='w', encoding='utf-8') as wfile:
    wfile.writelines(resule_content)





# 练习2：
# 写一个在终端执行拷贝文件的命令，文件不仅限于文本文件，
# 要求是：在终端环境下输入命令：

import shutil,sys
def fileCopy(source_fil_path, target_file_path):
    shutil.copyfile(source_fil_path, target_file_path)

if __name__ == '__main__':
    # Sys.argv[] 其实就是一个列表，里边的项为用户输入的参数，关键是这参数是从程序外部输入的。
    if len(sys.argv) != 3:
        print("请输入 文件.py + 空格 + 源文件地址 + 空格 + 目标文件地址")
    else:
        shutil.copyfile(sys.argv[1], sys.argv[2])





# 练习三
# 写一个修改文件的程序，要求是原来的内容不能被覆盖，
# 修改之后字符之间的空格不能变化（4个空格）
# 源文件内容如下：
# 马一特    18    male
# 刘德华    50    male
# 林志玲    20    female
# 修改为：
# 马一特{Albert}    18    male
# 刘德华    50    male
# 林志玲     20    female

list_file_content = []
with open('Chapter05.txt', mode='r+t', encoding='utf-8') as rtfile:
    for str in rtfile:
        if str.find("马一特") == 0:
            list_file_content.append(str)
    rtfile.seek(0)
    rtfile.writelines(list_file_content[0][0:3] + '{Albert}' + list_file_content[0][3:])
