#!/usr/bin/env python 
# -*- coding:utf-8 -*-


import numpy as np

# 四个参数分别为样本特征数据、样本目标数据、维度、阈值
def split(X, y, d, v):
	# 划分后左侧和右侧的索引数组
	index_l = (X[:, d] <= v)
	index_r = (X[:, d] > v)
	return X[index_l], X[index_r], y[index_l], y[index_r]

# 构建一个五行四列的样本数据
X = np.linspace(1, 10, 20)
X = X.reshape(5, 4)
y = 2 * X + 3
print("y:")
print(y)
print()

# 期望以第1个维度，既第1列特征为划分维度，以5为划分阈值
X_l, X_r, y_l, y_r = split(X, y, 0, 5)
print(X_l)
print()
print(y_l)

# 如果以第0个维度，既第0列特征为划分维度，以5为划分阈值，那么X_l为三行四列矩阵，因为第0列的第三行值也小于5
# X_l, X_r, y_l, y_r = split(X, y, 0, 5)
# print(X_l)