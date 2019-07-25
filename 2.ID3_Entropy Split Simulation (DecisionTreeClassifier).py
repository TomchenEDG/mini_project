#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# ID3决策树
import numpy as np
from collections import Counter
from math import log
from sklearn import datasets

# 1.数据准备X,y
iris = datasets.load_iris()
X = iris.data[:,2:]
y = iris.target

def entropy(y):
    counter = Counter(y)
    res = 0.0
    for num in counter.values():
        p = num / len(y)
        res += -p * log(p)
    return res

# 这里主要是决策树解决连续特征的做法。这代码其实C4.5的做法，而不是ID3
def split(X, y, d, value):
    # 大于v的值放右边，小于等于v的值放左边
    index_a = (X[:,d] <= value)
    index_b = (X[:,d] > value)
    return X[index_a], X[index_b], y[index_a], y[index_b]

# # 找到最大的信息熵差值，最优的划分特征和最优的划分边界
def try_split(X, y):
    # best_entropy：float('inf')设置成无穷大
    best_entropy = float('inf')
    best_d, best_v = -1, -1
    # 遍历所有属性分别计算信息增益，信息增益最大（不确定性最高）的那个属性将作为划分属性。
    # d：获取特征列数
    for d in range(X.shape[1]):
        # sorted_index : 获取列的从小到大的索引。
        sorted_index = np.argsort(X[:, d])
        for i in range(1, len(X)):
            # X[sorted_index[i], d]: d指定列，获取X的从小到大的值。
            # 不能使用相等的值进行循环。
            if X[sorted_index[i], d] != X[sorted_index[i - 1], d]:
                # （X第一列的第二个值 + X第一列的第一值）/2，赋值给v
                v = (X[sorted_index[i], d] + X[sorted_index[i - 1], d]) / 2
                # 开始根据v的值分割 X数据,y数据，大于v的值放右边，小于等于v的值放左边。
                X_l, X_r, y_l, y_r = split(X, y, d, v)
                # 计算左边和右边的y的信息熵。
                e = entropy(y_l) + entropy(y_r)
                # 找到最小的信息熵
                if e < best_entropy:
                    best_entropy, best_d, best_v = e, d, v

    return best_entropy, best_d, best_v

best_entropy, best_d, best_v = try_split(X, y)
print("best_entropy =", best_entropy)
print("best_d =", best_d)
print("best_v =", best_v)