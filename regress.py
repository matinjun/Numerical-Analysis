import numpy as np


def regress(x, y, n):
    """根据散点集，生成拟合函数"""
    # 初始条件
    alpha = np.mean(x)
    beta = 0

    # 计算出P[0], P[1]
    P = []
    P.append(np.poly1d([1.]))
    p = np.poly1d([1.0, -alpha]) * P[0]
    P.append(p)

    for k in range(1, n):
        alpha = np.sum(P[k](x) * (P[k] * np.poly1d([1., 0.]))(x)) / np.sum(P[k](x) * P[k](x))
        beta = np.sum(P[k](x) * P[k](x)) / np.sum(P[k - 1](x) * P[k - 1](x))
        p = np.poly1d([1.0, -alpha]) * P[k] - beta * P[k - 1]
        P.append(p)


