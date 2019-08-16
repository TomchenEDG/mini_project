#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time   : 2019/8/16 0016 11:54 
# @Autohor: Sam
# @File   : Chapter08_practice.py


# 八皇后问题
class Solution:
    def __init__(self, n):
        """
        初始化
        :param n: 设置N个皇后
        """
        self.chessboard = [0] * n  # 设置行棋盘
        self.solutions = 0    # 记录所有解

    def queens(self, start_position, number_of_queens):
        """
        算出N皇后问题的解
        :param start_position: 从棋盘第几个位置开始
        :param number_of_queens: 设置多少个皇后
        :return: None
        """
        if (start_position == number_of_queens):
            print(self.chessboard) # 打印解
            self.solutions += 1   # 叠加解的次数
            return

        # 遍历每一位皇后
        for i in range(number_of_queens):
            # 把皇后放在棋盘的位置
            self.chessboard[start_position] = i
            # 检查通过，则进入棋盘下一个位置进行递归
            if self.conflict(start_position) == True:
                self.queens(start_position + 1, number_of_queens)
        return

    def conflict(self, position):
        """
        # 检查 所放皇后的 横向、 纵向、 斜线，是否有冲突
        :param position: 当前皇后的位置
        :return: 冲突则返回True，否则，返回False
        """
        for i in range(position):
            # 检查 当前皇后的位置在 横向、纵向、斜线，是否有冲突
            if self.chessboard[i] == self.chessboard[position] or \
                    abs(self.chessboard[i] - self.chessboard[position]) == position - i:
                return False
        return True


if __name__ == '__main__':
    res = Solution(4)
    res.queens(0, 4)
    print(res.solutions)
